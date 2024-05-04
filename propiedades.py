class Datos:
    def  __init__(self,nombre) :
        #atributo privado o protegido
        self._nombre= nombre
        
    #le asigamos que sea una propiedad y con un decorador
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre= new_nombre
    @nombre.deleter
    def nombre(self):
        del self._nombre
fran = Datos("fran","1123")
nombre= fran.nombre
print(nombre)

#usamos el setter
fran.nombre = "juan"

#usamos el getter
nombre= fran.nombre

#usamos deleter
del fran.nombre
print(nombre)
