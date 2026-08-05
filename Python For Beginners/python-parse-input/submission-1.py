from typing import List

def read_integers() -> List[int]:
    append_list = []
    user_input = input()
    
    integer_list = user_input.split(",")
    # return integer_list
    for element in integer_list:
        append_list.append(int(element))
    return list(append_list)

    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())