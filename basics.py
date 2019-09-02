# basics.py
x = input("input a command:")
print("You enter {}.".format(x))
if x == "add" or x == "a":
	print("add")
	a = 1
	b = 2
	print("a = {}".format(a))
	c = a+b
	print("{} + {} = {}".format(a,b,c))
elif x == "s":
	print("subtract")
	a = 1
	b = 2
	c = a - b
	print("{} - {} = {}".format(a,b,c))
else:
	print("{} is not an active command".format(x))
print("Done")
