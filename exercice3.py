
# import random
# from W3D1 import Dog  # Importation de la classe Dog

# class PetDog(Dog):
#     def __init__(self, name, age, weight):
#         super().__init__(name, age, weight)  # Initialisation du parent (Dog)
#         self.trained = False  # L'attribut "trained" est False par défaut

#     def train(self):
#         # Imprime le message de l'aboiement et bascule "trained" à True
#         print(self.bark())  # Appel de la méthode bark de la classe parente
#         self.trained = True

#     def play(self, *args):
#         # Affiche que tous les chiens jouent ensemble
#         dog_names = ', '.join([dog.name for dog in args])  # recupere les noms des chiens
#         print(f"{dog_names} all plays together")

#     def do_a_trick(self):
#         # Si le chien est forme, il effectue un tour au hasard
#         if self.trained:
#             tricks = [
#                 f"{self.name} does a barrel roll",
#                 f"{self.name} stands on his back legs",
#                 f"{self.name} shakes your hand",
#                 f"{self.name} plays dead"
#             ]
#             print(random.choice(tricks))  # Choisi un tour au hasard
#         else:
#             print(f"{self.name} isnt trained yet.")


    


