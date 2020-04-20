import random
import sys
from ios_devices import R1
from ike_v1_questions import questions as ike_v1_questions
from nat_questions import questions as nat_questions

###TODO: BUILD A ROUTER CLASS WITH INTERFACES THAT WILL GIVE EXAMPLES WITH SHOW COMMANDS
###SHOULD BE ABLE TO DO SOMETHING LIKE (r1.show_ip_eigrp_neighbors) and print to screen.
###TO GIVE A MORE REALISTIC FEEL. AT LEAST A (r1.show_ip_interface_brief). See if you can
###TRACK STATE FOR THE SHOW COMMANDS; Partially done :)

discouragement = ["Alas no.\n", "Not Quite.\n", "Schade.\n", "Scheiss.\n", "Tabernak!!!\n", "Don't give up!\n"]
encouragement = ["\n\nGood Job!!!\n", "\nWell done!\n", "\nAye, that's you.\n", "\nChapeau!\n"]

###TODO: ADD ABILITY TO EXIT HERE?
print("\n\nHello Dearest User!\n\n")
print("Are you ready to study for your CCNP exam!?!\n\n")
print("             REMEMBER TO TYPE:")
print("                               'sample' IF YOU WANT TO SEE THE WHOLE CONFIGURATION")
print("                               'about' FOR MORE INFORMATION")
print("                               'hint' FOR A HINT.")
print("             TYPE 'sample' IF YOU ARE COMPLETELY LOST")
print("     ")

###

###TODO: ADD LEARNING MODE WHERE SAMPLE IS DISPLAYED AUTOMATICALLY 
###TODO: ADD MASTER MODE WHERE ANSWER IS NOT SHOWN
###TODO: ADD SCORING FOR EACH LEVEL FOR A GIVEN USER AND TRACK

###TODO: CREATE A USER CLASS
###TODO: BIND USER CLASS TO SQL MODEL/DATABASE


def get_line(line, attempts):
    ###TODO: user may need to be propted for which command to enter at a given moment.
    ###create optional field in questions when extra instructions are needed and check
    ###to display here!
    user_line = input(line["level"]["prompt"])
    answer_line = line["answer"]

    correct = (user_line == answer_line)

    if correct  == True:
        return 1
    elif user_line.strip() == "":
        print(line["level"]["prompt"])

    elif user_line.strip() == "?":
        for option in line["level"]["options"]:
            print(option)

    elif user_line.lower().strip() == "quit":
        sys.exit()
    elif user_line.lower().strip() == "hint":
        print(line['hint'])

    elif user_line.lower().strip() == "sample":
        print(question['sample'])

    elif user_line.lower().strip() == "about":
        ###Some answer lines may have specific "about" info, check and see. If not, fall back on generic question-level 'about'
        if line.get('about'):
            print(line['about'])
        else:
            print(question['about'])

    elif ((user_line.lower().strip() == "show ip int br") | (user_line.lower().strip() == "show ip interface brief")):
        print(R1["show_ip_interface_brief"])
    ###TODO: BROKE WHEN REFACTORING RECURSIVE FUNCTION TO NON-RECURSIVE; FIX
    else:
        print(discouragement[random.randint(0, len(discouragement)-1)])
        if (attempts > 0):
            print("THE CORRECT ANSWER IS:\n\n " + answer_line + "\n")
            print("YOUR WROTE:\n\n " + user_line + "\n")
        else:
            print(line['hint'] + "\n")



def get_answer(question):

    print("R1(config)#\n"*2+"R1(config)#")
    answer_lines = question["answer_lines"]
    ###TODO: ADD HINT COUNTER TO ENABLE USER TO CYCLES THROUGH MULTIPLE HINTS BEFORE GETTING ANSWER
    for line in answer_lines:
        solved = False
        attempts = 0
        while not solved:
            solved = get_line(line, attempts)
            attempts += 1
    print(encouragement[random.randint(0, len(encouragement)-1)])
    
def ask_question(question):
    print(question["question"])
    get_answer(question)

###

###TODO: MAKE SELECTION LESS FRAGILE

def get_choice():
    choice = input("What would you like to study today? Please enter a number.\n\t1)IKE\n\t2)NAT\n\t3)Exit\n>:")
    if choice == "1":
        questions = ike_v1_questions
    elif choice == "2":
        questions = nat_questions
    elif choice == "3":
        sys.exit()
    else:
        get_choice()
    return questions

questions = get_choice()

question_counter = 0
for question in questions:
    ask_question(question)
    question_counter += 1
    if question_counter < len(questions):
        print("         NEXT QUESTION:\n\n")

print("Looks like that's all for now!!!")
print("You should be thinking about scheduling your exam soon:)")