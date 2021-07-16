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

    input_amount = InputPreprocess(user_input)    

    if isinstance(input_amount, int):
        input_flag = 0

    else:
        print("\n === Invalid Input === \n")
        input_flag = 1


print("\nTotal in pence: ", input_amount)


# ==== Least Amount of Coins Calculation ====
# Allowed coins 200, 100, 50, 20, 10, 5, 2, 1
# All coins stored in a dictionary
no_of_coins = {
    "200": 0, 
    "100": 0,
    "50": 0,
    "20": 0,
    "10": 0,
    "5": 0,
    "2": 0,
    "1": 0,
}

# Finding the least amount of coins equivalent to input_amount
while input_amount != 0:

    for key in no_of_coins:
 
        if input_amount >= int(key):
            input_amount -= int(key)
            no_of_coins[key] += 1
            break
    
# Displaying all the amount of coins equivalent to input_amount
print("\nEquivalent in coins: ")
for key in no_of_coins:
    if no_of_coins[key] == 0:
        pass
    else:
        if key == "200":
            print('£2 x ', no_of_coins[key])

        elif key == '100':
            print('£1 x ', no_of_coins[key])

        else:
            print('{}p x {}'.format(key, no_of_coins[key]))