import random

print("Enter the number of friends joining (including you):")

while True:
        try:
            num_friends = input()
            print()
        except:
            print("Invalid input, try again")
            continue
        else:
          break

party_dict = {}

if num_friends == '0' or int(num_friends) < 0:
    print("No one is joining for the party")
else:
    for i in range(int(num_friends)):
        if i == 0:
            print("\nEnter the name of every friend (including you), each on a new line:")
        party_dict[input()] = 0
        
    while True:
        try:
            totalbill = input('Enter the total bill value:')
            totalbill = int(totalbill)
        except:
            print("Invalid input, try again")
            continue
        else:
            break
    
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    luckyinput = input()

    luckyinput = luckyinput.capitalize()

    if luckyinput == 'Yes':
        luckywin = random.choice(list(party_dict.keys()))
        print(f"\n{luckywin} is the lucky one!")

        seperatebill = totalbill/(int(num_friends)-1)

        for key in party_dict:
            if key == luckywin:
                continue
            party_dict[key] = round(seperatebill, 2)
    
    else:
        print("No one is going to be lucky")
        seperatebill = totalbill/int(num_friends)
            
        for key in party_dict:
            party_dict[key] = round(seperatebill, 2)
            
    print()
    print(party_dict)