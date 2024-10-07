class celular:
    #def __init__ es el constructor de la clase,osea 
    # lo que va a construir la clase cuando la llamemos
    def __init__(self,marca, modelo,camra) -> None:
        #atributos de instancia, son los tipos de atributos 
        # que va a tener una clase cuando sea invocada
        self.marca=marca
        self.modelo=modelo
        self.camra= camra
    #Esto es un metodo y siempre se les pasa self, para hacer referencia al objet
    def llamar(self):
        print(f'estas en llaamada en un:{self.modelo}')
    def cortar(self):
        print(f'cortaste la llaamada en un:{self.modelo}')
#instanciar una clase, o crear un objeto
celular1=celular("samsung","s23","48MP")
celular2 = celular("Apple","Ihopne 15 ","96MP")

print(celular1.cortar())
celular1.llamar()