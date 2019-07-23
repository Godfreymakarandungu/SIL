
new_file = open("newFile.txt", 'w+')
#takes a long while:
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first name is godfrey\n")
   f.write("I am a student\n\n")
   f.write("i've written lines\n ")

print("Welcome to Python-programming!")
print(10//3)
print(13//3)
print(10/3)
print(5**2)

multi_line_quotes = ''' this has
some vertical whitespace!'''
print(multi_line_quotes * 2)

name = 'Python'
program = 'f-string'
print(f'Example of {name} {program}')
print('Coding %s without an %s.'%(name,program))
print('Let\'s name the language {}!'.format(name))
print('It makes snake-like threads and has {program}, name it {name}!'.format(name=name,program=program))

x = 18
y = 49
z = 32
print(f'Here\'s some math {x * y - z}')

#array flexibility
depth_chart = ['Oxygen', 'Water', 'Carbon', 'Nitrogen']
print(depth_chart)
print('Life first requires', depth_chart[0])

print('Can small-number celled organisms survive without it?')
depth_chart[0] = "Electricity"
print(depth_chart)

class Animal:

  __name = None
  __color = None
  __height = None
  __sound = None

  def __init__(self, name, color, height,sound):
    self.__name = name
    self.__color = color
    self.__height = height
    self.__sound = sound

  def set_name(self, name):
    self.__name = name

  def set__color(self, color):
    self.__color = color

  def set__height(self, height):
    self.__height = height

  def set__sound(self, sound):
    self.__sound = sound

  def get_name(self):
    return self.__name

  def get_color(self):
    return self.__color

  def get_height(self):
    return self.__height

  def get_sound(self):
    return self.__sound

  def get_type(self):
    print("Animal")

  def toString(self):
    return "{} is colored {} and is {} cm tall and says {}".format(self.__name, self.__color, self.__height, self.__sound)

class Cat(Animal):
  __owner = None

  def __init__(self, name, color, height, sound, owner):
    self.__owner = owner

    super(Cat, self).__init__(name, color, height, sound)

  def set_owner(self, owner):
    self.__owner = owner

  def get_owner(self):
    return self.__owner

  def toString(self):
    return "{} is colored {} and is {} cm tall and says {}. Wait, you no longer belong to {}!!".format(self.get_name(), self.get_color(), self.get_height(), self.get_sound(), self.__owner)

class Lizard(Animal):
  __owner = None

  def __init__(self, name, color, height, sound, owner):
    self.__owner = owner

    super(Lizard, self).__init__(name, color, height, sound)

  def set_owner(self, owner):
    self.__owner = owner

  def get_owner(self):
    return self.__owner

  def toString(self):
    return "{} is colored {} and is {} cm tall and says {}. Wait, you no longer belong to {}!!".format(self.get_name(), self.get_color(), self.get_height(), self.get_sound(), self.__owner)

kitty = Cat('Missie', 'brown/black', 14, 'Grrarrrr!!!', 'Mrs.susan')
print(kitty.toString())
richie = Lizard('Richie', 'green/black', 8, 'Tsssssss!!!', 'Mr.james')
print(richie.toString())