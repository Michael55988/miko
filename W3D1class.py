# class Animal():
#      def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#      def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     pass

# rex= Dog("dog", 4, "wouaf")
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# print('This dog has', rex.number_legs , ' legs')
# # >> This dog has 4 legs

# print('This dog makes the sound ', rex.sound)
# # >> This dog makes the sound wouaf

# rex.make_sound()
# # >> I am an animal, and I love saying wouaf

# class Cat(Animal):
#     pass

# chouquette = Cat('cat', 4, 'miaou')
# print('this animal is a:', chouquette.type)
# print('this animal has:', chouquette.number_legs, 'legs')
# chouquette.make_sound()









# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)

# nc = NewCircle(1)
# print(nc.diameter)

# nc.grow()

# print(nc.diameter)
# # >> What will be the output






# ce code affichera erreur parce que la methode fetch_ball appartient a la class Dog et pas a la class Animal. alors que le sence inverse fonctionne cest tout le but des heritiers

# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")

# class Dog(Animal):
#     def fetch_ball(self):
#         print("I am a dog, and I love fetching balls")

# rex = Dog('dog', 4, "Wouaf")
# print('This animal is a:', rex.type)
# # >> This animal is a dog

# rex.fetch_ball()
# # >> I am a dog, and I love fetching balls

# roger = Animal('Roger', 4, "Grr")
# roger.fetch_ball()









# class Animal():
#     def __init__(self, type, number_legs, sound):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

# class Dog(Animal):
#     def __init__(self, type, number_legs, sound, fetch_ball):
#         super().__init__(type, number_legs, sound)                #super().__init__ sert a meviter de reecrir les lignes 103-105 si je veux les retuliser pour ma class Dog.
#         self.fetch_ball = fetch_ball

# boulou = Dog('dog', 4, 'wouaf', True)
# print(boulou.number_legs)
# print(boulou.type)
# print(boulou.sound)






# class Family():
#     def __init__(self, surname):
#      self.surname = surname

# class Child(Family):
#    def __init__(self, name, surname):
#       super().__init__(surname)
#       self.name = name        

# Lev = Child('Lev', 'levinski')
# elsa = Child('elsa', 'zazou')

# print('my surnamename is ', Lev.surname, 'but my real name is', Lev.name)


# class cousins(Family):
#    def __init__(self, surname):
#       super().__init__(surname)

# aaron = cousins('aaronzoo')
# print(aaron.surname)







# class door:
#     def __init__(self, is_opened = True):
#         self.is_opened = is_opened

#     def open_door(self):
#         self.is_opened = True

#     def close_door(self):
#         self.is_opened = False

# class BlockDoor(door):
#     def __init__(self):
#         super().__init__(False)

#     def open_door(self):
#         raise ValueError('a blocked door cannot be opened')
    
#     def close_door(self):
#         return super().close_door()
    
# my_door = BlockDoor()
# my_door.open_door()








# class Computer():

#     def __init__(self):
#         self.name = "Apple Computer" # public
#         self.__max_price = 900 # private

#     def sell(self):            # public method
#         print(f"Selling Price: {self.__max_price}")

#     def __sell(self):          # private method
#       print('This is private method')

#     def set_max_price(self, price):
#         self.__max_price = price

# c = Computer()
# c.__sell()       # le fait davoir mit 2_ -> .__sell() lutilisateur aura pas acces a la fonction vu quelle est privee donc ca imprimera AttributError parce que ligne 184 jai mit self.__max_price du coup je lai blocker a lutilisateur






# polymorphisme- designes des class diferentes ou apparentees qui utilises les memes noms pour leurs fonctions.

# class Parrot():

#     def fly(self):
#         print("Parrot can fly")

#     def swim(self):
#         print("Parrot can't swim")

# class Penguin():

#     def fly(self):
#         print("Penguin can't fly")

#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# flying_test(blu)

# flying_test(peggy)











# class Alien():
#     def __init__(self, name, planet):
#         self.name = name
#         self.planet = planet

#     def fly(self):
#         print(self.name, 'is flying!')

#     def sleep(self):
#         print("Aliens don't sleep")

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def sleep(self):
#         print("zzzZZZZZ")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barked, WAF !")

# class AlienDog(Alien, Dog):
#     def bark(self):
#         print(f"{self.name} barked, 0ul10ul0u (that's how aliens dogs bark..) !")


# my_normal_dog = Dog("Roger")
# my_normal_dog.sleep()
# # >> zzzZZZZZ

# my_normal_dog.bark()
# # >> Roger barked, WAF !

# my_alien_dog = AlienDog("Rex", "Neptune")
# print(my_alien_dog.planet)
# # >> Neptune

# my_alien_dog.fly()
# # >> Rex is flying!

# my_alien_dog.sleep()
# # >> Aliens don't sleep

# my_alien_dog.bark()
# # >> Rex barked, 0ul10ul0u (that's how aliens dogs bark..) !











# pour les modules voir dossier modules files pizza et making pizza







# xp exercice: exercice 3

# from exercice3 import PetDog

# # je cree de 3 chiens
# dog1 = PetDog('snoopy', 5, 30)
# dog2 = PetDog('boulou', 4, 25)
# dog3 = PetDog('booder', 3, 10)

# # je les fais aboyer les chiens
# dog1.train()  # Rex est entraîné
# dog2.train()  # Buddy est entraîné
# dog3.train()  # Max est entraîné

# # Faire jouer les chiens ensemble
# dog1.play(dog2, dog3)

# # Demander à chaque chien de faire un tour
# dog1.do_a_trick()
# dog2.do_a_trick()
# dog3.do_a_trick()










