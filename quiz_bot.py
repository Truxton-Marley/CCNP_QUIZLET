import sys
from questions_first_draft import questions

print("Hello Truxton!\n\n")
print("Would you like to study for your CCNP exam? Type '[y]es' or 'exit'\n\n")

####

def getLine(line):
    user_line = raw_input(line["level"])
    answer_line = line["answer"]

    correct = (user_line == answer_line)

    if correct:
        pass
    elif user_line.lower == "quit":
        sys.exit()
    elif user_line.lower().strip() == "hint":
        print(line['hint'])
        getLine(line)
    else:
        print("NOPE. KEEP TRYING")
        print("The correct answser was: " + answer_line)
        getLine(line)


def get_answer(question):

    print("R1(config)#\n"*2+"R1(config)#")
    answer_lines = question["answer_lines"]
    for line in answer_lines:
        getLine(line)
    print("\n\nGood Job!!!")
    
def ask_question(question):
    print(question["question"])
    get_answer(question)

###

for question in questions:
    ask_question(question)
    print("NEXT QUESTION.\n\n\n\n\n")
print("Looks like that's all for now!!!")