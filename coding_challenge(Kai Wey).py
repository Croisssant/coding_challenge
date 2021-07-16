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








