def remove_fourth_character(word: str) -> str:
    removed_pt1 = word[:3]
    removed_pt2 = word[(len(removed_pt1)) + 1:]

    new = removed_pt1 + removed_pt2
    return new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
