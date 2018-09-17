# lista = [x for x in range(50) if x % 2 == 0]

# print(lista)


# def yell(stringy):
#     return f'{stringy}!'.upper()

# print(yell('HoLa'))


'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''


# def return_day(num = None):
# 	days = {1: "Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
# 	# print(days)
# 	# print(days.get(num, None))
#     return = days.get(num, None)

# return_day(1)
# return_day(2)
# return_day()

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

# def last_element(lista):
#     if lista == []
#     	return None
#     return lista[-1]


# def single_letter_count(string,l):
#     string = string.lower
#     l = l.lower
#     return 0 + string.count(l)


# single_letter_count('banana','a')


# print('banana'.count('a'))


'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
# def multiple_letter_count():
#     pass


string = [1, 2, 3]
# # answer = {x:string.count(x) for x in string}

# print(string)

# string.pop()

# print(string)


# string.pop(0)

# print(string)

# string.insert(0,20)

# print(string)


# string.append(30)

# print(string)


# def list_manipulation(lista,manip,be,v=0):
#     if manip == 'remove' and be == 'end':
#         return lista.pop()
#     if manip == 'remove' and be == 'beginning':
#         return lista.pop(0)
#     if manip == 'add' and be == 'end':
#         print('append')
#         print(lista)
#         lista.append(30)
#         print(lista2)
#         return lista2
#         # return lista.append(100)
#     if manip == 'add' and be == 'beginning':
#         print('insert')
#         return lista #.insert(0,100)

# print(list_manipulation([1,2,3], "remove", "end")) # 3
# print(list_manipulation([1,2,3], "remove", "beginning")) #  1
# print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
# print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]

# print('A ver Gaston'.lower().replace(' ',''))


# # lista = [1,2,3,4,5,6,7]
# # lista2 = lista[::-1]
# # print(lista2)


# '''
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('hannah') # True
# is_palindrome('robert') # False
# is_palindrome('amanaplanacanalpanama') # True
# '''

# def is_palindrome(string):
#     stripped = string.lower().replace(' ','')
#     lista = [x for x in stripped]
#     revlist = lista[::-1]
#     if lista == revlist:
#     	return True
#     return False

# is_palindrome('Hola Viteh')


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

# def frequency():
#     pass


# lista = [1,2,3,4,4,4]
# print(lista.count(4))

# lista2 = [True, False, True, True]
# print(lista2.count('carrot'))

# lista = [1,2,3,4,4,4]
# even = [x for x in lista if x % 2 == 0]
# result = 1
# for y in even:
# 	result = result * y
# return result
# print(even)


# lista = 'holaviteh'
# print(lista[:1:])


'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
# '''

# def compact(lista):
#     print(lista)
#     result = [x for x in lista if x == True]
#     print(result)
#     return result

# # print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]


# fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

# fish_list = [fish for fish in fish_tuple if fish != 'octopus']
# print(fish_list)

# # getting ['blowfish', 'clownfish', 'catfish']


# listin = [0,1,2,"",[], False, {}, None, "All done"]
# listin2 = [x for x in listin if x != None]
# print(listin2)
# for x in listin:
# 	print(type(x))

# # expecting [1,2, "All done"]
# getting [1]


'''
def isEven(num):
#     return num % 2 == 0

# partition([1,2,3,4], isEven) # [[2,4],[1,3]]
# '''
# def isEven(num):
#     return num % 2 == 0


# def partition(lista, funcion):
#     listaTruthy = []
#     listaFalsy = []
#     for item in lista:
#     	if funcion(item) is True:
#     		listaTruthy.append(item)
#     	else:
#     		listaFalsy.append(item)
#     return [listaTruthy,listaFalsy]

# print(partition([2,2,3,4], isEven)) # [[2,4],[1,3]]


# def combine_words(word,**presuf):
#     if 'prefix' in presuf.keys() and 'suffix' in presuf.keys():
#     	return presuf['prefix']+word+presuf['suffix']
#     elif 'suffix' in presuf.keys():
#     	return word+presuf['suffix']
#     elif 'prefix' in presuf.keys():
#     	return presuf['prefix']+word
#     return word


# combine_words('tu',suffix="vieja")


'''
# calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
# calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
# '''

# def calculate(make_float, operation,first,second,message='The result is'):
#     if operation == 'add':
#     	result = first + second
#     elif operation == 'substract':
#     	result = first - second
#     elif operation == 'multiply':
#     	result = first - second
#     else:
#     	result = first / second
#     if make_float:
#     	result = float(result)
#     else:
#     	result = int(result)
#     return message + ' ' + str(result)


# print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
# # print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"

# var1 = 'a'
# var2 = 2

# print(type(var1))
# print(type(var2))


# def extremes(l):
#     maxi = max(l)
#     print(maxi)
#     mini = min(l)
#     print(mini)
#     return (mini,maxi)
#     # return (min(l, key=lambda n : n in l),max(l, key=lambda n : n in l))

# print(extremes([1,2,3,4,5]))


'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0
# '''

# def sum_even_values(*nums):
# 	result = 0
# 	evens = ([num for num in nums if num % 2 == 0])
# 	for x in evens:
# 		result += x
# 	return result


# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0


'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

# def sum_floats(*args):
#     result = 0
#     for arg in args:
#     	if type(arg) == float:
#     		result += arg
#     return result


# print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
# print(sum_floats(1,2,3,4,5)) # 0

# def interleave(str1,str2):
# 	inter = list(zip(str1,str2))
# 	print(inter)
# 	resultado = ''
# 	for i in inter:
# 		for n in i:
# 			print(n)
# 			resultado += n
# 	print(resultado)

# 	# print(result)
# 	# "".join([i for i in inter])

# 	# result = ''.join(list(*zip(*str1,*lst2)))
# 	# return result

# interleave('tn','oi')
# # print(interleave('tn','oi'))


'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
# '''


# def triple_and_filter(lista):
#     return [x * 3 for x in list(filter(lambda x: x % 4 == 0, lista))]

# triple_and_filter([1, 2, 3, 4])  # [12]
# triple_and_filter([6, 8, 10, 12])  # [24,36]


'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''



names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']