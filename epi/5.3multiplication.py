def multiplication(arr1, arr2):
    """given two array representing integers,
    return an array representing the product.

      """
    sum = []
    counter = 0
    for x in range(len(arr1)-1, -1, -1):
        carried = 0
        product = [0]*counter
        for y in range(len(arr2)-1,-1,-1):
            cur_product = (arr1[x]*arr2[x]) + carried
            product.append(cur_product % 10)
            carried = cur_product // 10








