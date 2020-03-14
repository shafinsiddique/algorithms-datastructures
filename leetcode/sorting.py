def heap_sort(l):
    length = len(l) -1
    leastParent = length // 2

    for i in range(leastParent,-1,-1):
        moveDown(l, i, length)


    for i in range(length, 0, -1):
        if l[0] > l[i]:
            swap(l, 0, i)
            moveDown(l, 0, i-1)


def moveDown(l, first, last):
    largest = 2*first +1

    while largest <= last:
        if (largest < last) and l[largest] < l[largest + 1]:
            largest += 1


        if l[largest] > l[first]:
            swap(l, largest, first)
            first = largest
            largest = 2*first+1

        else:
            return


def swap(l, i, j):
    l[i],l[j] = l[j], l[i]

l = [1,1,1,1,1,1]


heap_sort(l)

print(l)
