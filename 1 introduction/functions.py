i= 56
print (type(i))

# funtion with no return type

def display_greatings():
	print ("Welcome")

print (display_greatings());


# Example to return for funtion
def vol(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print (vol(10,3))

result = vol(10,3)

print("Volume fo the cylinder H= 10, r= 3 is {}".format(result))


print(str(b'Zoot!'))
print ('01\t012\t0123\t01234'.expandtabs())

mystring='abcdefghijklmnopqrstuvwxyz' 
print(mystring)
print(mystring.capitalize())
print(mystring.casefold())

print(mystring.find('fgh', 0, 16))

print('fgh' in mystring)