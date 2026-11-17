\# Fitness Tracker

\*\*INT2067 Introduction to Programming and Problem Solving — Group Project\*\*

Group 7  
\---

\#\# 1\. About the program

Our project is an application that helps users in calculating their daily requirements  
for calories, protein, carbohydrates and fats. Our program performs these  
calculations automatically depending on an individual's weight, height, age, gender  
and activity level because doing them by hand can be hard and time consuming. It  
functions similarly to a basic user manager. You can add new users, search them,  
change their information or remove them. The program instantly recalculates the  
user's stats if their weight or aim like gaining, losing or maintaining weight  
changes.  
Our program includes basic checks to make sure bad inputs don't crash the app. All  
user information is saved right in the computer's memory while the program is  
running using standard lists and dictionaries. Overall, the project combines easy  
math formulas with a clean menu so users can manage health profiles straight from  
the terminal

\#\# 2\. Requirements

\- Python \*\*3.10 or newer\*\* (the program uses \`match / case\`)  
\- No external libraries

\#\# 3\. Files

\| File \| Description \|  
\|---\|---\|  
\| \`project.py\` \| Source code \|  
\| \`users.txt\` \| Saved profiles. Created automatically when the first user is added \|  
\| \`README.md\` \| Instructions and test cases \|

Format of one line in \`users.txt\`:

\`\`\`  
name,mass,height,age,gender,activity\_level,weight\_goal  
eliza,60,165,20,female,active,lose  
\`\`\`

\#\# 4\. How to run

Open a terminal in the folder with \`project.py\` and run:

\`\`\`  
python project.py  
\`\`\`

(On macOS / Linux: \`python3 project.py\`.)

\#\# 5\. How to use

\- Type the \*\*number\*\* of an option and press Enter.  
\- Type \*\*-1 in any prompt\*\* to exit the program.

\*\*Start screen.\*\* If there are no users:

\`\`\`  
No users found. Enter 1 to create a new user. Enter \-1 to exit. \>  
\`\`\`

If users exist, the program shows the list:

\`\`\`  
The following users exist:  
1\. Bektur  
2\. Abdullah  
Enter the number of the user whose profile to access. Enter 0 to add a new user (or \-1 to exit). \>  
\`\`\`

\*\*Profile menu\*\* (after choosing a user):

\| Option \| Action \|  
\|---\|---\|  
\| 1 \| Display current profile data and daily requirements \|  
\| 2 \| Alter current profile data \|  
\| 3 \| Remove current profile (asks for confirmation first) \|  
\| 4 \| Return to user list \|

\*\*Altering a profile.\*\* The program shows every field with its current value:

\`\`\`  
Altering data for: Kamila  
1\. Name: Kamila  
2\. Mass (kg): 60  
3\. Height (cm): 165  
4\. Age (years): 20  
5\. Gender: Female  
6\. Activity level: Active  
7\. Weight goal: Lose  
0\. Finish editing  
\`\`\`

Choose a field, enter the new value, and repeat for other fields. Choose \`0\` to finish.  
If something was changed, the profile is saved and the new results are displayed.

\*\*Removing a profile.\*\* The program asks:

\`\`\`  
Are you sure you want to delete this profile? This action cannot be undone.  
Enter 1 to confirm deletion, 2 to cancel \>  
\`\`\`

\#\# 6\. Input rules

\| Field \| Allowed values \| Error message \|  
\|---\|---\|---\|  
\| Name \| Not empty, up to 20 characters, no commas, not already used \| \`Error: Please do not leave name field empty\` / \`Error: Name is too long; please use 1-20 characters\` / \`Error: Name cannot contain a comma\` / \`Error: User already exists. Please try another name\` \|  
\| Mass \| Whole number 20–300 (kg) \| \`Please enter a whole number\` / \`Please enter a number between 20 and 300\` \|  
\| Height \| Whole number 100–250 (cm) \| \`Please enter a whole number\` / \`Please enter a number between 100 and 250\` \|  
\| Age \| Whole number 10–100 (years) \| \`Please enter a whole number\` / \`Please enter a number between 10 and 100\` \|  
\| Gender \| \`male\` / \`female\` \| \`Please enter one of: male, female\` \|  
\| Activity level \| \`sedentary\` / \`moderate\` / \`active\` \| \`Please enter one of: sedentary, moderate, active\` \|  
\| Weight goal \| \`maintain\` / \`lose\` / \`gain\` \| \`Please enter one of: maintain, lose, gain\` \|  
\| Menu choice \| One of the listed numbers \| \`Error: Please enter only numbers\` / \`Error: Please input a number from the available choices\` \|

Names and text answers are not case-sensitive (they are converted to lower case).  
After an error the program asks again instead of crashing.

\#\# 7\. Calculations

\| Value \| Formula \|  
\|---\|---\|  
\| BMR (Mifflin–St Jeor) \| \`10 × mass \+ 6.25 × height − 5 × age\`, then \*\*+5\*\* for male or \*\*−161\*\* for female \|  
\| TDEE \| \`BMR × activity factor\` — sedentary 1.2, moderate 1.55, active 1.725 \|  
\| Target calories \| \`TDEE \+ 0\` (maintain), \`TDEE − 500\` (mass loss), \`TDEE \+ 300\` (mass gain). All three are displayed \|  
\| Protein \| \`2 g × mass\`; 4 kcal per gram \|  
\| Fat \| 25% of the target calories for the user's goal; 9 kcal per gram \|  
\| Carbohydrates \| The remaining calories; 4 kcal per gram \|

\#\# 8\. Programming techniques used

\| Technique \| Where in the code \|  
\|---\|---\|  
\| Classes and objects \| \`User\` stores one user's data and does the calculations; \`GetUserStats\` groups the input methods; \`ExitProgram\` is a custom exception \|  
\| Functions (modularisation) \| \`get\_input\`, \`get\_number\`, \`get\_option\`, \`check\_name\`, \`get\_user\_stats\`, \`create\_new\_user\`, \`alter\_profile\_data\`, \`show\_report\`, \`delete\_profile\`, \`profile\_menu\`, \`load\_all\_users\`, \`save\_all\_users\` \|  
\| Lists \| The list of \`User\` objects; lists of allowed choices \|  
\| Dictionaries \| \`GENDER\_OFFSET\`, \`ACTIVITY\_FACTORS\`, \`CALORIE\_CHANGE\` \|  
\| Strings \| \`.strip()\`, \`.lower()\`, \`.capitalize()\`, \`.split(",")\`, \`.join()\`, f-strings \|  
\| Selection \| \`if / elif / else\`, \`match / case\` \|  
\| Iteration \| \`while\` loops for menus and input checking; \`for\` loops for the user list and the file \|  
\| File operations \| \`load\_all\_users\` reads \`users.txt\`; \`save\_all\_users\` writes it \|  
\| Error handling \| \`try / except\` for \`ValueError\`, \`FileNotFoundError\` and \`ExitProgram\` \|

\#\# 9\. Test cases

Start each test \*\*without a \`users.txt\` file\*\*, unless the test says otherwise.

\#\#\# Test 1 — Create a new user

\| Step \| Input \| Expected output \|  
\|---\|---\|---\|  
\| 1 \| Start the program \| \`No users found. Enter 1 to create a new user. Enter \-1 to exit. \>\` \|  
\| 2 \| \`1\` \| \`Creating a new user\` \|  
\| 3 \| \`Kamila\`, \`60\`, \`165\`, \`20\`, \`female\`, \`active\`, \`lose\` \| \`New user created successfully\` \|  
\| 4 \| — \| The list shows \`1. Kamila\`. \`users.txt\` contains \`kamila,60,165,20,female,active,lose\` \|

\#\#\# Test 2 — Display daily requirements

Uses the user from Test 1\.

\| Step \| Input \| Expected output \|  
\|---\|---\|---\|  
\| 1 \| \`1\` (Kamila) \| \`Profile loaded successfully\` / \`Currently loaded profile: Kamila\` \|  
\| 2 \| \`1\` (display) \| Profile data, then the results below \|

\`\`\`  
Basal Metabolic Rate (BMR, cal/day): 1370.25  
Total Daily Energy Expenditure (cal/day): 2363.7  
Target Calories (cal/day): 2363.7 to maintain,  
1863.7 for mass loss,  
2663.7 for mass gain  
Protein (grams): 120  
Protein (calories): 480  
Fat (calories): 465.9  
Fat (grams): 51.8  
Carb (calories): 917.8  
Carb (grams): 229.4  
\`\`\`

\#\#\# Test 3 — Invalid input when creating a user

Uses \`users.txt\` from Test 1 (Kamila exists). Enter \`0\` to add a new user, then:

\| Input \| Expected output \|  
\|---\|---\|  
\| Name: (press Enter) \| \`Error: Please do not leave name field empty\` \|  
\| Name: \`,\` \| \`Error: Name cannot contain a comma\` \|  
\| Name: \`kamila\` \| \`Error: User already exists. Please try another name\` \|  
\| Name: \`Bektur\` \| Accepted \|  
\| Mass: \`abc\` \| \`Please enter a whole number\` \|  
\| Mass: \`10\` \| \`Please enter a number between 20 and 300\` \|  
\| Mass: \`80\`, Height: \`180\`, Age: \`25\` \| Accepted \|  
\| Gender: \`man\` \| \`Please enter one of: male, female\` \|  
\| Gender: \`male\` \| Accepted \|  
\| Activity level: \`fast\` \| \`Please enter one of: sedentary, moderate, active\` \|  
\| Activity level: \`active\` \| Accepted \|  
\| Weight goal: \`keep\` \| \`Please enter one of: maintain, lose, gain\` \|  
\| Weight goal: \`gain\` \| \`New user created successfully\` \|

The program asks again after every error and does not crash.

\#\#\# Test 4 — Invalid menu choice

\| Input \| Expected output \|  
\|---\|---\|  
\| \`x\` \| \`Error: Please enter only numbers\` \|  
\| \`9\` \| \`Error: Please input a number from the available choices\` \|

\#\#\# Test 5 — Alter a profile and recalculate

Uses Kamila from Test 1\.

\| Step \| Input \| Expected output \|  
\|---\|---\|---\|  
\| 1 \| \`1\` (Kamila), \`2\` (alter) \| The edit menu with all current values \|  
\| 2 \| \`2\` (mass), \`65\` \| \`Changed 60 to 65\` \|  
\| 3 \| \`7\` (weight goal), \`maintain\` \| \`Changed lose to maintain\` \|  
\| 4 \| \`2\` (mass), \`65\` \| \`Your value is the same as before, no changes made\` \|  
\| 5 \| \`0\` \| \`Profile altered successfully\`, then the recalculated results, including \`Target Calories (cal/day): 2449.9 to maintain\` \|  
\| 6 \| — \| \`users.txt\` contains \`kamila,65,165,20,female,active,maintain\` \|

\#\#\# Test 6 — Alter the name

Two users exist: Kamila and Bektur. Open Kamila, choose \`2\` (alter), then \`1\` (name).

\| Input \| Expected output \|  
\|---\|---\|  
\| \`bektur\` \| \`Error: User already exists. Please try another name\` \|  
\| \`kamila\` (her own name) \| \`Your value is the same as before, no changes made\` \|

\#\#\# Test 7 — Finish without changes

\| Input \| Expected output \|  
\|---\|---\|  
\| Open a user, \`2\` (alter), \`0\` \| \`No changes were made\` \|

\#\#\# Test 8 — Remove a profile (cancel and confirm)

Two users exist: Kamila and Bektur.

\| Step \| Input \| Expected output \|  
\|---\|---\|---\|  
\| 1 \| \`2\` (Bektur), \`3\` (remove) \| \`Are you sure you want to delete this profile? This action cannot be undone.\` \|  
\| 2 \| \`2\` (cancel) \| \`Deletion cancelled\`, then back to the user list. Bektur is still in the list \|  
\| 3 \| \`2\` (Bektur), \`3\` (remove), \`1\` (confirm) \| \`Profile removed successfully.\` \|  
\| 4 \| — \| The list shows only \`1. Kamila\`. Bektur is removed from \`users.txt\` \|

\#\#\# Test 9 — Data is kept between runs

\| Step \| Input \| Expected output \|  
\|---\|---\|---\|  
\| 1 \| Create a user, then \`-1\` \| \`Exiting program, goodbye\!\` \|  
\| 2 \| Start the program again \| The user is still in the list \|

\#\#\# Test 10 — Exit at any time

\| Input \| Expected output \|  
\|---\|---\|  
\| \`-1\` in any prompt (for example, while entering mass) \| \`Exiting program, goodbye\!\` \|

\#\# 10\. Sample session

\`\`\`  
Welcome to Fitness Tracker\!  
No users found. Enter 1 to create a new user. Enter \-1 to exit. \>1  
Creating a new user  
Enter user's name \>Kamila  
Enter user's mass (kg, 20-300) \>60  
Enter user's height (cm, 100-250) \>165  
Enter user's age (years, 10-100) \>20  
Please enter gender \[male/female\] \>female  
Please enter activity level \[sedentary/moderate/active\] \>active  
Please enter weight goal \[maintain/lose/gain\] \>lose  
New user created successfully

The following users exist:  
1\. Kamila  
Enter the number of the user whose profile to access. Enter 0 to add a new user (or \-1 to exit). \>-1

Exiting program, goodbye\!  
\`\`\`

\#\# 11\. Known limitations

\- If \`users.txt\` is edited by hand and a line has the wrong format, the program stops with an error when it starts.  
\- There is no minimum calorie limit, so the mass-loss target can be very low for small or elderly users.  
\- Mass, height and age must be whole numbers.  
\- Altering a profile and then exiting with \`-1\` before choosing \`0\` does not save the changes.

\#\# 12\. Acknowledgement

We used AI tools (Claude) in working on this project. The AI helped us with the structure  
of this README file and gave us hints and suggestions for improving the code, such as input  
checking and editing a profile one field at a time. All suggestions were reviewed, tested and  
written into the program by our group.