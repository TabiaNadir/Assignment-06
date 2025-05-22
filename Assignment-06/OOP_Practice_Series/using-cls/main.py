class Counter:
    object_count = 0

    def __init__(self):
        Counter.object_count += 1

    @classmethod
    def display_count(cls):
        """Class method to display the total number of objects"""
        print(f"Total objects created: {cls.object_count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_count()
