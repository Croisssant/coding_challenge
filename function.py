def InputPreprocess(user_input, input_flag):
     # All inputs with only "p" goes here
    if (user_input.find("£") == -1 and user_input.find("p") != -1):

        user_input = user_input.replace("p", "")
    
        try:

            if user_input.find(".") != -1:
                input_amount = int(round(float(user_input), 2) * 100)

            else:
                input_amount = int(user_input)
            
            input_flag = 0

        except ValueError:
            print("\n ===== This is an invalid input ===== \n")

    # All inputs with "£" or ("£" and "p") goes here
    else:
        
        user_input = user_input.replace("p", "")
    
        try:

            if user_input.find(".") != -1:
                user_input = user_input.replace("£", "")
                input_amount = int(round(float(user_input), 2) * 100)

            else:

                if user_input.find("£") != -1:
                    user_input = user_input.replace("£", "")
                    input_amount = int(user_input) * 100
                else:
                    input_amount = int(user_input)
            
            input_flag = 0

        except ValueError:
            print("\n ===== This is an invalid input ===== \n")
    
    return input_amount, input_flag