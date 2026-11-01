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

    return[count , summ]
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
#8 задача
def sum_array(a):
    pass
    return sum(a)

#9 задача 
def sum_mix(arr):
    #your code here
    return sum(int(x)for x in arr)
#10
def invert(lst):
    pass
    return [-i for i in lst]
#11 
def hero(bullets, dragons):
    return bullets >= dragons * 2
#12
def friend(x):
    #Code
    return [name for name in x if len(name) == 4 ]
#13
def maps(a):
    pass
    return [x * 2 for x in a]
#14 
def even_or_odd(number):
    pass
    if number % 2 == 0: 
        return "Even"
    else: 
        return "Odd"
#15
def smash(words):
    return " ".join(words)
#16
def repeat_str(repeat, string):
    return string * repeat
#17
def count_sheeps(sheep):
    return sheep.count(True)
# TODO May the force be with you
#18
def dna_to_rna(dna):
    return dna.replace ('T', 'U')
#19
def find_average(numbers):
    # your code here
    pass
    if len(numbers) == 0: 
        return 0 
    return sum(numbers) / len(numbers)
#20
def descending_order(num):
    # Bust a move right here
       return int(''.join(sorted(str(num), reverse = True)))
#21
def find_smallest_int(arr):
    # Code here
    return min(arr)
#22
def make_upper_case(s):
    # Code here
    return s.upper()
#23
def reverse_seq(n):
    pass
    return list(range(n,0,-1))
#24
def solution(text, ending):
    # your code here...
    pass
    return text.endswith(ending)
#25 
def get_middle(s):
    pass
    return s[(len(s)-1)//2:len(s)// 2+1]