import random
import sys
from ios_devices import R1
from questions_first_draft import questions

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

def getLine(line):
    ###TODO: user may need to be propted for which command to enter at a given moment.
    ###create optional field in questions when extra instructions are needed and check
    ###to display here!
    user_line = raw_input(line["level"]["prompt"])
    answer_line = line["answer"]

    correct = (user_line == answer_line)

    if correct  == True:
        pass
    elif user_line.strip() == "":
        print(line["level"]["prompt"])
        getLine(line)
    elif user_line.strip() == "?":
        for option in line["level"]["options"]:
            print(option)
        getLine(line)
    elif user_line.lower().strip() == "quit":
        sys.exit()
    elif user_line.lower().strip() == "hint":
        print(line['hint'])
        getLine(line)
    elif user_line.lower().strip() == "sample":
        print(question['sample'])
        getLine(line)
    elif user_line.lower().strip() == "about":
        ###Some answer lines may have specific "about" info, check and see. If not, fall back on generic question-level 'about'
        if line.get('about'):
            print(line['about'])
        else:
            print(question['about'])
        getLine(line)
    elif ((user_line.lower().strip() == "show ip int br") | (user_line.lower().strip() == "show ip interface brief")):
        print(R1["show_ip_interface_brief"])
    else:
        print(discouragement[random.randint(0, len(discouragement)-1)])
        if (line.get('after_first_attempt')):
            print("THE CORRECT ANSWER IS:\n\n " + answer_line + "\n")
            print("YOUR WROTE:\n\n " + user_line + "\n")
        else:
            print(line['hint'] + "\n")
        line['after_first_attempt'] = 1
        getLine(line)


def get_answer(question):

    print("R1(config)#\n"*2+"R1(config)#")
    answer_lines = question["answer_lines"]
    ###TODO: ADD HINT COUNTER TO ENABLE USER TO CYCLES THROUGH MULTIPLE HINTS BEFORE GETTING ANSWER
    for line in answer_lines:
        getLine(line)
    print(encouragement[random.randint(0, len(encouragement)-1)])
    
def ask_question(question):
    print(question["question"])
    get_answer(question)

###

question_counter = 0
for question in questions:
    ask_question(question)
    question_counter += 1
    if question_counter < len(questions):
        print("         NEXT QUESTION:\n\n\n")

print("Looks like that's all for now!!!")
print("You should be thinking about scheduling your exam soon:)")
