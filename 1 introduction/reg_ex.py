import re

print('---------- Was a Match Found ----------')
 
# Search for ape in the string
if re.search("ape","bitty baught a little buttle but the ape inside it"):
	print("there is a ape")

print('---------- Get All Matches ----------')
 

# findall() returns a list of matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")
for ape in allApes:
	print(ape)
	pass

print('---------- finditer----------')
# finditer returns an iterator of matching objects
# You can use span to get the location
 
theStr = "The ape was at the apex"
# . will include all ape after after
for i in re.finditer("ape.", theStr):
# Span returns a tuple
    locTuple = i.span()
 
    print(locTuple)
    print(theStr[locTuple[0]:locTuple[1]])


print('---------- Match 1 of Several Letters ----------')
 
# Square brackets will match any one of the characters between
# the brackets not including upper and lowercase varieties
# unless they are listed
 
animalStr = "Cat rat mat fat pat"
 #lower case c
allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)
 
print()
 
 # We can also allow for characters in a range
# Remember to include upper and lowercase letters
someAnimals = re.findall("[c-mC-M]at", animalStr)
for i in someAnimals:
    print(i)
 
print()

# Use ^ to denote any character but whatever characters are
# between the brackets
someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)
 
print()

print('---------- Replace All Matches ----------')
 
# Replace matching items in a string
 
owlFood = "rat cat mat pat"
 
# You can compile a regex into pattern objects which
# provide additional methods
regex = re.compile("[cr]at")
 
# sub() replaces items that match the regex in the string
# with the 1st attribute string passed to sub
owlFood = regex.sub("owl", owlFood)
 
print(owlFood)


print('---------- Solving Backslash Problems ----------')
 
# Regex use the backslash to designate special characters
# and Python does the same inside strings which causes
# issues.
 
# Let's try to get "\\stuff" out of a string
 
randStr = "Here is \\stuff"


# This won't find it
print("Find \\stuff : ", re.search("\\stuff", randStr))

# This does, but we have to put in 4 slashes which is
# messy
print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# You can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff : ", re.search(r"\\stuff", randStr))

print('---------- Matching Any Character ----------')

randStr = "F.B.I. I.R.S. CIA"
 
print("Matches :", len(re.findall(".\..\..", randStr)))