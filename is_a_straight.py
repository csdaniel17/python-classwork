## Is it a straight?

# Implement a function to determine if a list of 7 cards is a straight. The cards will be represented as numbers representing the point values of the cards. is_a_straight(cards).

# Example:

# is_a_straight([1, 2, 3, 4, 5, 6, 7]) => True
# is_a_straight([4, 2, 1, 8, 3, 5]) => True
# is_a_straight([1, 2, 3, 3, 3, 4, 5]) => True
# is_a_straight([4, 4, 2, 1, 9, 10, 11]) => False


def is_a_straight(cards):
    cards.sort()
    streak = 1
    for i in range(1, len(cards)):
        last_card = cards[i - 1]
        curr_card = cards[i]
        if curr_card - last_card == 1:
            streak = streak + 1
        elif curr_card == last_card:
            pass
        else:
            streak = 1
        if streak == 5:
            return True
    return False


print is_a_straight([1, 2, 3, 4, 5, 6, 7])  # True
print is_a_straight([4, 2, 1, 8, 3, 5])  # True
print is_a_straight([1, 2, 3, 3, 3, 4, 5])  # True
print is_a_straight([4, 4, 2, 1, 9, 10, 11])  # False
print is_a_straight([3, 4, 2, 1, 9, 10, 11])  # False
print is_a_straight([1, 2, 3, 5, 6, 7, 8, 9, 10])  # True
