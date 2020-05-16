def plus_one(arr):
    """given an arr of integers, add 1 to it."""

    output_reversed = []
    carried = 1
    for x in range(len(arr)-1,-1,-1):
        sum_number = arr[x] + carried

        if sum_number > 10:
            carried = 1
            output_reversed.append(sum_number % 10)

        else:
            carried = 0
            output_reversed.append(sum_number)
    output = []
    for x in range(len(output_reversed)-1,-1,-1):
        output.append(output_reversed[x])

    return output
