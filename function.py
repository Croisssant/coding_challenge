def InputPreprocess(user_input):
     # All inputs with only "p" goes here
    if (user_input.find("£") == -1 and user_input.find("p") != -1):

        user_input = user_input.replace("p", "")
    
        try:
            # For inputs with decimal points
            if user_input.find(".") != -1:
                input_amount = int(round(float(user_input), 2) * 100)

            else:
                input_amount = int(user_input)

        except ValueError:
            input_amount = "This is an invalid input"

    # All inputs with "£" or ("£" and "p") goes here
    else:
        
        user_input = user_input.replace("p", "")
    
        try:
            # For inputs with decimal points
            if user_input.find(".") != -1:
                user_input = user_input.replace("£", "")
                input_amount = int(round(float(user_input), 2) * 100)
            
            # For inputs with NO decimal points
            else:            
                # If "£" is found multiply by 100
                if user_input.find("£") != -1:
                    user_input = user_input.replace("£", "")
                    input_amount = int(user_input) * 100
                
                # Retain original value if no "£"    
                else:
                    input_amount = int(user_input)

        except ValueError:
            input_amount = "This is an invalid input"
    
    return input_amount