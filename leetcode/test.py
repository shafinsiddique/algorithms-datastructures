import requests as re
from datetime import date, timedelta
import datetime
def convertMonthToNumber(monthName):
    d = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,
         "July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

    return (d[monthName])


def convertWeekDayToNumber(weekDay):
    d = {"Sunday":6,"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5}

    return d[weekDay]

def convertNumberToMonth(number):
    d = {1:"January",2:"February", 3:"March",4:"April",5:"March", 6:"June",
         7:"July", 8:"August",9:"September",10:"October",
         11:"November",12:"December"}

    return d[number]

def convertNumberToWeek(number):
    d = {1:"Tuesday",2:"Wednesday",3:"Thursday", 4:"Friday",5:"Saturday", 6:"Sunday", 0: "Monday"}

    return d[number]
def getAllDates(firstDate, lastDate, weekday):
    firstDay = firstDate.split("-")

    weekday = convertWeekDayToNumber(weekday)

    firstDay = datetime.date(int(firstDay[-1]), convertMonthToNumber(firstDay[1]), int(firstDay[0]))

    secondDate = lastDate.split("-")

    secondDate = datetime.date(int(secondDate[-1]),
                               convertMonthToNumber(secondDate[1]), int(secondDate[0]))
    allDates = []

    foundAllDates = False

    adder = 0
    while not foundAllDates:
        newDate = firstDay + timedelta(days=adder)

        if newDate.weekday() == weekday:
            allDates.append(newDate)

        if newDate > secondDate:
            foundAllDates = True

        adder += 1

    return allDates

def stock(firstDay, lastDay, weekday):
    allDates = getAllDates(firstDay, lastDay, weekday)
    query = "https://jsonmock.hackerrank.com/api/stocks/search?date="
    outputList = []
    for date in allDates:
        day = str(date.day)
        if date.day < 10:
            day = "0" + str(date.day)

        dateString = day + "-" + convertNumberToMonth(date.month) + "-" + str(date.year)
        page = re.get(query + dateString).json()

        if page['total'] > 0:
            for dictionaries in page['data']:
                if str(dictionaries['date']) == dateString:
                    outputList.append(dictionaries)
                    break

        else:
            day = str(date.day)
            dateString = day + "-" + convertNumberToMonth(date.month) + "-" + str(date.year)
            newPage = re.get(query + dateString).json()

            for dictionaries in newPage['data']:
                if str(dictionaries['date']) == dateString:
                    outputList.append(dictionaries)
                    break

    return outputList

def longestAlphabeticalSubstring(s):
    """Given a string return the longest substring that is in alphabetical string."""

    alphabeticalSubstrings = []
    for x in range(len(s)):
        for y in range(len(s),x,-1):
            if isAlphabetical(s[x:y]):
                alphabeticalSubstrings.append(s[x:y])
    longestSubstring = ''
    for strings in alphabeticalSubstrings:
        if len(strings) >= len(longestSubstring):
            longestSubstring = strings

    return longestSubstring


def isAlphabetical(string):
    '""Return if a string is in alphabetical format.'

    for x in range(len(string)-1):
        if ord(string[x]) > ord(string[x+1]):
            return False

    return True

def subArrayHasKOddNumbers(subarray,k):
    """Return the subarray has exact k odd numbers."""

    oddCounter = 0

    for items in subarray:
        if items % 2 != 0:
            oddCounter += 1

    return oddCounter == k
def satisfyingSubarrays(arr, k):
    subArrays =[]

    for x in range(len(arr)):
        for y in range(len(arr), x, -1):
            if len(arr[x:y]) >= k:
                if subArrayHasKOddNumbers(arr[x:y],k):
                    subArrays.append(arr[x:y])

    return len(subArrays)

print(satisfyingSubarrays([1,4,6,8,10],1))


