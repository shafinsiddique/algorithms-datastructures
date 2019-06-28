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

def duplicate_zeroes(l):
    orglen = len(l)
    counter= 0
    while counter < len(l):

        if l[counter] == 0:
            l.insert(counter+1,0)
            counter += 2
        else:
            counter += 1
    counter = -1
    if len(l) > orglen:
        while len(l) != orglen:
            l.pop(-1)

def fairCandySwap(l1, l2):
    for x in range(len(l1)):
        for y in range(len(l2)):
            l1without = l1[:x] + l1[x+1:]
            l2without = l2[:y] + l2[y+1:]

            if sum(l1without) + l2[y] == sum(l2without) + l1[x] :
                return [l1[x],l2[y]]

# def rob(nums):
#     sums = []
#
#     if len(nums) == 0:
#         return 0
#
#     elif len(nums) <=2 :
#         return nums[0]
#
#     else:
#         for x in range(len(nums)):
#             sums.append(nums[x])
#
#             for y in range(x+2,len(nums),2):
#                 sums[-1] += nums[y]
#
#
#         return max(sums)

def monotonicincreasing(l):
    for x in range(len(l)):
        if l[x] != min(l[x:]):
            return False

    return True

def monotonicdecreasing(l):
    for x in range(len(l)):
        if l[x] != max(l[x:]):
            return False

    return True
def monotonic(l):
    if monotonicdecreasing(l) or monotonicincreasing(l):
        return True
    return False


def maxProfit(p):
    profits = []

    counter = 0
    while counter < len(p)-1:
        if p[counter+1] > p[counter]:
            buyprice =  p[counter]
            sellprice = p[counter+1]
            newcounter = counter + 1
            counter += 2
            while newcounter < len(p)-1 and p[newcounter] < p[newcounter+1]:
                sellprice = p[newcounter+1]
                counter = newcounter + 2
                newcounter+=1

            profits.append(sellprice - buyprice)
        else:
            counter += 1

    return sum(profits)

def twoSumII(numbers, target):
    for x in range(len(numbers)-1):
        for y in range(x+1,len(numbers)):
            if numbers[x] + numbers[y] == target:
                return [x+1,y+1]

            elif numbers[x] + numbers[y] > target:
                break

def buySellStock(prices):
    profits = []

    if sorted(prices, reverse=True) == prices:
        return 0
    else:
        for x in range(len(prices)-1):
            for y in range(x+1, len(prices)):
                profits.append(prices[y]-prices[x])

print(buySellStock([]))

