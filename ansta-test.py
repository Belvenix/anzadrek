import re
from decimal import *

def generatePostalCodes(start, end):
    '''
    Generate all possible postal codes between start and end parameters (inclusive).
    
    No data validation.
    
    Parameters:
        start (str): The Postal Code string from which we start the generation.
        
        end (str): The postal code string which end the generation.
        
    Returns:
        result (array(str)): An array of all possible postal codes between start and end parameters (inclusive)
    
    '''
    startFirst, startSecond = int(start[0:2]), int(start[3:6])
    endFirst, endSecond = int(end[0:2]), int(end[3:6])
    startN = startFirst * 1000 + startSecond
    endN = endFirst * 1000 + endSecond
    result = []
    for i in range(startN, endN + 1):
        fir = str(i // 1000)
        sec = str(i % 1000)
        if int(fir) // 10 == 0:
            fir = '0' + fir
        if int(sec) // 100 == 0:
            sec = '0' + sec
        if int(sec) // 10 == 0:
            sec = '0' + sec
        code = fir + '-' + sec
        result.append(code)
    return result
    
def findMissing(partial, n):
    '''
    Find all missing numbers from 1 to n, which are not included in partial list (inclusive).
    
    No data validation.
    
    Parameters:
        partial (array(int)): Array of numbers in that are 'not missing'.
        
        n (int): The last elemnt of the 1..n list (inclusive).
        
    Returns:
        result (array(int)): An array of missing numbers from 1..n list (inclusive)
    
    '''
    result = []
    for i in range (1, n + 1):
        if i not in partial:
            result.append(i)
    return result
        
    
def generateList(start, end, jump):
    '''
    Custom range() function.
    
    No data validation.
    
    Parameters:
        start (float): Starting number of the array.
        
        end (float): Last number of the array.
        
        jump (float): difference between each element in the list.
        
    Returns:
        result (array(Decimal)): [start, start + 1 * jump, start + 2 * jump, ..., end]
    
    '''
    result = []
    start, end, jump = Decimal(start), Decimal(end), Decimal(jump)
    while start <= end:
        result.append(start)
        start += jump
    return result
    
    
def test():
    print("\nFirst exercise result")
    print(generatePostalCodes('79-900', '80-155'))
    
    print("\nSecond exercise result")
    print(findMissing([2,3,7,4,9], 10))
    
    print("\nThird exercise result")
    print(generateList(2, 5.5, .5))
