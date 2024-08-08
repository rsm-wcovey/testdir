dct = {}

# add key-value pair to dictionary

dct['name'] = 'value1'
dct['name2'] = 'value2'

for key, value in dct.items():
    print(key, value)

dct = {}

lst = ["one", "two", "three", "four", "five"]

for n in lst:
    dct[n] = len(n)

print(dct)
