
src = {
 'a': 'A',
 'b': 'B',
}

data = {
    **src,
    'a': '__a__',
}


assert data == {'a': '__a__', 'b': 'B'}
assert data == {'b': 'B', 'a': '__a__'}


data = {
    'a': '__a__',
    **src,
}

assert data == {'a': 'A', 'b': 'B'}
