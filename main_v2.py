#--- Group Project: Fitness Tracker ---#

#--- Declaration ---#

"""
This code is my own individual and original work with very limited AI assistant. For any
part of codes that are referenced to, supported by AI, acknowledgement will be specified
"""

#--- Imports ---#

import sys

#--- Modules ---#
def welcome():

    print("Welcome to Fitness Tracker")

def check_for_users():
    
    try:
        with open("users.txt") as file:
            pass
        return(True)
    
    except FileNotFoundError:
        return(False)

def validated_choice(prompt,acceptable_inputs):

    choice_valid=False
    
    while not choice_valid:
        
        try:
            choice=int(input(prompt))
            
            if choice not in acceptable_inputs:
                print("Error: Please input a number from the available choices")
            
            else:
                choice_valid=True
                return(choice)
        
        except ValueError:
            print("Error: Please enter only numbers")

def print_all_users():
    
    global all_users
    
    with open("users.txt") as file:
        
        all_data=file.readlines()
        
        for line in all_data:
            name,mass,height,age,gender,activity_level,weight_goal=line.split(",")
            activity_level.strip()
            weight_goal.strip()
            all_users.append(name)
    
    print("The following users exist:")
    
    x=1
    
    for name in all_users:
        print(str(x)+". "+name.capitalize())
        x+=1

def create_new_user():
    
    print("Creating a new user.")
    
    name=input("Enter new user's name >").strip().lower()
    
    mass,height,age,gender,activity_level,weight_goal=get_user_stats()
    
    new_user_data_line=name+","+str(mass)+","+str(height)+","+str(age)+","+gender+","+activity_level+","+weight_goal+"\n"
    
    with open("users.txt","a") as file:
        file.write(new_user_data_line)
    
    print("New user created successfully")

def get_user_stats():
    
    mass_valid=False
    
    while not mass_valid:
        
        mass=input("Enter user's mass (kg, whole number) >")
        
        try:
            if int(mass)>=0:
                mass_valid=True
            else:
                print("Please enter a mass >= 0 kg")
        
        except ValueError:
            print("Please enter whole number mass in kg")

    height_valid=False
    
    while not height_valid:
        
        height=input("Enter user's height (cm, whole number) >")
        
        try:
            if int(height)>=0:
                height_valid=True
            else:
                print("Please enter a height >= 0 cm")
        
        except ValueError:
            print("Please enter whole number height in cm")

    age_valid=False
    
    while not age_valid:
        
        age=input("Enter user's age (years, whole number) >")
        
        try:
            if int(age)>=0:
                age_valid=True
            else:
                print("Please enter an age >= 0 years")
        
        except ValueError:
            print("Please enter whole number age in years")

    gender_valid=False
    
    while not gender_valid:
        gender=input("Please enter gender [Male/Female] >").lower().strip()
        if gender not in ["male","female"]:
            print("Please enter either Male or Female")
        else:
            gender_valid=True

    activity_level_valid=False
    
    while not activity_level_valid:
        activity_level=input("Please enter activity level [Active/Moderate/Sedentary] >").lower().strip()
        if activity_level not in ["active","moderate","sedentary"]:
            print("Please enter an activity level that either Active, Moderate or Sedentary")
        else:
            activity_level_valid=True
    
    weight_goal_valid=False
    
    while not weight_goal_valid:
        weight_goal=input("Please input your weight goal [Maintain/Lose/Gain] >").lower().strip()
        if weight_goal not in ["maintain","lose","gain"]:
            print("Please enter a goal from one of the listed options")
        else:
            weight_goal_valid=True

    return(mass,height,age,gender,activity_level,weight_goal)

def load_user_profile(selected_user):
    
    with open("users.txt") as file:
        all_users=file.readlines()
        current_user=all_users[selected_user-1]
        name,mass,height,age,gender,activity_level,weight_goal=current_user.split(",")
        mass=int(mass)
        height=int(height)
        age=int(age)
    
    print("Profile loaded successfully.")
    
    return(name.capitalize(),mass,height,age,gender.capitalize(),activity_level.capitalize(),weight_goal.capitalize())

def print_profile(name,mass,height,age,gender,activity_level,weight_goal):
    
    print("Name:",name)
    print("Mass (kg):",mass)
    print("Height (cm):",height)
    print("Age (years):",age)
    print("Gender:",gender)
    print("Activity level:",activity_level)
    print("Weight goal:",weight_goal)

def alter_profile_data(selected_user):
    
    with open("users.txt") as file:
        all_data=file.readlines()
    
    current_user_data=all_data[selected_user-1]
    name,mass,height,age,gender,activity_level,weight_goal=current_user_data.split(",")
    
    print("Altering data for:",name.capitalize())
    
    name=input("Enter new profile name >").lower().strip()
    mass,height,age,gender,activity_level,weight_goal=get_user_stats()
    new_data_line=name+","+str(mass)+","+str(height)+","+str(age)+","+gender+","+activity_level+","+weight_goal+"\n"
    all_data[selected_user-1]=new_data_line
    
    with open("users.txt","w") as file:
        file.writelines(all_data)
    
    print("Profile altered successfully.")

def delete_profile(selected_user):
    
    with open("users.txt") as file:
        all_data=file.readlines()
    del all_data[selected_user-1]
    
    with open("users.txt","w") as file:
        file.writelines(all_data) 
    print("Profile removed successfully.")

def current_profile_data(name,mass,height,age,gender,activity_level,weight_goal):
    
    print_profile(name,mass,height,age,gender,activity_level.strip(),weight_goal.strip())
    
    bmr=print_bmr(gender.lower(),mass,height,age)
    
    tdee=print_tdee(bmr,activity_level.lower().strip())
    
    print_target_cal(tdee)
    
    print_macronutrient_breakdown(mass,tdee,weight_goal.strip().lower())

def print_bmr(gender,mass,height,age):
    
    if gender=="male":
        bmr=(10*mass)+(6.25*height)-(5*age)+5
    else:
        bmr=(10*mass)+(6.25*height)-(5*age)-161
    print("Basal Metabolic Rate (BMR, cal/day):",bmr)
    
    return(bmr)

def print_tdee(bmr,activity_level):
    
    if activity_level=="active":
        print("Total Daily Energy Expenditure (cal/day):",round(bmr*1.725,1))
        return(bmr*1.725)
    
    elif activity_level=="moderate":
        print("Total Daily Energy Expenditure (cal/day):",round(bmr*1.55,1))
        return(bmr*1.55)
    
    else:
        print("Total Daily Energy Expenditure (cal/day):",round(bmr*1.2,1))
        return(bmr*1.2)

def print_target_cal(tdee):
    
    print(f"Target Calories (cal/day): {round(tdee,1)} to maintain,\n{round(tdee-500,1)} for mass loss,\n{round(tdee+300,1)} for mass gain")

def print_macronutrient_breakdown(mass,tdee,weight_goal): #TDEE we get here is already based on weight loss goal
    
    if weight_goal=="maintain":
        target_cal=tdee
    
    if weight_goal=="lose":
        target_cal=tdee-500
    
    if weight_goal=="gain":
        target_cal=tdee+300
    
    protein_gsm=round(mass*2,1)
    protein_cal=round(protein_gsm*4,1)
    fat_cal=round(target_cal*0.25,1)
    fat_gsm=round(fat_cal/9,1)
    carb_cal=round(target_cal-(protein_cal+fat_cal),1)
    carb_gsm=round(carb_cal/4,1)
    
    print(f"Protein (grams): {protein_gsm}\nProtein (calories): {protein_cal}")
    
    print(f"Fat (calories): {fat_cal}\nFat (grams): {fat_gsm}")
    
    print(f"Carb (calories): {carb_cal}\nCarb (grams): {carb_gsm}")

def main_loop():

    while True:

        users_exist=check_for_users()

        if users_exist:

            global all_users
            all_users=[]

            print_all_users()

            selected_user=validated_choice("Enter the number of the user whose profile to access. Enter 0 to add a new user. >",[_ for _ in range(0,len(all_users)+1)])

            if selected_user==0:
                create_new_user()

            else:
                name,mass,height,age,gender,activity_level,weight_goal=load_user_profile(selected_user)
                print("Currently loaded profile:",name)

            loaded_profile_action=validated_choice("Enter 1 to display current profile data, 2 to alter current profile data, 3 to remove current profile, 4 to exit. >",[1,2,3,4])
        
            match loaded_profile_action:
            
                case 1:
                    current_profile_data(name,mass,height,age,gender,activity_level.strip(),weight_goal.strip())
            
                case 2:
                    alter_profile_data(selected_user)
            
                case 3:
                    delete_profile(selected_user)
            
                case 4:
                    sys.exit("Exiting program, goodbye!")

        else:

            _=validated_choice("No users found. Enter 1 to create a new user. Enter 0 to exit. >",[0,1])

            if _==1:
                create_new_user()
            else:
                sys.exit("Exiting program, goodbye!")

#--- Main ---#

all_users=[]

welcome()

main_loop()
