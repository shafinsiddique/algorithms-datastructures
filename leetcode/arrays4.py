def two_sum(arr, target):
    """given an arr and a target, return indices of two elements that add up to
    target.

    guaranteed to have a solution."""

    elements_dict = {}

    for x in range(len(arr)):
        elements_dict[arr[x]] = x

    for x in range(len(arr)):
        if target - arr[x] in elements_dict and elements_dict[target-arr[x]] != x:
            return [x, elements_dict[target-arr[x]]]

def best_time_to_buy_and_sell_stock(arr):
    """the intuition behind this algorithm is that you want the min element on the left
    hand side and the max element on the right hand side. Such when u subtract,
    you get profit. The apporoach im thinking of is you keep a min variable keeping tracking
    of each new minimum. This is because whenever we find a value lower than our current_min,
    we have the possibility that there might be number to its right that
    gives us a greater profit."""

    min = arr[0]
    max_profit = 0

    for x in range(1, len(arr)):
        if arr[x] < min:
            min = arr[x]

        else:
            if arr[x] - min > max_profit:
                max_profit = arr[x] - min

    return max_profit

print(best_time_to_buy_and_sell_stock([7,1,5,3,6,4]))