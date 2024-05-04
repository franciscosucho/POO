class Datos:
    def  __init__(self,nombre,contra) :
        #atributo privado o protegido
        self._nombre= nombre
        #atributo muy privado o privado
        self.__contra = contra
    def get_nombre(self):
        return self._nombre
    def get_contra(self):
        return self.__contra
    def set_nombre(self, new_nombre):
        self._nombre= new_nombre
        
    def set_contra(self,new_contra):
        self.__contra= new_contra
fran = Datos("fran","1123")
#METODOS 
nombre= fran.get_nombre()
#asi se acceso a un dato privado
print(nombre)

fran.set_nombre("pedro")
nombre = fran.get_nombre()
print(nombre)