# Program #3: Capital quiz, Griffin Corniea, 10/21/25

import random

states_capitals = {
    'Alabama': 'montgomery',
    'Alaska': 'juneau',
    'Arizona': 'phoenix',
    'Arkansas': 'little rock',
    'California': 'sacramento',
    'Colorado': 'denver',
    'Connecticut': 'hartford',
    'Delaware': 'dover',
    'Florida': 'tallahassee',
    'Georgia': 'atlanta',
    'Hawaii': 'honolulu',
    'Idaho': 'boise',
    'Illinois': 'springfield',
    'Indiana': 'indianapolis',
    'Iowa': 'des moines',
    'Kansas': 'topeka',
    'Kentucky': 'frankfort',
    'Louisiana': 'baton rouge',
    'Maine': 'augusta',
    'Maryland': 'annapolis',
    'Massachusetts': 'boston',
    'Michigan': 'lansing',
    'Minnesota': 'saint paul',
    'Mississippi': 'jackson',
    'Missouri': 'jefferson city',
    'Montana': 'helena',
    'Nebraska': 'lincoln',
    'Nevada': 'carson city',
    'New Hampshire': 'concord',
    'New Jersey': 'trenton',
    'New Mexico': 'santa fe',
    'New York': 'albany',
    'North Carolina': 'raleigh',
    'North Dakota': 'bismarck',
    'Ohio': 'columbus',
    'Oklahoma': 'oklahoma city',
    'Oregon': 'salem',
    'Pennsylvania': 'harrisburg',
    'Rhode Island': 'providence',
    'South Carolina': 'columbia',
    'South Dakota': 'pierre',
    'Tennessee': 'nashville',
    'Texas': 'austin',
    'Utah': 'salt lake city',
    'Vermont': 'montpelier',
    'Virginia': 'richmond',
    'Washington': 'olympia',
    'West Virginia': 'charleston',
    'Wisconsin': 'madison',
    'Wyoming': 'cheyenne'
}




correct = 0
incorrect = 0

for i in range(5):
    state = random.choice(list(states_capitals.keys()))
    answer = input("What is the capital of {state}? ").lower()

    if answer == states_capitals[state]:
        print("Correct")
        correct += 1
    else:
        print("Wrong, The correct a answer is: {states_capitals[state]}")
        incorrect += 1

print(f"\nYou got {correct} correct and {incorrect} incorrect.")