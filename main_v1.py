#--- Group 7: Fitness Tracker ---#

#--- Imports ---#
import sys

#--- Modules ---#
def check_for_users():
    global names_of_users
    try:
        with open("names_of_users.txt") as names:
            for name in names:
                names_of_users.append(name)
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

#--- Main ---#

names_of_users=[]

print("Hello & welcome to Fitness Tracker")

user_exists=check_for_users()
if user_exists:
    x=1
    print("\n")
    print("The following users were found. Enter the number of the user you wish to access information about.")
    for name in names_of_users:
        print(str(x)+" "+name.strip()+"\n")
        x+=1
    user_choice=validated_choice(">",[_ for _ in range(1,x)])
    print()
    print(f"Currently selected user: {names_of_users[user_choice-1]}.")
    file_name=str(user_choice)+".txt"
    with open(file_name) as user_file:
        user_data=user_file.readlines()
        mass=user_data[0]
        height=user_data[1]
        age=user_data[2]
        gender=user_data[3]
        activity_level=user_data[4]
        print("Data loaded successfully.")
        to_do_choice=validated_choice("Press 1 to Display current profile, 2 to Edit current profile, 3 to Remove current profile & 4 to exit. >",[1,2,3,4])
        match to_do_choice:
            case 1:
                print(f"Mass: {mass}")
                print(f"Height: {height}")
                print(f"Age: {age}")
                print(f"Gender: {gender}")
                print(f"Activity Level: {activity_level}")
            case 4:
                sys.exit("Goodbye")
else:
    choice=validated_choice("No users found. Enter 1 to create new user, 0 to exit. >",[0,1])
    if choice==1:
        print("Good scene so far")

sys.exit("Goodbye!")
    