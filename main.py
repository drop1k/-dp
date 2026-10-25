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
def string_to_number(s):
    # your code here
    pass
    return int(s)
#6 задача
def better_than_average(class_points, your_points):
    # Your code here
    suma = 0 
    for i in class_points: 
        suma = suma + i 
        
    suma = suma + your_points 
    srednee = suma / (len(class_points) + 1)
    
    if your_points > srednee: 
        return True 
    else:
        return False 
#7 задача
def simple_multiplication(number) :
    # Your code goes here

    if number % 2 == 0: 
        return number * 8 
    else: 
        return number * 9