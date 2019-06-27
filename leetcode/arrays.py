def flip(list):
    flippedlist = []
    for x in range(len(list)-1,-1,-1):
        flippedlist.append(list[x])

    for x in range(len(flippedlist)):
        list[x] = flippedlist[x]


def flipandInvertImage(a):
    for lists in a:
        flip(lists)

    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] == 0:
                a[x][y] = 1

            else:
                a[x][y] = 0

def sortArrayByParity(l):
    sortedbyparity = []
    for items in l:
        if items % 2 == 0:
            sortedbyparity.append(items)

    for items in l:
        if items % 2 != 0:
            sortedbyparity.append(items)

    return sortedbyparity

def heightChecker(A):
    sortlist = sorted(A)
    counter = 0
    for x in range(len(A)):
        if A[x] != sortlist[x]:
            counter += 1

    return counter


def shapeMatric(l, r, c):
    shaped = []
    counter = 0
    cr = 0
    cl = 0
    for x in range(r):
        row = []

        while len(row) < c:
            row.append(l[cr][cl])

            if cl == len(l[cr])-1:
                cr += 1
                cl = 0

            else:
                cl += 1

        shaped.append(row)

    return shaped





def reshapeMatrix(l, r, c):
    """Reshape the matrix."""

    rows = len(l)
    cols = len(l[0])

    # Dimensions are Rows * Cols.
    # NEed to reshape to r * c.

    if rows * cols == r * c:
        l = shapeMatric(l, r, c)

    return l

def singleNumber(l):
    temp = []
    for items in l:
        if items in temp:
            temp.remove(items)

        else:
            temp.append(items)

    return temp[0]


print(reshapeMatrix([[1,2],[3,4]],1,4))


