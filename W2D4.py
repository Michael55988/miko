# exercice xp

# exercice 1 



# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# miko_cat = Cat('Boulou', 26)
# uriel_cat = Cat('Minou', 7)
# zazou_cat = Cat('Aribot', 5)

# # print(f'Miko cat {miko_cat.name}, is {miko_cat.age} years old ')
# # print(f'Uriel cat {uriel_cat.name}, is {uriel_cat.age} years old')
# # print(f'zazou cat {zazou_cat.name}, is {zazou_cat.age} years old')


# def old_cat(cats):
#     old_cat = cats[0]  # je commence avec le premier chat de la liste
#     for cat in cats[1:]:  # je le compare avec les autres 
#         if cat.age > old_cat.age:
#             old_cat = cat
#     return old_cat



# # liste de chats
# cats = [miko_cat, uriel_cat, zazou_cat]

# # trouver le chat le plus vieux
# oldest_cat = old_cat(cats)


# print(f"The oldest cat is {oldest_cat.name} and he is {oldest_cat.age} years old.")







# exercice2


# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f'{self.name} does wofwof')

#     def jump(self):
#         print(f'{self.name} jumps {self.height *2} cm hight')

# davids_dog = Dog('Rex', 20)

# # print(f"david's dog  {davids_dog.name},  is {davids_dog.height} cm height ")
# # davids_dog.bark()
# # davids_dog.jump()
# sarahs_dog = Dog('teacup', 10)

# # print(f'sarah\'s dog {sarahs_dog.name}, is {sarahs_dog.height} cm height ')
# # sarahs_dog.bark()
# # sarahs_dog.jump()

# if davids_dog.height > sarahs_dog.height:
#     print(f'the bigger dog is {davids_dog.name}')
# elif davids_dog.height < sarahs_dog.height:
#     print(f'the bigger dog is {sarahs_dog.name}')
# else:
#     print('they measure the same')








# exercice 3



# class song:
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
        
        

#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# stairway= song(["There’s a lady who's sure ",
#                 "all that glitters is gold",
#                   "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()







# exercice4

# class zoo:
#     def __init__(self,zoo_name):
#         self.name = zoo_name
#         self.animals = []
#         self.sorted_groups = {}  #pour stocker les groupes d'animaux

#     def add_animals(self,new_animal):
#      if new_animal not in self.animals:
#       self.animals.append(new_animal)
#       print(f' {new_animal} has been added to the zoo')
#      else:
#       print(f'{new_animal} is allready in the zoo')

#     def get_animals(self):
#       print(f'{self.animals}')

#     def sell_animals(self, animal_sold):
#       if animal_sold in self.animals:
#         self.animals.remove(animal_sold)
#         print(f'{animal_sold} has been sold')
#         print(f'{self.animals}')
#       else:
#         print('this animal is not in the zoo')

#     def sort_animals(self):
#         self.animals.sort()  # trier la liste des animaux
#         sorted_dict = {}  #  je cree un dictionnaire pour stocker les animaux par lettre

#         for animal in self.animals:
#             first_letter = animal[0].upper()  # premiere lettre en majuscule
#             if first_letter not in sorted_dict:
#                 sorted_dict[first_letter] = []
#             sorted_dict[first_letter].append(animal)

#         # afiche tout propre apres le tri
#         print("Sorted animals:")
#         for key, value in sorted_dict.items():   #la premiere lettre en maj devient ma key et l'animal devient ma value. le .items() vient pour afficher ce que jai dans mon dict.
#             print(f"{key}: {value}")  
#             self.sorted_groups = {}  # Réinitialiser le dictionnaire des groupes

#         for animal in self.animals:
#             first_letter = animal[0].upper()  # Première lettre en majuscule
#             if first_letter not in self.sorted_groups:
#                 self.sorted_groups[first_letter] = []
#             self.sorted_groups[first_letter].append(animal)

#     def get_groups(self):
#         if not self.sorted_groups:
#             print("The animals haven't been sorted yet. Please call sort_animals() first.")
#             return
        
#         print("Animal Groups:")
#         for letter, animals in self.sorted_groups.items():
#             print(f"{letter}: {', '.join(animals)}")
        


# my_zoo = zoo('fellous safari')

# # my_zoo.add_animals('lion')
# # my_zoo.add_animals('elephant')
# # my_zoo.add_animals('elephant')
# # my_zoo.add_animals('bat')
# # my_zoo.add_animals('bear')
# # my_zoo.add_animals('monkey')
# # my_zoo.add_animals('baboon')
# # my_zoo.add_animals('mamouth')


# # my_zoo.get_animals()

# # my_zoo.sell_animals('lion')


# # my_zoo.add_animals('tiger')
# # my_zoo.sort_animals()
# # my_zoo.get_groups()



# new_yotk_zoo = zoo('new york zoo')

# new_yotk_zoo.add_animals('lion')
# new_yotk_zoo.add_animals('elephant')
# new_yotk_zoo.add_animals('elephant')
# new_yotk_zoo.add_animals('bat')
# new_yotk_zoo.add_animals('bear')
# new_yotk_zoo.add_animals('monkey')
# new_yotk_zoo.add_animals('baboon')
# new_yotk_zoo.add_animals('mamouth')


# new_yotk_zoo.get_animals()

# new_yotk_zoo.sell_animals('lion')


# new_yotk_zoo.add_animals('tiger')
# new_yotk_zoo.sort_animals()
# new_yotk_zoo.get_groups()


















# daily challlenge




# class Farm:
#     def __init__(self, farm_name):
#         self.farm_name = farm_name
#         self.animals = {}  # dictionnaire pour stocker les animaux et leurs quantites

#     def add_animal(self, animal, quantity=1):
#         if animal in self.animals:             #je rajoute un certain nombre danimaux a ma ferme. si jajoute un animal qui existe deja sa quantite se mettra a jour seule
#             self.animals[animal] += quantity
#         else:
#             self.animals[animal] = quantity

#     def get_info(self):
#         info = f"{self.farm_name}'s farm\n"
#         #  formate les animaux avec un alignement sur les noms et les quantites a l'aide de :<5 ligne 250. 
#         for animal, quantity in self.animals.items():
#             info += f"{animal:<5} : {quantity:>5}\n"            
#         info += "\n    E-I-E-I-O!"
#         return info


# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

        















        