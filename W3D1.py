# exercices xp

# ecercice 1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
            
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'


# bengal = Bengal('Bengal', 3)
# chartreux = Chartreux('Chartreux', 4)
# siamese = Siamese('Siamese', 5)

# all_cats = [bengal, chartreux, siamese]

# sara_pets = Pets(all_cats)


# sara_pets.walk()








# exercice2+3

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         return f'{self.name} barks'

#     def run_speed(self):
#         return (self.weight / self.age) *10
    
#     def fight(self, other_dog):
#         strength = self.run_speed() * self.weight
#         other_strength = other_dog.run_speed() * other_dog.weight

#         if strength > other_strength:
#             return f"{self.name} won the fight"
#         elif strength < other_strength:
#             return f"{other_dog.name} won the fight"
#         else:
#             return 'tie match'
        

# dog1 = Dog('snoopy', 5, 30)
# dog2 = Dog('boulou', 4, 25)
# dog3 = Dog('booder', 3, 10)


# print(dog1.bark())
# print(dog2.bark())
# print(dog3.bark())

# print(f"run speed of {dog1.name}: {dog1.run_speed()} km/h")
# print(f"run speed of {dog2.name}: {dog2.run_speed()} km/h")
# print(f"run speed of {dog3.name}: {dog3.run_speed()} km/h")
    
# print(dog1.fight(dog2))  
# print(dog2.fight(dog3))  
# print(dog1.fight(dog3))




# the end of the exercice 3 is in exercice3.py and lines 308-328 of W3D1class








# exercice 4


# class Family:
#     def __init__(self, last_name, members):
#         self.last_name = last_name
#         self.members = members 

#     def born(self, **kwargs):
#         self.members.append(kwargs)  
#         print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 return member['age'] > 18
#         return False  

#     def family_presentation(self):
#         print(f"The {self.last_name} family consists of:")
#         for member in self.members:
#             print(f"{member['name']}, {member['age']} years old, Gender: {member['gender']}, Is Child: {member['is_child']}")


# family_members = [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
# ]

# family = Family("bokobza", family_members)




# family.family_presentation()

# family.born(name="lev", age=0, gender="Female", is_child=True)


# family.family_presentation()

# print(f"Is Michael over 18? {family.is_18('Michael')}")


# print(f"Is Sarah over 18? {family.is_18('Sarah')}")












# exercice5


# class Family:
#     def __init__(self, last_name, members):
#         self.last_name = last_name
#         self.members = members  

#     def born(self, **kwargs):
#         self.members.append(kwargs)  
#         print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

#     def is_18(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 return member['age'] > 18
#         return False  

#     def family_presentation(self):
#         print(f"The {self.last_name} family consists of:")
#         for member in self.members:
#             print(f"{member['name']}, {member['age']} years old, Gender: {member['gender']}, Is Child: {member['is_child']}")


# class TheIncredibles(Family):
#     def __init__(self, last_name, members):
#         super().__init__(last_name, members)

#     def use_power(self, name):
#         for member in self.members:
#             if member['name'] == name:
#                 if member['age'] > 18:
#                     print(f"{member['incredible_name']} has the power to {member['power']}!")
#                     return
#                 else:
#                     raise Exception(f"{member['name']} is not over 18 years old and cannot use their power.")
#         raise Exception(f"{name} not found in the family.")  

#     def incredible_presentation(self):
#         print("Here is our powerful family!")
#         super().family_presentation()  


# incredible_family = TheIncredibles("Incredibles", [
#     {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
#     {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
# ])

# incredible_family.incredible_presentation()


# incredible_family.born(name="Baby Jack", age=2, gender="Male", is_child=True, power="Unknown power", incredible_name="BabyJack")


# incredible_family.incredible_presentation()


# try:
#     incredible_family.use_power("Michael")  
# except Exception as e:
#     print(e)


# try:
#     incredible_family.use_power("Baby Jack")  
# except Exception as e:
#     print(e)







# daily challeng:

# import math

# class pagination:
#     def __init__(self, items=None, pageSize=10):
#         self.items = items if items is not None else []
#         self.pageSize = int(pageSize)
#         self.currentPage = 1
#         self.totalPages = math.ceil(len(self.items) / self.pageSize)     #.ceil = ca arrondit un nombre vers le haut. exemple si jai 3,2 ca va arrondir a 4

# # alphabetList = list("abcdefghijklmnopqrstuvwxyz")   
# # p = pagination(alphabetList, 4)      # je veux que mon p soit egale a la liste alphabet et quil imprime 4 items par page
# #        # print(p.totalPages)                  # 7 (26 lettres / 4 = 6.5, arrondi à 7 pages)
#     def getVisibleItems(self):
#         start_index = (self.currentPage - 1) * self.pageSize     #prmiere index de la page
#         end_index = start_index + self.pageSize                  #dernier index de la page
#         return self.items[start_index:end_index]                 #retour de la liste

# # alphabetList = list("abcdefghijklmnopqrstuvwxyz")   
# # p = pagination(alphabetList, 4)  #['a','b','c','d']    

# # print(p.getVisibleItems())   


#     def nextPage(self):
#         if self.currentPage < self.totalPages:  #verifi si jai la possibilite daller a la page suivante
#             self.currentPage += 1
#             return self
        
#     def prevPage(self):
#         if self.currentPage > 1:     #je verifie si je suis pas deja a la premiere page
#             self.currentPage -= 1
#             return self
        
#     def firstPage(self):
#         self.currentPage = 1   #met la page actuelle a 1
#         return self
    
#     def lastPage(self):
#         self.currentPage = self.totalPages      #met la page actuelle a la derniere
#         return self
        
# # alphabetList = list("abcdefghijklmnopqrstuvwxyz")   
# # p = pagination(alphabetList, 4)
# # p.nextPage()
# # print(p.getVisibleItems())

# # p.prevPage()
# # print(p.getVisibleItems())

# # p.firstPage()
# # print(p.getVisibleItems())

# # p.lastPage()
# # print(p.getVisibleItems())
   
#     def goToPage(self, pageNum):
#         pageNum = int(pageNum)  # convertit en entier si cest un float
#         if pageNum < 1:
#             self.currentPage = 1  # si on demande une page trop basse on met page 1
#         elif pageNum > self.totalPages:
#             self.currentPage = self.totalPages  # si trop grande on met la derniere
#         else:
#             self.currentPage = pageNum  # sinon on va a la page demande
#         return self

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")   
# p = pagination(alphabetList, 4)

# p.goToPage(2)          #['e','f','g','h']
# print(p.getVisibleItems())














