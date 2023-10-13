from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


print(list(map(lambda pet: pet.upper(), my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


print(list(filter(lambda score: score>50, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

print(reduce(lambda acc,item: acc+item, scores+my_numbers))


#5 Square
my_list=[5,4,3]

print(list(map(lambda item: item*item, my_list)))

#6 List of tupples sorting

a = [(0,2),(4,3),(10,-1),(9,9)]

a.sort(key=lambda pair: pair[1])

print(a)

#7 List, set, dict compehensions

my_list = [char for char in 'hello']
my_list2 = [num*2 for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100) if num % 2 ==0]
# print (my_list)
# print (my_list2)
# print (my_list3)

simple_dict = {
    'a':1,
    'b':2,
    'c':3
}
my_dict = { key:value**2 for key,value in simple_dict.items()}
my_dict2 = { key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict3 = {i:i*2 for i in [3,2,4]}

print (my_dict)
print (my_dict2)
print (my_dict3)

