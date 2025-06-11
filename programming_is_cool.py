# list comprehension

doubles = [x * 2 for x in range(1,11)]
print(doubles)

doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

a = lambda x: x * 2
print(a(10))

def double(x):
    return x * 2
print(double(10))   





