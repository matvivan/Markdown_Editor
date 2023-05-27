formatters = ["plain", "bold", "italic", "inline-code","header",
              "link", "new-line", "unordered-list", "ordered-list"]


def header_markdown():
    # READ THE NUMBER OF LEVEL UNTIL VALID
    while True:
        level = int(input("Level: "))
        if level not in range(1, 7):
            print("The level should be within the range of 1 to 6")
        else:
            break

    # READ HEADER TITLE AND COMPILE IN ONE STRING
    header_size = '#' * level
    header_text = input('Text: ')
    return header_size + ' ' + header_text + '\n'


def list_markdown(cmd):
    # READ A NUMBER OF ROWS
    while True:
        rows = int(input('Number of rows: '))
        if rows > 0:
            break
        else:
            print("The number of rows should be greater than zero")

    # MAKE THE LINES BY NUMBERS/STARS
    text_lines = ''
    flag = ['unordered-list', 'ordered-list'].index(cmd)
    for i in range(1, rows + 1):
        # READ THE LINE TEXT
        row_text = input(f"Row #{i}:")
        if flag:
            text_lines += f"{i}. {row_text}\n"
        else:
            text_lines += f"* {row_text}\n"
    return text_lines


text = ''
while True:
    command = input("Choose a formatter: ")
    if command in formatters:

        if command == "plain":
            # JUST ADDS A PLAIN TEXT
            text = text + input('Text: ')

        elif command == "bold":
            # ADDS DOUBLE STAR AT BOTH ENDS
            text = text + "**" + input('Text: ') + "**"

        elif command == "italic":
            # ADDS SINGLE STAR AT BOTH ENDS
            text = text + '*' + input('Text: ') + '*'

        elif command == "inline-code":
            # ADDS TILDES AT BOTH ENDS
            text = text + '`' + input('Text: ') + '`'

        elif command == 'link':
            # ADDS A FORMATTED STRING
            label = input('Label: ')
            url = input('URL: ')
            text = text + "[" + label + "](" + url + ")"

        elif command == 'new-line':
            # JUST ADDS A NEW LINE
            text = text + '\n'

        elif command == 'header':
            text += header_markdown()

        elif command in ['ordered-list', 'unordered-list']:
            text += list_markdown(command)

        # PRINT THE TEXT
        print(text)

    elif command == "!help":
        # PRINT HELP
        print("Available formatters: ", *formatters, "\nSpecial commands: !help !done")

    elif command == "!done":
        # END PROGRAM: OVERWRITE THE MARKDOWN FILE WITH TEXT, EXIT LOOP
        with open('output.md', 'w') as file:
            file.write(text)
        break

    else:
        # UNKNOWN COMMAND
        print("Unknown formatting type or command")
