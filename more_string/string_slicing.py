#string slicing

string = "Hello World. this is new world"
hello = string[0:5]
hello1 = string[:5] #f I know, string slicing starts from the first index, which is zero.
print(hello)
print(hello1)

world = string [5:] #count Spece
world1 = string[6:]
world2 = string[6: len(string)]
print(world)
print(world1)
print(world2)