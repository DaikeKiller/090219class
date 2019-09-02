# first module.py

def addition():
	print("add")
        a = 1
        b = 2
        print("a = {}".format(a))
        c = a+b
        print("{} + {} = {}".format(a,b,c))
	return
def subtract():
	print("add")
        a = 1
        b = 2
        print("a = {}".format(a))
        c = a+b
        
if __name__ = "__main__":
	print("{} + {} = {}".format(a,b,c))

	x = input("input a command:")
	print("You enter {}.".format(x))
	if x == "add" or x == "a":
		addition()
	elif x == "s":
		subtract()
	else:
		print("{} is not an active command".format(x))
	print("Done")
		
