#1. A key that is not in the dictionary
prices = {'apple': 12, 'banana': 7, 'cherry': 25}
print(prices)

key = input("Which fruit? ")
try:
    print(prices[key])
except KeyError:
    print(f'{key} not exist, Goodbye')

# 2.Changing a tuple
t = (1, 2, 3)
try:
    t[0] = 99
except TypeError as e:
    print(t)

# 3. Removing something that is not in the list
fruits = ["apple", "banana"]
try:
    fruits.remove("orange")
except ValueError as e:
    print('orange is not in the list')

if "orange" in fruits:
    fruits.remove("orange")
else:
    print("orange is not in the list")