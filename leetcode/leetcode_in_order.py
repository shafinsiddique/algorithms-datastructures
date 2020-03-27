def decompressRLElist(nums):
    output = []
    for x in range(0, len(nums), 2):
        freq = nums[x]
        value = nums[x + 1]

        output.extend([value] * freq)

    return output

def defangIPAddr(address):
    return address.replace(".","[.]")

def even_numbers(nums):
    counter = 0
    for items in nums:
        if len(str(items)) % 2 == 0:
            counter += 1

    return counter
