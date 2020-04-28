with open("myfile.txt") as file:
    data = file.read()
    data = data.split('\n')

    finished_config = ""

    print("""
import config_levels as cli
    """)

    print("questions = [")

    sample = ""
    for line in data:
        if line.startswith("!"):
            pass
        else:
            if line.startswith("  "):
                print("\t\t{")
                print('\t\t"answer": "' + line.strip() + '",')
                print('\t\t"indention": "2",')
                print('\t\t"level": cli.CONFIG,')
                print('\t\t"hint": "' + line.strip() + '",')
                sample += line
                sample += "\n"
            elif line.startswith(" "):
                print("\t\t{")
                print('\t\t"answer": "' + line.strip() + '",')
                print('\t\t"indention": "1",')
                print('\t\t"level": cli.CONFIG,')
                print('\t\t"hint": "' + line.strip() + '",')
                print('\t\t},')
                sample += line
                sample += "\n"
            else:
                if sample != "":
                    print('\t],')
                    print('\n\t"sample":\n"""\n' + sample + '""",')
                    print('\t},')
                questions_header = '\t{\n'
                questions_header += '\t"question": "' + 'How do you configure ' + line + '",\n\n'
                questions_header += '\t"about": "' + line + '",\n'
                print(questions_header)
                print('\t"answer_lines": [')
                print("\t\t{")
                print('\t\t"answer": "' + line.strip() + '",')
                print('\t\t"indention": "0",')
                print('\t\t"level": cli.CONFIG,')
                print('\t\t"hint": "' + line.strip() + '",')
                print('\t\t},')
                sample = ""
                sample += line
                sample += "\n"
    print('\t],')
    print('\n\t"sample":\n"""\n' + sample + '""",')
    print('\t},')

    print(']')
