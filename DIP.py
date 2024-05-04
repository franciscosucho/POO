
#ESTO DE ABAJO ESTA MAL,YA QUE LA CLASE PRINCIPLA"VERIFICADOR ORTOGRAFICO" DEPENDE DE UNA CLASE DE MENOR IMPORTANCIA, DICCIONARIO

# class Diccionario():
#     def verificar_palabras(self):
#         #logica para verificar palabras
#         pass
# class Verificador_Ortografico():
#     def __init__(self):
#         self.diccionario= Diccionario()
#     def Corregir_texto():
#         #usamos el diccionario para corregirlo
#         pass

# Este seria el codigo que esta bien, ya que el corrector ortografico es la clase principal y no depende de otra clase, sino que las clases dependen de ella,
from abc import ABc, abstractclassmethod

class Verificador_ortografico(ABc):
    @abstractclassmethod
    def Verificar_palabra(self,palabra):
        pass
    
def Diccionario(Verificador_ortografico):
    def Verificar_palabra(self,palabra):
        #logica para verificar palabras si esta en el diccionario
        pass
def Corrector_ortorgrafico():
    def __init__(self,verificador):
        self.verificador = verificador
    def corregir_texto(self,texto):
        #usamos el verificador para corregir texto, no el diccionario.
        pass