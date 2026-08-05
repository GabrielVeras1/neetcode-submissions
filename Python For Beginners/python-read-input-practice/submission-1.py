def add_two_numbers() -> int:
    append_list = []
    user_input = input()
    integer_list = user_input.split(",")
    
    for element in integer_list:
        append_list.append(int(element))
    
    total = append_list[0] + append_list[1]
    return total



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
