#--- Group Project: Fitness Tracker ---#

#--- Constants ---#

GENDER_OFFSET={
    "male":5,
    "female":-161}

ACTIVITY_FACTORS={
    "sedentary":1.2,
    "moderate":1.55,
    "active":1.725}

CALORIE_CHANGE={
    "maintain":0,
    "lose":-500,
    "gain":300}

#--- Exception(s) ---#

class ExitProgram(Exception):
    pass

#--- Class ---#

class User:
    def __init__(self,name,mass,height,age,gender,activity_level,weight_goal):
        self.name=name
        self.mass=int(mass)
        self.height=int(height)
        self.age=int(age)
        self.gender=gender
        self.activity_level=activity_level
        self.weight_goal=weight_goal

    def print_profile(self):
        print("Name:",self.name.capitalize())
        print("Mass (kg):",self.mass)
        print("Height (cm):",self.height)
        print("Age (years):",self.age)
        print("Gender:",self.gender.capitalize())
        print("Activity level:",self.activity_level.capitalize())
        print("Weight goal:",self.weight_goal.capitalize())

    def print_bmr(self):
        bmr=(10*self.mass)+(6.25*self.height)-(5*self.age)+GENDER_OFFSET[self.gender]
        print("Basal Metabolic Rate (BMR, cal/day):",bmr)
        return(bmr)

    def print_tdee(self,bmr):
        tdee=bmr*ACTIVITY_FACTORS[self.activity_level]
        print("Total Daily Energy Expenditure (cal/day):",round(tdee, 1))
        return(tdee)

    def print_target_cal(self,tdee):
        print(
            f"Target Calories (cal/day): {round(tdee+CALORIE_CHANGE['maintain'],1)} to maintain,\n"
            f"{round(tdee+CALORIE_CHANGE['lose'],1)} for mass loss,\n"
            f"{round(tdee+CALORIE_CHANGE['gain'],1)} for mass gain")

    def print_macronutrient_breakdown(self,tdee):
        target_cal=tdee+CALORIE_CHANGE[self.weight_goal]
        protein_gsm=round(self.mass*2,1)
        protein_cal=round(protein_gsm*4,1)
        fat_cal=round(target_cal*0.25,1)
        fat_gsm=round(fat_cal/9,1)
        carb_cal=round(target_cal-(protein_cal+fat_cal),1)
        carb_gsm=round(carb_cal/4,1)
        print(f"Protein (grams): {protein_gsm}\nProtein (calories): {protein_cal}")
        print(f"Fat (calories): {fat_cal}\nFat (grams): {fat_gsm}")
        print(f"Carb (calories): {carb_cal}\nCarb (grams): {carb_gsm}")

#--- Modules ---#

def welcome():
    print("Welcome to Fitness Tracker!")

def get_input(prompt):
    user_input=input(prompt)
    if user_input.strip()=="-1":
        raise ExitProgram()
    return(user_input)

def load_all_users():
    users=[]
    try:
        with open("users.txt") as file:
            for line in file:
                line=line.strip()
                if line:
                    name,mass,height,age,gender,activity_level,weight_goal=line.split(",")
                    users.append(User(name,int(mass),int(height),int(age),gender,activity_level,weight_goal))
    except FileNotFoundError:
        pass
    return(users)

def save_all_users(users):
    with open("users.txt","w") as file:
        for user in users:
            file.write(f"{user.name},{user.mass},{user.height},{user.age},{user.gender},{user.activity_level},{user.weight_goal}\n")

def validated_choice(prompt,acceptable_inputs):
    choice_valid=False
    while not choice_valid:
        try:
            choice=int(get_input(prompt))
            if choice not in acceptable_inputs:
                print("Error: Please input a number from the available choices")
            else:
                choice_valid=True
                return(choice)
        except ValueError:
            print("Error: Please enter only numbers")

def print_all_users(users):
    print("\nThe following users exist:")
    x = 1
    for user in users:
        print(str(x)+". "+user.name.capitalize())
        x+=1

def create_new_user(users):
    print("Creating a new user")

    name_valid = False
    while not name_valid:
        name=get_input("Enter new user's name >").strip().lower()
        if name=="":
            print("Error: Please do not leave name field empty")
        elif any(user.name==name for user in users):
            print("Error: User already exists. Please try another name")
        elif 1<=len(name)<=20:
            name_valid=True
        else:
            print("Error: Name is too short or too long; please revise so is 1-20 characters long")

    mass,height,age,gender,activity_level,weight_goal=get_user_stats()
    new_user=User(name,mass,height,age,gender,activity_level,weight_goal)
    users.append(new_user)
    save_all_users(users)
    print("New user created successfully")

def get_user_stats():
    mass_valid=False
    while not mass_valid:
        mass=get_input("Enter user's mass (kg, whole number) >")
        try:
            if 20<=int(mass)<=300:
                mass=int(mass)
                mass_valid=True
            else:
                print("Please enter a mass >= 20 & <= 300 kg")
        except ValueError:
            print("Please enter whole number mass in kg")

    height_valid=False
    while not height_valid:
        height=get_input("Enter user's height (cm, whole number) >")
        try:
            if 100<=int(height)<=250:
                height=int(height)
                height_valid=True
            else:
                print("Please enter a height >= 100 and <= 250 cm")
        except ValueError:
            print("Please enter whole number height in cm")

    age_valid=False
    while not age_valid:
        age=get_input("Enter user's age (years, whole number) >")
        try:
            if 10<=int(age)<= 100:
                age=int(age)
                age_valid=True
            else:
                print("Please enter an age >= 10 and <= 100 years")
        except ValueError:
            print("Please enter whole number age in years")

    gender_valid=False
    while not gender_valid:
        gender=get_input("Please enter gender [Male/Female] >").lower().strip()
        if gender not in ["male", "female"]:
            print("Please enter either Male or Female")
        else:
            gender_valid=True

    activity_level_valid=False
    while not activity_level_valid:
        activity_level=get_input("Please enter activity level [Active/Moderate/Sedentary] >").lower().strip()
        if activity_level not in ["active", "moderate", "sedentary"]:
            print("Please enter an activity level that either Active, Moderate or Sedentary")
        else:
            activity_level_valid=True

    weight_goal_valid=False
    while not weight_goal_valid:
        weight_goal=get_input("Please input your weight goal [Maintain/Lose/Gain] >").lower().strip()
        if weight_goal not in ["maintain", "lose", "gain"]:
            print("Please enter a goal from one of the listed options")
        else:
            weight_goal_valid=True

    return(mass,height,age,gender,activity_level,weight_goal)

def alter_profile_data(users,selected_user):
    user=users[selected_user-1]
    print("Altering data for:",user.name.capitalize())
    new_name=get_input("Enter new profile name >").lower().strip()
    mass,height,age,gender,activity_level,weight_goal=get_user_stats()
    user.name=new_name
    user.mass,user.height,user.age,user.gender,user.activity_level,user.weight_goal=(mass, height, age, gender, activity_level, weight_goal)
    save_all_users(users)
    print("Profile altered successfully")

def delete_profile(users,selected_user):
    del(users[selected_user-1])
    save_all_users(users)
    print("Profile removed successfully.")

#--- Main ---#

if __name__=="__main__":

    welcome()

    users = load_all_users()

    try:
        while True:
            if users:
                print_all_users(users)
                selected_user = validated_choice("Enter the number of the user whose profile to access. Enter 0 to add a new user (or -1 to exit). >",[_ for _ in range(0, len(users) + 1)])
                if selected_user==0:
                    create_new_user(users)
                else:
                    current_user=users[selected_user-1]
                    print("Profile loaded successfully")
                    print("Currently loaded profile:",current_user.name.capitalize())
                    loaded_profile_action=validated_choice("Enter 1 to display current profile data, 2 to alter current profile data, 3 to remove current profile, 4 to return to user list. >",[1, 2, 3, 4])
                    
                    match loaded_profile_action:
                        
                        case 1:
                            current_user.print_profile()
                            bmr=current_user.print_bmr()
                            tdee=current_user.print_tdee(bmr)
                            current_user.print_target_cal(tdee)
                            current_user.print_macronutrient_breakdown(tdee)
                        
                        case 2:
                            alter_profile_data(users,selected_user)
                        
                        case 3:
                            delete_profile(users,selected_user)
                        
                        case 4:
                            pass
            
            else:
                choice = validated_choice("No users found. Enter 1 to create a new user. Enter -1 to exit. >",[1])
                if choice == 1:
                    create_new_user(users)
    
    except ExitProgram:
        print("\nExiting program, goodbye!")
