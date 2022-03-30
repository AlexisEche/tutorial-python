def decorator(func):
  def new_function():
    print("El perro dice: ")
    func()

  return new_function

@decorator
def saluda():
  print("Guau! ")

saluda()


class my_decorator(object):
  def __init__(self,func):
    self.func = func
  
  def __call__(self):
    self.func()

@my_decorator
def talk():
  print("Hello !")

talk()