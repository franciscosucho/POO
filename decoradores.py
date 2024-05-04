
# creamos el decorador
def decorador(funtion):
    #creamos la funcion decoradora
    def funcion_modificada():
        #podemos escribir codigo tanto como antes y despues 
        # de llamar ala funcion
        print("Antes de llamar ala funcion")
        funtion()
        print("Despues de llamar ala funcion")
    #returnamos la nueva funcion para guardarla como un metodo
    return funcion_modificada


# def hola():
#     print("hola")
# #la guardamos como una variable
# saludo_mod= decorador(hola)
# saludo_mod()

#MANERA OPTIMA DE INVOCAR UN DECORARDOR
#creamos la funcion sobre el decorador
@decorador
def hola():
    print("hola")
hola()