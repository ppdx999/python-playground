class Sample:
    only_class = 0
    both_class_and_instance = 0

    def __init__(self, only_instance, both_class_and_instance):
        self.only_instance = only_instance
        self.both_class_and_instance = both_class_and_instance

    def __str__(self):
        return f'only_instance = {self.only_instance}; only_class = {self.only_class}; both_class_and_instance = {self.both_class_and_instance}'


if __name__ == '__main__':
    print("Original values")
    s1 = Sample(1, 1)
    s2 = Sample(2, 2)

    print(f"  s1: {s1}")
    print(f"  s2: {s2}")

    print("s1.only_instance = 3")
    s1.only_instance = 3
    print(f"  s1: {s1}")
    print(f"  s2: {s2}")

    print("s1.only_class = 3")
    s1.only_class = 3
    print(f"  s1: {s1}")
    print(f"  s2: {s2}")

    print("s1.both_class_and_instance = 3")
    s1.both_class_and_instance = 3
    print(f"  s1: {s1}")
    print(f"  s2: {s2}")

    print("Sample.only_class = 5")
    Sample.only_class = 5
    print(f"  s1: {s1}")
    print(f"  s2: {s2}")

    print("Sample.both_class_and_instance = 3")
    Sample.both_class_and_instance = 3
    print(f"  s1: {s1}")
    print(f"  s2: {s2}")
