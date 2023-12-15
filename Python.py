#���̽�
##**���� ����**

###**�̸���Ģ**
- ������ ���� Ȥ�� _�� �����ؾ���
- ���ڴ� A-z, 0-9, _ �� ��� ����
- ��ҹ��� ����

�Լ� : function, my_function  
���� : variable, my_variable  
Class : Bug, MyClass  
��� : CONSTANT, MY_CONSTANT  
��� : module.py my_module.py

###**Ư���� ǥ��**
_internal_variable : protected ���
__properties : private ���
specual_case_ : keyword �ߺ��� ���ϱ� ����
__magic_word__ : dunver(double underscore), ������, ��Ʈ�� �Լ�

###**�ڵ��**
indent(�鿩����)

**ex)**
if x> 0:
  print("x�� 0���� Ů�ϴ�")
  

**�ּ�**  
#���� �ּ��Դϴ�
or  

'''
������ �ּ��Դϴ�
'''   
"""
������ �ּ��Դϴ�
"""

**����**
- ������ �ʿ� ����. ����Ÿ��

x = 0   
y = "hello"  
z = 3.14  
x, y, z = 0, "hello", 3.14

**���ͷ�**  
���� - int -11, 0xffffffff  
�Ǽ� - float -3.14 (double ���е�), 1.0e+8  
���Ҽ� - complex -1.1 + 2.2j

�� - bool - True, False   
���ڿ� - str - "print"  
                char Ÿ�� x
                null_terminated X
                " ... "
                ' ... '
                r" ..."

" ' ȥ�밡��  
**ex)**   
print("Hello World")    
print('Hello World')  
print('"Hello World"')  
print("you are't my friend")

**������ Ÿ��(Sequence Type)**

- list

- tuple

- set

- dict

#if
if x> 1:
    print("x >1")
elif x< 1:
    print("x <1")
else:
    print("x =1")

if 1 <= x <= 10:
    print("1 <= x <= 10")

# match
operator = "+"

match operater:
    case "+":
      print("Addition")
    case "-":
      print("Subtraction")
    case "*":
      print("Multiplication")
    case "/":
      print("Division")
    case "and" | "or" | "not":
      print("Logical")
    case _":
      print("Invaild operator")

  # while
  i = 0
  while i < 5:
      print(i)
      i += 1

  # for
  # C++�� range-based for
  champions = ['Lux','Ahri','Ezreal','zed']
  for champions in champions:
      print(champions)
  
  champion = {"name": "Lux", "type": "magician", "skill":"light"}

    for element in champions:
        print(element)
  
    for item in champion.items():
      print(item)

# list comprehension
numbers = [1,2,3,4,5]
for number in numbers:
    if number > 3:
        print(number)

comp = [number for number in numbers if number > 3]
print(comp)

# function

def square(x):
    return x ** 2

def test():
    pass    #���Լ�

def test2():
    ...     #���Լ�

def return_many():
    retrun 1,2,3

a, b, c = return_many()
print(return_many())

###

def create_champion(name, lane="mid"):
    print("Creating" + name + "in" + lane)

  create_champion("ahri")
  # named arguments
  create_champion(name="aatrox", lane="top")

###

 def create_champion(name, lane="mid"):
    print("Creating" + name + "in" + lane)

  def rotation_champs(func)
      func("Ahri")
      func("Lux")
      func("zed")

  rotation_champs(create_champion)

  # arbitrary arguments

  def f1(*args):
      for arg in args:
        print(arg)
  
  f1(1,2,3,4)

def f2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

f2(a=1, b=3.14, c="hello")

# function overloading
def func(*args):
    pass        ##�����ε� ������ ���� �ʿ����

# Object Oriented Programming
class Champion:
  #double underscore - dunder - special methods

    # special method
    def __init__(self):
        self.name = name # arrribute
        self.hp = hp
        print("Champion created")

    # method
    def move(self):
        print(f"{self.name} moves")

ahri = Champion("ahri", 100)
print(f"{name:{ahri.name}}, hp:{ahri.hp}")


###
class Point2D:
    def __init__(self, x, y):
      self.x = x
      self.y = y

    def __str__(self):
      return f"({self.x},{self.y})"

    def __add__(self, other):
      return Point2D(self.x + other.x, self.y + other.y)

  pt1 = Point2D(10, 20)
  pt2 = Point2D(30, 40)
  print(pt1 + pt2)

###
class Golum:
  def __init__(self):
    self.my_precious = None
    print("constructor")

  @property # @ = decorater
  def my_precious(self):
    print("getter")
    return self.__my_precious

  @my_precious.setter
  def my_precious(self, value):
      print("setter")
      self.__my_precious = value

g = Golum()
g.my_precious = "The Ring"
print(g.my_precious)

# name mangling
print(g._Golum__my_precious)


attribute - ��� ����


# inheritance
class Animal:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      print("Animal Create")

    def sound(self):
      print("Animal sound #!@~!@#")

class Cat(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)
    print("Cat Created")

    def sound(self):
      print("Meow")
    
instance = Animal("kitty", 3)
instance = Cat("kitty", 3)
instance.sound()

# polymorphism
class Animal:
  pass

class Cat(Animal):
  def sound(self):
    print("Meow")

class Dog(Animal):
  def sound(self):
    print("Bark")

animals =[Cat(), Dog(), Cat(), Cat(), Dog()]
for animal in animals:
  animal.sound()


# static variable
Class MyClass:
  variable = 1

  def func():
    print("This is a message inside the class.")

c1 = MyClass()
c2 = MyClass()
MyClass.variable = 3

c1.variable = 1
c2.variable = 2
print(f"{c1.variable} {c2.variable} {MyClass.variable}")

###
class Utility:
  @staticmethod
  def sum(x,y):
    return x+y

Utility.sum(1,2)


# module
from math import sqrt

print(sqrt(10))

###
import random

word = ["a", "b", "c", "d", "e"]

random.shuffle(word)
print(word)

# m*n �̷θ� �»�ܿ��� ����Ͽ�, ���ϴ����� �̵��ϴ� ����� ��
# brute force
def find_wats(m,n = {}):
  if m == 0 or n == 0:
    return 0
  if m == 1 or n == 1:
    return 1

  if (m,n) in memo:
    return memo[(m,n)]

  memo[(m,n)] = find_wats(m-1, n) + find_wats(m, n-1)
  return memo[(m,n)]

m, n = 2, 3
print(find_wats(m, n))