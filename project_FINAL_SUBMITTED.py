#--- Group Project: Fitness Tracker ---#

'''
This code is our own individual and original work with very limited AI assistant. For any
part of codes that are referenced to, supported by AI, acknowledgement will be specified
'''

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

class GetUserStats:
    @staticmethod
    def get_mass():
        return(get_number("Enter user's mass (kg, 20-300) >",20,300))

    @staticmethod
    def get_height():
        return(get_number("Enter user's height (cm, 100-250) >",100,250))

    @staticmethod
    def get_age():
        return(get_number("Enter user's age (years, 10-100) >",10,100))

    @staticmethod
    def get_gender():
        return(get_option("Please enter gender",list(GENDER_OFFSET)))

    @staticmethod
    def get_activity_level():
        return(get_option("Please enter activity level",list(ACTIVITY_FACTORS)))

    @staticmethod
    def get_weight_goal():
        return(get_option("Please enter weight goal",list(CALORIE_CHANGE)))


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

def check_name(users,current_name=""):
    while True:
        name=get_input("Enter user's name >").strip().lower()
        if name=="":
            print("Error: Please do not leave name field empty")
        elif len(name)<1 or len(name)>20:
             print("Error: Name is too long; please use 1-20 characters")
        elif "," in name:
            print("Error: Name cannot contain a comma")
        elif name!=current_name and any(user.name==name for user in users):
            print("Error: User already exists. Please try another name")
        else:
            return (name)

def create_new_user(users):
    print("Creating a new user")
    name=check_name(users)
    mass,height,age,gender,activity_level,weight_goal=get_user_stats()
    new_user=User(name,mass,height,age,gender,activity_level,weight_goal)
    users.append(new_user)
    save_all_users(users)
    print("New user created successfully")

def get_number(prompt, min_value, max_value):
    while True:
        value=get_input(prompt)
        try:
            value=int(value)
            if min_value<=value<=max_value:
                return(value)
            else:
                print(f"Please enter a number between {min_value} and {max_value}")
        except ValueError:
            print("Please enter a whole number")

def get_option(prompt, options):
    while True:
        answer=get_input(prompt+" ["+"/".join(options)+"] >").lower().strip()
        if answer in options:
            return(answer)
        else:
            print("Please enter one of: "+", ".join(options))

def get_user_stats():
    get_stats=GetUserStats()
    mass=get_stats.get_mass()
    height=get_stats.get_height()
    age=get_stats.get_age()
    gender=get_stats.get_gender()
    activity_level=get_stats.get_activity_level()
    weight_goal=get_stats.get_weight_goal()
    return(mass,height,age,gender,activity_level,weight_goal)

def alter_profile_data(users,selected_user):
    user=users[selected_user-1]
    changed=False
    get_stats=GetUserStats()
    while True:
        print("\nAltering data for:",user.name.capitalize())
        print("1. Name:",user.name.capitalize())
        print("2. Mass (kg):",user.mass)
        print("3. Height (cm):",user.height)
        print("4. Age (years):",user.age)
        print("5. Gender:",user.gender.capitalize())
        print("6. Activity level:",user.activity_level.capitalize())
        print("7. Weight goal:",user.weight_goal.capitalize())
        print("0. Finish editing")

        field_to_change=validated_choice("Enter the number of the field to change >",[0,1,2,3,4,5,6,7])
        if field_to_change==0:
            break
        elif field_to_change==1:
            old=user.name
            user.name=check_name(users, old)
            new=user.name
        elif field_to_change==2:
            old=user.mass
            user.mass=get_stats.get_mass()
            new=user.mass
        elif field_to_change==3:
            old=user.height
            user.height=get_stats.get_height()
            new=user.height
        elif field_to_change==4:
            old=user.age
            user.age=get_stats.get_age()
            new=user.age
        elif field_to_change==5:
            old=user.gender
            user.gender=get_stats.get_gender()
            new=user.gender
        elif field_to_change==6:
            old=user.activity_level
            user.activity_level=get_stats.get_activity_level()
            new=user.activity_level
        elif field_to_change==7:
            old=user.weight_goal
            user.weight_goal=get_stats.get_weight_goal()
            new=user.weight_goal

        if old==new:
            print("Your value is the same as before, no changes made")
        else:
            print(f"Changed {old} to {new}")
            changed=True
    if changed:
        save_all_users(users)
        print("Profile altered successfully")
        show_report(user)
    else:
        print("No changes were made")

def show_report(user):
    user.print_profile()
    bmr=user.print_bmr()
    tdee=user.print_tdee(bmr)
    user.print_target_cal(tdee)
    user.print_macronutrient_breakdown(tdee)

def delete_profile(users,selected_user):
    del(users[selected_user-1])
    save_all_users(users)
    print("Profile removed successfully.")

def profile_menu(users,selected_user):
    current_user=users[selected_user-1]
    print("Profile loaded successfully")
    print("Currently loaded profile:",current_user.name.capitalize())
    loaded_profile_action=validated_choice("Enter 1 to display current profile data, 2 to alter current profile data, 3 to remove current profile, 4 to return to user list. >",[1, 2, 3, 4])
    
    match loaded_profile_action: 
        case 1:
            show_report(current_user)   
        case 2:
            alter_profile_data(users,selected_user)   
        case 3:
            print("Are you sure you want to delete this profile? This action cannot be undone.")
            confirmation=validated_choice("Enter 1 to confirm deletion, 2 to cancel >",[1, 2])
            if confirmation==1:
                delete_profile(users,selected_user)
            else:
                print("Delete action cancelled")
        case 4:
            pass

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
                    profile_menu(users,selected_user)
            
            else:
                choice = validated_choice("No users found. Enter 1 to create a new user. Enter -1 to exit. >",[1])
                if choice == 1:
                    create_new_user(users)
                    
    
    except ExitProgram:
        print("\nExiting program, goodbye!")