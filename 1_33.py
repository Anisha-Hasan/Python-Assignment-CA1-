
def generate_list_and_tuple(input_string):

    number_list = input_string.split(',')
    number_tuple = tuple(number_list)
    return number_list, number_tuple

input_string = input("Enter a sequence of comma-separated numbers: ")

number_list, number_tuple = generate_list_and_tuple(input_string)

print("List:", number_list)
print("Tuple:", number_tuple)
