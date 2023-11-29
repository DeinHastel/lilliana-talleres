class Mago:
    def defender(self):
        print("escudo magico")
class Arquero:
    def defender(self):
        print("esconderse")
class Samurai:
    def defender(self):
        print("atacando, (el ataque es la mejro defensa)")
class Cucha:
    def defender(self):
        print("entonces pague usted los servicios")
merlin = Mago()

elfin = Arquero()

takeo = Samurai()

mama = Cucha()

personajes = [merlin,elfin,takeo,mama]

for personaje in personajes:
    personaje.defender()