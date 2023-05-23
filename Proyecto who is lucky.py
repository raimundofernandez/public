import random

print("Enter the number of friends joining (including you):")
guests = int(input())
guests_dictionary = {}

if guests <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(guests):
        guest_name = input()
        guests_dictionary[guest_name] = 0
    print("Enter the total bill value:")
    total_bill = float(input())
    lucky_guest = random.choice(list(guests_dictionary.keys()))
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if input() == "Yes":
        print(f"{lucky_guest} is the lucky one!")
        individual_bill = total_bill/(guests - 1)
        for guest in guests_dictionary:
            if guest != lucky_guest:
                guests_dictionary[guest] = round(individual_bill, 2)
            else:
                guests_dictionary[guest] = 0

    else:
        print("No one is going to be lucky")
        individual_bill = total_bill / guests
        for guest in guests_dictionary:
            guests_dictionary[guest] = round(individual_bill, 2)

    print(guests_dictionary)
