def add(*args):
    sum = 0
    for x in args:
        sum+=x
    return sum

print(add(4,5,1,5))