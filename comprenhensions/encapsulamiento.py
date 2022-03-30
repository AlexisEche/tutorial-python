class usuario():
    def __init__ (self, nombre, clave):
      self.__nombre = nombre
      self.__clave = clave

    @property
    def nombre(self):
      return self.__nombre

    @nombre.setter
    def nombre(self,nuevo):
      print("Modificando el nombre")
      self.__nombre = nuevo
      print("Nombre modificado")

    @nombre.deleter
    def nombre(self):
      print("Borrando nombre")
      del self.__nombre

    def clave(self):
      return self.__clave


Usuario1 = usuario("Nikola","Tesla")

del Usuario1.nombre
Usuario1.nombre = "Miguel"

print(Usuario1.nombre)
