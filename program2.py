numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[x for x in numbers if x % 2==0]
odd_numbers=[x for x in numbers if x % 2 !=0]
print('number:' , numbers)
print('even number:' , even_numbers)
print('odd number:' , odd_numbers)