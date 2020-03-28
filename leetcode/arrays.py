import math
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

def reveal(l):
    while len(l) >= 2:
        print(l.pop(0))
        l.append(l.pop(0))

    print(l.pop())


def findallduplicates(l):
    all_items  = []
    dups = []

    for items in l:
        if items in all_items and items not in dups:
            dups.append(items)

        else:
            all_items.append(items)

    return dups


def sortColors(l):
    for x in range(len(l)-1):
        minindex = x
        minimum = l[x]
        for y in range(x+1, len(l)):
            if l[y] < l[x]:
                minindex = y
        l[x], l[minindex] = l[minindex],l[x]

def productExceptSelf(nums):
    output = []
    queue = nums.copy()

    for x in range(len(nums)):
        temp = queue.pop(0)

        product = 1

        tempqueue = []
        while queue:
            item = queue.pop(0)
            product *= item
            tempqueue.append(item)

        while tempqueue:
            queue.append(tempqueue.pop(0))

        queue.append(temp)
        output.append(product)

    return output

def subArraysInLength(l, length):
    subarrays = []
    for x in range(len(l)-length):
        subarrays.append(l[x:x+length])

    return subarrays

def maximumSumTwoNoOverlap(a, l, m):
    """A is a list."""

    subArraysofLengthl = subArraysInLength(a, l)
    subArraysofLengthM = subArraysInLength(a, m)

    sums = []

    for x in range(len(subArraysofLengthl)):
        for y in range(len(subArraysofLengthM)):
            sums.append(sum(subArraysofLengthM[y]) + sum(subArraysofLengthl[x]))

    return max(sums)


def subsets(l):
    """Return all possible subsets of the list."""

    ssets = []

    for x in range(len(l)):
        for y in range(len(l), x-1, -1):
            if l[x:y] not in ssets:
                ssets.append(l[x:y])

    return ssets

def inAllWords(char, l):
    for words in l:
        if char not in words:
            return False

    return True

def replaceLetter(word, index):
    newString = ""

    for x in range(len(word)):
        if x!=index:
            newString += word[x]

    return newString
def removeFirstOccurence(char, l):
    for x in range(len(l)):
        for y in range(len(l[x])):
            if l[x][y] == char:
                l[x] = replaceLetter(l[x], y)
                break


def commonchars(l):
    common = []
    restOfList = l[1:]
    for char in l[0]:
        if inAllWords(char, restOfList):
            removeFirstOccurence(char, restOfList)
            common.append(char)

    return common

def firstLastArray(nums, target):

    if nums == []:
        return [-1,-1]
    midPoint = len(nums) // 2
    output = [-1,-1]
    if target < nums[midPoint]:
        for x in range(midPoint):
            if nums[x] == target:
                output[0] = x
                output[1] = x

                for y in range(x+1, midPoint):
                    if nums[y] == target:
                        output[1] = y

                break

    elif target > nums[midPoint]:
        for x in range(midPoint, len(nums)):
            if nums[x] == target:
                output[0] = x
                output[1] = x

                for y in range(x+1, len(nums)):
                    if nums[y] == target:
                        output[1] = y

                break

    else:
        counter1 = midPoint
        counter2 = midPoint

        while nums[counter1] == target and counter1 >= 0:
            output[0] = counter1
            counter1 -=1

        while counter2 < len(nums) and nums[counter2] == target:
            output[1] = counter2
            counter2 +=1

    return output
def fib(n):
    if n <= 1:
        return 1

    else:
        return fib(n-1) + fib(n-2)


def discreteTest(n):
    ls = fib(n-1) * fib(n+1)-(fib(n)*fib(n))

    rs = math.pow(-1,n+1)

    if ls != rs:
        print("found")



def wiggleSort(l):
    for x in range(0, len(l),2):
        min = l[x]
        for y in range(x-1, len(l)):
            if l[y] < min:
                min = l[y]
                l[x], l[y] = l[y],l[x]

def wiggleSort2(l):
    l.sort()

    for x in range(1, len(l)-1, 2):
        l[x], l[x+1] = l[x+1], l[x]


def roomAvailable(room, starttime, endtime):
    for meetings in room:
        meetingStartTime = meetings[0]
        meetingEndTime = meetings[1]

        if starttime >= meetingStartTime and starttime <= meetingEndTime:
            return False

    return True

def meetingRooms(l):
    """Given a list of meeting times, figure out the minimum rooms we need."""

    rooms = []
    for meetingTimes in l:
        starttime = meetingTimes[0]
        endTime = meetingTimes[1]
        roomFound = False
        for room in rooms:
            if roomAvailable(room, starttime, endTime):
                room.append((starttime, endTime))
                roomFound = True
                break

        if not roomFound:
            rooms.append([(starttime, endTime)])

    return len(rooms)


def firstMissingPositive(nums):
        nums.sort()

        if nums == []:
            return 1

        counter = 0
        for x in range(len(nums) - 1):
            if nums[x] > 0:
                counter += 1

                if nums[x] != counter:
                    return counter

        if counter == 0:
            return 1

        else:
            return nums[-1] + 1


def deckRevealedIncreasingOrder(deck):
    simulator = [x for x in range(len(deck))]
    retList = [None]*len(deck)
    sortedDeck = sorted(deck)

    for items in sortedDeck:
        retList[simulator.pop(0)] = items

        if simulator:
            simulator.append(simulator.pop(0))

    return retList

def findAllDuplicates(nums):
    elements = {}
    final = []
    for i in range(1, len(nums) + 1):
        elements[i] = 0

    for items in nums:
        elements[items] += 1

        if elements[items] == 2:
            final.append(items)

    return final


def reverseList(nums):
    """Reverse the list."""

    for x in range(len(nums)//2):
        nums[x], nums[len(nums)-1-x] = nums[len(nums)-1-x], nums[x]

def binarySearch(l, item):
    if l == []:
        return False

    else:
        midpoint = len(l)//2
        middleElement = l[midpoint]

        if middleElement == item:
            return True

        elif (item < middleElement):
            return binarySearch(l[:midpoint], item)

        else:
            return binarySearch(l[midpoint+1:], item)
def k_difference(l, k):
    dict = {}

    for items in l:
        dict[items] = None

    counter = 0
    for items in l:
        if items + k in dict:
            counter += 1

    return counter

def getPath(startingPoint, magic, dist):
    currentIndex = startingPoint
    totalPower = 0
    totalIterations = 0
    for x in range(len(magic)):
        totalPower += magic[currentIndex]

        if totalPower >= dist[currentIndex]:
            totalPower -= dist[currentIndex]

        else:
            return -1, totalPower

        if currentIndex < len(magic)-1:
            currentIndex +=1

        else:
            currentIndex = 0

        totalIterations += 1

    return totalIterations, totalPower

def aladin(magic, dist):
    maxDist = {}
    for x in range(len(magic)):
        cycleLength, totalPower = getPath(x, magic, dist)[0][1]

        if cycleLength != -1:
            pass

        else:
            maxDist[x] = (cycleLength, totalPower)

    maxIndex = 0

    for items in maxDist:
        if maxDist[items][0] > maxDist[maxIndex][0]:
            maxIndex = items


    print(maxDist)
    return maxIndex

def diagonalWin(arr):
    """Given an nxn array, return true if there's a diagonal win from top left."""
    counter = 0
    index = 0

    while index < len(arr):
        if arr[index][index] == "x":
            counter += 1

        index += 1

    return counter == len(arr)

def leadingZeroes(num):
    s = str(num)
    charArray = []
    for items in s:
        charArray.append(items)

    counter = 0
    while len(charArray)<7:
        counter += 1
        charArray.insert(0,0)


    return "Leading Zeroes: " + str(counter)


def reverseAndInvert(row):
    """Reverse and Flip this 1d Array."""

    for x in range(len(row)//2):
        if row[x] == 0:
            row[x] = 1
        else:
            row[x] = 0

        if row[0-x] == 0:
            row[0-x] = 1
        else:
            row[0-x] = 0

        row[x],row[0-x] = row[0-x], row[x]
        return row
def flippingAnImage(arr):
    """Flip and invert image."""

    for row in arr:
        reverseAndInvert(row)


def sortParity(arr):
    odd = []
    even = []

    for items in arr:
        if (items % 2 ==0 ):
            even.append(items)

        else:
            odd.append(items)
    return even + odd

def squareArray(arr):
    squares = []
    for items in arr:
        squares.append(arr*arr)

    return squares

def heightChecker(arr):
    counter = 0

    for x in range(1, len(arr)):
        if arr[x-1] > arr[x]:
            arr[x-1],arr[x] = arr[x],arr[x-1]
            counter += 1

    return counter


def numberofOddNumberDigits(arr):
    counter = 0
    for elements in arr:
        if (numberOfDigits(elements, 1) % 2 == 1):
            counter += 1

    return counter

def numberOfDigits(element, currentPoint):
    if element < math.pow(10, currentPoint):
        return currentPoint

    return numberOfDigits(element, currentPoint+1)

def reverse(arr):
    """
    reverse the arr in inplace.
    """
    for x in range(len(arr)//2):

        arr[x], arr[len(arr)-1-x] = arr[len(arr)-1-x], arr[x]

    return arr

def binary_search(arr, element):
    """use binary search to find the element in the arr."""

    if arr == []:
        return False

    mid_point = len(arr)//2

    if arr[mid_point] == element:
        return True

    elif element < arr[mid_point]:
        return binary_search(arr[:mid_point], element)

    else:
        return binary_search(arr[mid_point+1:],element)


def osmosis_array(arr):
    output_list = []
    for elements in arr:
        if output_list == []:
            output_list.append(elements)

        else:
            if output_list[-1] == elements:
                output_list[-1] = elements*2

            else:
                output_list.append(elements)
    return output_list



print(osmosis_array([1,1,2,3]))


