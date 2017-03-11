import functools

def rf(fs, sm):
    assert len(fs) == len(sm)
    if len(fs) == 1:
        #print("base")
        return fs[0]
    else:
        #print(fs[-1], end=" ")
        #print(functools.reduce(lambda x, y: x * y, sm[:-1]))
        return rf(fs[:-1], sm[:-1]) + (fs[-1] - 1) * functools.reduce(lambda x, y: x*y, sm[:-1])

for i in reversed(range(1, 6)):
    print(len([1, 3, 3, 2, 3, 3][:-i])-2)
    print(rf([1, 3, 3, 2, 3, 3][:-i], [1, 1, 1, 2, 1, 1][:-i]))
    print("---------------------------")


print(rf([1, 3, 3, 2, 3, 3], [1, 1, 1, 2, 1, 1]))
