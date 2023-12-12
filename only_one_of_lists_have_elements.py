from typing import List

def only_one_of_lists_have_elements(a: List, b: List):
    return bool(a) != bool(b)

# Test
assert only_one_of_lists_have_elements([], []) == False
assert only_one_of_lists_have_elements([1], []) == True
assert only_one_of_lists_have_elements([], [1]) == True
assert only_one_of_lists_have_elements([1], [1]) == False

print("All tests passed!")
