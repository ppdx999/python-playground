from dictknife import deepmerge
d0 = {
    "a": {
        "x": 1
    },
    "b": {
        "y": 10
    },
}
d1 = {
    "a": {
        "x": 1
    },
    "b": {
        "y": 15,
        "z": 10
    },
    "c": 100
}
actual = deepmerge(d0, d1)
expected = {
    "a": {
        "x": 1
    },
    "b": {
        "y": 15,
        "z": 10,
    },
    "c": 100
}

assert actual == expected
