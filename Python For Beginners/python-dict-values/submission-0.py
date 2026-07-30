from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values = list(age_dict.values())

    return values
        


    # val = []
    # for key, value in age_dict.items():
    #     val.append(value)
    # return val



# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
