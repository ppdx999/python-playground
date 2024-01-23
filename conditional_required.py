def conditional_required(*args) -> bool:
    # print([all(v or []) for v in args].count(True))
    return [all(v or [False]) for v in args].count(True) > 0

def one_of_them_required(*args) -> bool:
    return [any(v or [False]) for v in args].count(True) == 1

def more_than_one_required(*args) -> bool:
    return [any(v or [False]) for v in args].count(True) > 1

assert bool(filter(None, [None, None])) is True
assert any([None, None]) is False
assert any(["1", None]) is True
assert any([None, "1"]) is True
assert any(["1", "1"]) is True
assert any(["0", "0"]) is True
assert any(["", None]) is False
assert any("") is False
assert any("1") is True
assert any("0") is True
assert any("") is False
assert any([ None ]) is False
assert bool([None, "1"]) is True
assert all([None, "1"]) is False
assert all([]) is True
assert all([None, None]) is False
assert all([None, "1"]) is False
assert all(["1", None]) is False
assert all(["1", "1"]) is True

assert conditional_required("1", [ None, None ]) is True
assert conditional_required(None, [ "1", "1" ]) is True
assert conditional_required(None, [ "1", None ]) is False
assert conditional_required(None, [ None, "1" ]) is False
assert conditional_required("1", [ "1", None ]) is True
assert conditional_required("1", [ None, "1" ]) is True
assert conditional_required("1", [ "1", "1" ]) is True

assert all("1") != all([None, None])
assert all("1") != all([None, "1"])
assert all("1") != all(["1", None])
assert all("1") == all(["1", "1"])
assert all(None or [False]) == all([None, None])
assert all(None or [False]) == all([None, "1"])
assert all(None or [False]) == all(["1", None])

print("All tests passed")
