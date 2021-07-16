# ================= CODING CHALLENGE =================
# Problem: Given number of pennies return the minimum number of Sterling coins in the equivalent amount

from function import InputPreprocess

# ==== Input Preprocessing ====
print("===========================\n")
print("Pound to Pence Converter\n")
print("===========================\n")
input_flag = 1

while input_flag == 1:
    print("Please insert the amount")
    user_input = input(">>> ")
    input_amount, input_flag = InputPreprocess(user_input, input_flag)        

print("\nTotal in pence: ", input_amount)


# ==== Least Amount of Coins Calculation ====
# Allowed coins 200, 100, 50, 20, 10, 5, 2, 1
# All coins stored in a dictionary
no_of_coins = {
    "£2": 0, 
    "£1": 0,
    "50p": 0,
    "20p": 0,
    "10p": 0,
    "5p": 0,
    "2p": 0,
    "1p": 0,
}

# Finding the least amount of coins equivalent to input_amount
while input_amount != 0:
    if input_amount >= 200:
        input_amount -= 200
        no_of_coins["£2"] += 1

    elif input_amount >= 100:
        input_amount -= 100
        no_of_coins["£1"] += 1

    elif input_amount >= 50:
        input_amount -= 50
        no_of_coins["50p"] += 1

    elif input_amount >= 20:
        input_amount -= 20
        no_of_coins["20p"] += 1

    elif input_amount >= 10:
        input_amount -= 10
        no_of_coins["10p"] += 1

    elif input_amount >= 5:
        input_amount -= 5
        no_of_coins["5p"] += 1

    elif input_amount >= 2:
        input_amount -= 2
        no_of_coins["2p"] += 1

    elif input_amount >= 1:
        input_amount -= 1
        no_of_coins["1p"] += 1


# Displaying all the amount of coins equivalent to input_amount
print("\nEquivalent in coins: ")
for key in no_of_coins:
    if no_of_coins[key] == 0:
        pass
    else:
        print(key, 'x', no_of_coins[key])






