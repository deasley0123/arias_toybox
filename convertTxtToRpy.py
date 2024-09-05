def printRenPyLine(name, card):
    print(name[0] + " " + '"' + card + '"')

def read_file_line_by_line(file_path):
    unknownName = ("q", "???")
    narrator = ("n", "")

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Iterate over each line in the file
            name = unknownName
            card = ""
            isFirstLine = True
            options = 0
            choiceNum = 0
            endJump = ""

            for line in file:
                curLine = line.strip()
                # IF the current line is a dialogue tag Name, then...
                if curLine[0] == '#':
                    # Print out current RenPy line
                    if not isFirstLine:
                        printRenPyLine(name, card)
                    isFirstLine = False
                    # Strip off the leading character, trim whitespace
                    curLine = curLine.lstrip('#').strip()
                    
                    # Configure the new name
                    if curLine.isalnum() != True:
                        name = unknownName
                    elif curLine == "Narration":
                        name = narrator
                    else:
                        name = (curLine[0].lower(), curLine)
                    # print(name)
                    card = ""
                elif curLine[0] == '%':
                    printRenPyLine(name, card)
                    card = ""
                    splitTag = curLine.lstrip('%').strip().split("_")
                    if splitTag[0] == "options":
                        choiceNum = splitTag[1]
                        print("menu:")
                        options = options +1
                        endJump = "jump resume_"+splitTag[1]
                    else:
                        if splitTag[0] == "resume" or not splitTag[2] == 1:
                            print(endJump)
                        print("label "+curLine.lstrip('%')+":")
                elif options > 0:
                    print("    \""+curLine+"\":\n        jump choice_"+choiceNum+"_"+str(options))
                    options = options +1
                    if options > 2:
                        options = 0
                        choiceNum = 0
                # IF the current line is a part of the dialogue, then...
                else:
                    if card == "":
                        card = curLine.strip()
                    else:
                        card += "{p}" + curLine.strip()
                    # print(card)
            # Print out current RenPy line
            printRenPyLine(name, card)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}")

read_file_line_by_line("test.txt")