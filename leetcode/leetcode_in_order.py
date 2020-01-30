def decompressRLElist(nums):
    output = []
    for x in range(0, len(nums), 2):
        freq = nums[x]
        value = nums[x + 1]

        output.extend([value] * freq)

    return output
