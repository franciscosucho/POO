class Documento:
    def __init__(self, contenido):
        self.contenido = contenido

    def obtener_contenido(self):
        return self.contenido

class Impresora:
    def __init__(self):
        pass

    def imprimir(self, documento):
        # Delegación: La impresora delega en el documento la tarea de obtener su contenido
        print(f"Imprimiendo: {documento.obtener_contenido()}")

# Crear un documento
doc = Documento("Contenido del doc")

# Crear una impresora
impresora = Impresora()

# Imprimir el documento (delegación)
impresora.imprimir(doc)