import random


def check_entropy(original_deck, shuffled_deck):
    entropy = []
    ind = 0
    while ind < len(original_deck):
        el = original_deck[ind]
        shuffled_index = shuffled_deck.index(el)
        subset = [el]
        if (
            shuffled_index < len(shuffled_deck) - 1
            and ind < len(original_deck) - 1
            and original_deck[ind + 1] == shuffled_deck[shuffled_index + 1]
        ):
            while (
                shuffled_index < len(shuffled_deck) - 1
                and ind < len(original_deck) - 1
                and original_deck[ind + 1] == shuffled_deck[shuffled_index + 1]
            ):
                shuffled_index += 1
                ind += 1
                subset.append(original_deck[ind])
        else:
            ind += 1
        if len(subset) > 3:
            entropy.append(subset)
    ind = 0
    shuffled_deck = list(reversed(shuffled_deck))
    while ind < len(original_deck):
        el = original_deck[ind]
        shuffled_index = shuffled_deck.index(el)
        subset = [el]
        if (
            shuffled_index < len(shuffled_deck) - 1
            and ind < len(original_deck) - 1
            and original_deck[ind + 1] == shuffled_deck[shuffled_index + 1]
        ):
            while (
                shuffled_index < len(shuffled_deck) - 1
                and ind < len(original_deck) - 1
                and original_deck[ind + 1] == shuffled_deck[shuffled_index + 1]
            ):
                shuffled_index += 1
                ind += 1
                subset.append(original_deck[ind])
        else:
            ind += 1
        if len(subset) > 3:
            entropy.append(subset)

    return entropy


def calculate_entropy(entropy):
    entropy_sum = 0
    for subset in entropy:
        entropy_sum += 0.148483 * len(subset) ** 3.1344 + 4.67464
    return entropy_sum


def shuffle_deck_method1(deck):
    for _ in range(5):
        left_count = random.randint(0, 8)
        half1 = deck[:left_count]
        half2 = deck[left_count:]
        while len(half2) > 0:
            card_count = random.randint(3, 9)
            if card_count > len(half2):
                card_count = len(half2)
            unshifted_card = half2[:card_count]
            half2 = half2[card_count:]
            half1 = [*unshifted_card, *half1]
        deck = half1
    return deck


def shuffle_deck_method2(deck):
    for _ in range(7):
        left_count = random.randint(0, 8)
        half1 = deck[:left_count]
        half2 = deck[left_count:]
        direction = True
        while len(half2) > 0:
            card_count = random.randint(3, 9)
            if card_count > len(half2):
                card_count = len(half2)
            unshifted_card = half2[:card_count]
            half2 = half2[card_count:]
            if direction:
                half1 = [*unshifted_card, *half1]
            else:
                half1 = [*half1, *unshifted_card]
            direction = not direction
        deck = half1

    return deck


def combined(deck):
    for _ in range(5):
        left_count = random.randint(0, 8)
        half1 = deck[:left_count]
        half2 = deck[left_count:]
        counter = 0
        while len(half2) > 0:
            card_count = random.randint(3, 9)
            if card_count > len(half2):
                card_count = len(half2)
            unshifted_card = half2[:card_count]
            half2 = half2[card_count:]
            if counter < 2:
                half1 = [*unshifted_card, *half1]
                counter += 1
            if counter == 2:
                half1 = [*half1, *unshifted_card]
                counter = 0

        deck = half1

    return deck


deck = [i for i in range(52)]


def random_shuffle(a):
    n = len(a)
    copied = a.copy()
    for i in range(0, n):
        r = random.randint(0, n - 1)
        copied[i], copied[r] = copied[r], copied[i]
    return copied


def stats(deck, shuffle_method, iterations=10):
    entropy_koefs = []
    for _ in range(iterations):
        current = calculate_entropy(check_entropy(deck, shuffle_method(deck)))
        entropy_koefs.append(current)

    return (
        max(entropy_koefs),
        min(entropy_koefs),
        sum(entropy_koefs) / len(entropy_koefs),
    )


print("method 1", stats(deck, shuffle_deck_method1, 10000))
print("method 2", stats(deck, shuffle_deck_method2, 10000))
print("combined", stats(deck, combined, 10000))

