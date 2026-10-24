#1 задача
def find_needle(haystack):
     return "found the needle at position " + str(haystack.index("needle"))
#2 задча
def count_positives_sum_negatives(arr):
    if arr == None or len(arr) == 0: 
        return []
    
    count = 0
    summ = 0
    
    for x in arr:
        if x > 0:
            count += 1
        elif x < 0:
            summ += x

    return[count, summ]
#3 задача
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump: 
        return True
    else: 
        return False 
#4 задача 
def solution(string):
    pass
    return string[::-1]
#5 задача 