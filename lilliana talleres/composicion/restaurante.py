#ejemplo de composicion 2

class Cocina:
    def __init__(self,tipo):
        self.tipo = tipo
    def preparar_plato(self, plato):
        print(f" el plato {plato}  en la cocina {self.tipo}")
class Restaurante:
    def __init__(self,nombre,cocina_tipo):
        self.nombre= nombre
        self.cocina = Cocina(cocina_tipo)
    def recibir_orden(self,plato):
        print(f"recibiendo orden de un plato de {plato}")
        self.cocina.preparar_plato(plato)
restaurante = Restaurante("rikotas","ejecutiva")
restaurante.recibir_orden("pasta")
restaurante.cocina = Cocina("mexicana")
restaurante.recibir_orden("tacos")