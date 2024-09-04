#32. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized


def capitalize_lines(lines):
    return [line.upper() for line in lines]


def input_lines():
    lines = []
    print("Enter lines of text (type 'END' to finish):")
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)
    return lines

lines = input_lines()


capitalized_lines = capitalize_lines(lines)


print("\nCapitalized Lines:")
for line in capitalized_lines:
    print(line)
