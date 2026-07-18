from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    ##we want to go through our list length, go to its end, then append
    append_length = (len(elements) + 1)
    append_list = elements
    ## then its index has to be -1 the length since we start at 0
    for element in elements:
        my_list.append(element)
  
    return my_list



# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))
