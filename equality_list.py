empty_list = []
alist = [1]

assert (empty_list or empty_list) == empty_list
assert (empty_list or alist) == alist
assert (alist or empty_list) == alist
assert (alist or alist) == alist

assert any([]) == False
assert any([0]) == False
assert any([1]) == True
assert all([]) == True
assert all([0]) == False
assert all([1]) == True

print("All tests passed!")
