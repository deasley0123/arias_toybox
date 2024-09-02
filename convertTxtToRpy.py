def read_file_line_by_line(file_path):
    unknownName = ("q", "???")
    narrator = ("n", "")

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Iterate over each line in the file
            name = unknownName
            for line in file:
                curLine = line
                if curLine[0] == '#':
                    #We've got ourselves a new name card
                    curLine = curLine.lstrip('#').strip()
                    if curLine.isalnum():
                        name = (curLine[0].lower(), curLine)
                    else:
                        name = unknownName
                    print(name)
                else:
                    print(curLine.strip())
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except IOError as e:
        print(f"An IOError occurred: {e}")

read_file_line_by_line("test.txt")