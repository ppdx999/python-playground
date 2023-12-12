def only_one_of_three_is_true(a, b, c):
    return a ^ b ^ c and not (a and b and c)

# improve the above
def only_one_of_three_is_true_2(a, b, c):
    return sum([a, b, c]) == 1

#
# test
#
assert only_one_of_three_is_true(True, False, False)
assert only_one_of_three_is_true(False, True, False)
assert only_one_of_three_is_true(False, False, True)
assert not only_one_of_three_is_true(True, True, False)
assert not only_one_of_three_is_true(True, False, True)
assert not only_one_of_three_is_true(False, True, True)
assert not only_one_of_three_is_true(True, True, True)
assert not only_one_of_three_is_true(False, False, False)

assert only_one_of_three_is_true_2(True, False, False)
assert only_one_of_three_is_true_2(False, True, False)
assert only_one_of_three_is_true_2(False, False, True)
assert not only_one_of_three_is_true_2(True, True, False)
assert not only_one_of_three_is_true_2(True, False, True)
assert not only_one_of_three_is_true_2(False, True, True)
assert not only_one_of_three_is_true_2(True, True, True)
assert not only_one_of_three_is_true_2(False, False, False)

print("All tests passed")


