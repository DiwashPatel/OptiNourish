def initialize():
    #total diseases whose prescriptions we have
    all_disease_list = ["Thyroid", "Diabetes", "Rheumatoid Arthritis", "Obesity"]

    #list of diseases user is suffering from
    disease_list = []


    print("Please enter")
    for i,disease in enumerate(all_disease_list):
        print(f"{i} for {disease}")


    user_input = input("Enter the disease(s) num (for eg:  1,2  or 0,1) ")
    indexes = user_input.split(",")

    for i in indexes:
        try:
            disease_list.append(all_disease_list[int(i)])
        except:
            print("Plase enter the index as specified.")
            return False
    print("Thank you! Please enter your food choices.")
    
    
    #total food choices allowed
    all_choices = ["Fruits", "Vegetables", "Nuts and Seeds", "Beans and Lentils", "Meats", "Fish"]

    #food choices the user selects
    food_choices =  []

    for i,food in enumerate(all_choices):
        print(f"{i} for {food}")

    user_inputs = input("Enter the food(s) num (for eg:  1,2  or 0,1) ")
    indexes = user_inputs.split(",")

    for i in indexes:
        try:
            food_choices.append(all_choices[int(i)])
        except:
            print("Plase enter the index as specified.")
            return False

    return (disease_list, food_choices)

