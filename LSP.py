

# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"

# def hacer_volar(ave=Ave()):
#     return ave.volar()

# print(hacer_volar(Pinguino()))
# #en este caso se nota que no se cumple el principio y la clase pinguino no puede hacer
# #Lo que podria hacer la clasecpadre

class Ave:
    pass

class Ave_voladora(Ave):
    def volar(self):
        return "Puedo volar"


class Ave_no_voladora(Ave):
   pass
    
