from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    tracker = {}
    for char in word:
        if char in tracker:
            tracker[char] = tracker[char] + 1
        else:
            tracker[char] = 1
    return tracker



# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
