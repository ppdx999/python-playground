from decimal import Decimal

a = Decimal('0.1')

assert a == Decimal('0.1')
assert a == Decimal('0.10')
assert a != 0.1
assert a != Decimal(0.1)
assert Decimal(0.1) == 0.1
print('All tests passed!')
