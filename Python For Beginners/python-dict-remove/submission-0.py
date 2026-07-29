from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    ## accepts a dictionary my_dict, and a list of strings keys
    for element in keys:
        check = element in my_dict
        if check == True:
            del my_dict[element]
        else:
            my_dict.pop(element, 0)
    return my_dict




# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
