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

l = [[1,1,0],[1,0,1],[0,0,0]]
flipandInvertImage(l)
print(l)


