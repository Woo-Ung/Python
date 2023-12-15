#파이썬
##**기초 문법**

###**이름규칙**
- 변수는 글자 혹은 _로 시작해야함
- 글자는 A-z, 0-9, _ 만 사용 가능
- 대소문자 구분

함수 : function, my_function  
변수 : variable, my_variable  
Class : Bug, MyClass  
상수 : CONSTANT, MY_CONSTANT  
모듈 : module.py my_module.py

###**특수한 표기**
_internal_variable : protected 멤버
__properties : private 멤버
specual_case_ : keyword 중복을 피하기 위해
__magic_word__ : dunver(double underscore), 생성자, 빌트인 함수

###**코드블럭**
indent(들여쓰기)

**ex)**
if x> 0:
  print("x는 0보다 큽니다")
  

**주석**  
#한줄 주석입니다
or  

'''
여러줄 주석입니다
'''   
"""
여러줄 주석입니다
"""

**변수**
- 선언이 필요 없다. 동적타입

x = 0   
y = "hello"  
z = 3.14  
x, y, z = 0, "hello", 3.14

**리터럴**  
정수 - int -11, 0xffffffff  
실수 - float -3.14 (double 정밀도), 1.0e+8  
복소수 - complex -1.1 + 2.2j

논리 - bool - True, False   
문자열 - str - "print"  
                char 타입 x
                null_terminated X
                " ... "
                ' ... '
                r" ..."

" ' 혼용가능  
**ex)**   
print("Hello World")    
print('Hello World')  
print('"Hello World"')  
print("you are't my friend")

**시퀀스 타입(Sequence Type)**

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
  # C++의 range-based for
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
    pass    #빈함수

def test2():
    ...     #빈함수

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
    pass        ##오버로딩 개념은 굳이 필요없다

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


attribute - 멤버 변수


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

# m*n 미로를 좌상단에서 출발하여, 우하단으로 이동하는 경우의 수
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