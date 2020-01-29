class SomeClass:
    a = 0

    def go(self):
        self.a += 1
        yield 1


obj = SomeClass()
print(obj.go())
