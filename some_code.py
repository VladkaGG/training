def generator(iteration: int):
    a = 0
    for x in range(iteration):
        a += 1
        yield a


gen = generator(5)
try:
    for i in range(6):
        print(next(gen))
except StopIteration:
    print('It is end.')
