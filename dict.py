# # DON'T TOUCH PLEASE!
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# # DON'T TOUCH PLEASE!

# total_donations = 0

# for key,value in donations.items():
#     total_donations = total_donations + value
    
# print(total_donations)

# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# # YOUR CODE GOES BELOW:

# print(food)

# if bakery_stock.get(food) != None:
#     print(f'{bakery_stock.get(food)} left')
# else:
# 	print('We don\'t make that')


# # 	
# #DO NOT TOUCH game_properties!
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"] 

# # Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
# initial_game_state = {}.fromkeys(game_properties,0)

# print(initial_game_state)


# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# # Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

# stock_list = inventory.copy()

# print(inventory)


# # add the value 18 to stock_list under the key "cookie"

 
# stock_list.update({'cookie': 18})


# # remove 'cake' from stock_list USE A DICTIONARY METHOD

# stock_list.pop('cake')
# print(stock_list)

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[n]:list2[n] for n in range(0,len(list1))}

# # print(answer)
# # ======


# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# # use the person variable in your answer

# print(person[0][1])

# d = {person[0][0]:person[0][1]}

# print(d)

# answer = {}

# for x in range(0,len(person)):
# 	answer.update({person[x][0]:person[x][1]})
	
	

# # answer = 

# make sure your solution is assigned to the answer variable so the tests can work!
# answer = {k:0 for k in 'aeiou'}

# answer = dict.fromkeys("aeiou", '1') 

# answer = {x:chr(x) for x in range(65,91)}

# print(answer)



# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.

numbers = {1,2,3,4}

# 2 - Create a variable called value which is a tuple with the the value 1 inside.

value = {1}

# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple

static_values = tuple(values)
print(static_values)
# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list


