# Modules and getting stuff running
import math
import time


# Title
title = input('What do you call this trip? ')
name = input('What is your name? ')
title = "              " + name +"\'s " + title
TITLE = title.upper()


# Passengers
passengers = int(input('How many more people are coming with you? '))


# Luggage counter
luggage = input('What are you bringing? (separate items with commas) ')
commas = ','
luggages = luggage.count(commas)


# Destination list
start = ['EVCC', 0]
dest1 = ['Seattle Childrens Museum', 110.5]
dest2 = ['Ellensburg Comic Shop', 122.3]
dest3 = ['Grand Coulee Dam Light Show', 98.7]
dest4 = ['Winthrop', 159.9]


# Gas prices and Mileage
mileage = float(input('Do you know your miles per gallon? (if not, please type "26" because I don\'t know how to use if/else statements yet.) '))
gasprice = float(input('How much is gas? $'))
placelist = [dest1, dest2, dest3, dest4]
totalmiles = dest1[1] + dest2[1] + dest3[1] + dest4[1]
gascost = (totalmiles / mileage)* gasprice


# Makes it look like its thinking about it...
print('Calculating.')
time.sleep(1)
print('Calculating..')
time.sleep(1)
print('Calculating...')
time.sleep(1)


# Final Output
print(' \n \n \n \n             ')
print('\033[1m' + TITLE + '\033[0m')
print(f'You need {passengers + 1} seats, including the drivers.')
print(f'The amount of luggage you need to pack is {luggages + 1}')
print(f'Your first stop is {dest1[0]}, and your last stop is {dest4[0]}.')
print(f'Your total distance is {totalmiles} miles')
print(f'You will need {totalmiles / mileage} gallons of gasoline.\nIt will cost you roughly ${gascost:.4}')
print(f'\n{dest1[0]} -> {dest2[0]} -> {dest3[0]} -> {dest4[0]}')
