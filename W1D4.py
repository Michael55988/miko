# Instructions
# Créez un ensemble appelé my_fav_numbersavec tous vos numéros favoris.
# Ajoutez deux nouveaux nombres à l’ensemble.
# Supprimez le dernier numéro.
# Créez un ensemble appelé friend_fav_numbersavec les numéros préférés de vos amis.
# Concaténer my_fav_numberset friend_fav_numbersà une nouvelle variable appelée our_fav_numbers.


# 🌟 Exercice 2 : Tuple
# Instructions
# Étant donné un tuple dont la valeur est un entier, est-il possible d'ajouter plus d'entiers au tuple ?



# 🌟 Exercice 3 : Liste
# Instructions
# Utilisation de cette listebasket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Supprimez « Banane » de la liste.
# Supprimez « Myrtilles » de la liste.
# Ajoutez « Kiwi » à la fin de la liste.
# Ajoutez « Pommes » au début de la liste.
# Comptez combien de pommes il y a dans le panier.
# Vider le panier.
# Imprimer (panier)


# 🌟 Exercice 4 : Flotteurs
# Instructions
# Récapitulatif – Qu'est-ce qu'un float? Quelle est la différence entre un entier et un flottant ?
# Créez une liste contenant la séquence suivante de nombres flottants et d'entiers (il doit s'agir d'une liste avec des types mixtes) : 1,5, 2, 2,5, 3, 3,5, 4, 4,5, 5 (ne codez pas en dur la séquence).
# Pouvez-vous penser à une autre façon de générer une séquence de flottants ?


# 🌟 Exercice 5 : Boucle For
# Instructions
# Utilisez une forboucle pour imprimer tous les nombres de 1 à 20 inclus.
# À l'aide d'une forboucle allant de 1 à 20 (inclus), imprimez chaque élément qui a un index pair.


# 🌟 Exercice 6 : Boucle While
# Instructions
# Écrivez une boucle while qui demandera continuellement à l'utilisateur son nom, à moins que l'entrée ne soit égale à votre nom.



# 🌟 Exercice 7 : Fruits préférés
# Instructions
# Demandez à l'utilisateur de saisir son ou ses fruits préférés (un ou plusieurs fruits).
# Astuce : utilisez la méthode intégrée input. Demandez à l'utilisateur de séparer les fruits par un espace, par exemple "apple mango cherry".
# Stockez le(s) fruit(s) préféré(s) dans une liste (convertissez la chaîne de mots en une liste de mots).
# Maintenant que nous avons une liste de fruits, demandez à l'utilisateur de saisir le nom de n'importe quel fruit.
# Si l'entrée de l'utilisateur se trouve dans la liste des fruits favoris, imprimez « Vous avez choisi l'un de vos fruits préférés ! Bon appétit ! ».
# Si la saisie de l'utilisateur n'est PAS dans la liste, indiquez : « Vous avez choisi un nouveau fruit. J'espère que vous l'apprécierez. »


# Exercice 8 : Qui a commandé une pizza ?
# Instructions
# Écrivez une boucle qui demande à un utilisateur de saisir une série de garnitures de pizza, lorsque l'utilisateur saisit « quit », il arrête de demander des garnitures.
# Au fur et à mesure qu'ils ajoutent chaque garniture, imprimez un message indiquant que vous ajouterez cette garniture à leur pizza.
# À la sortie de la boucle, imprimez toutes les garnitures sur la pizza et quel est le prix total (10 + 2,5 pour chaque garniture).


# Exercice 9 : Cinemax
# Instructions
# Un cinéma pratique des prix de billets différents en fonction de l'âge d'une personne.
# si une personne a moins de 3 ans, le billet est gratuit.
# s'ils ont entre 3 et 12 ans, le billet est à 10 $.
# s'ils ont plus de 12 ans, le billet coûte 15 $.

# Demandez à une famille l’âge de chaque personne qui veut un billet.

# Enregistrez le coût total de tous les billets de la famille et imprimez-le.

# Un groupe d'adolescents vient dans votre cinéma et souhaite voir un film interdit aux 16-21 ans.
# À partir d'une liste de noms, créez un programme demandant l'âge de chaque adolescent. S'il n'est pas autorisé à voir le film, retirez-le de la liste.
# À la fin, imprimez la liste finale.


# Exercice 10 : Commandes de sandwichs
# Instructions
# En utilisant la liste ci-dessous :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# La charcuterie n'a plus de pastrami, utilisez une whileboucle pour supprimer toutes les occurrences de « sandwich au pastrami » de sandwich_orders.
# Nous devons préparer les commandes des clients :
# Créez une liste vide appelée finished_sandwiches.
# Retirez un à un chaque sandwich de sandwich_ordersla liste tout en les ajoutant à celle-ci finished_sandwiches.
# Une fois tous les sandwichs préparés, imprimez un message répertoriant chaque sandwich préparé, par exemple :
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich





# exercice 1:

# my_fav_numbers = {1, 2, 3, 4, 5}
# my_fav_numbers.add(555)
# my_fav_numbers.add (55)
# print(my_fav_numbers)
# my_fav_numbers.discard(5)
# print(my_fav_numbers)
# friend_fav_numbers = {6,7,8,9,10}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)




# # exercice 2:

# we cannot add things to a tuple but i can creat a new one based on the first.

# tuple = (1,2,3,4,5)
# tuple2 = tuple + (6,7)
# print(tuple2)








# exercice 3:

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)

# basket.remove('Banana')
# print(basket)

# basket.remove('Blueberries')
# print(basket)

# basket.append('kiwi')
# print(basket)

# basket.insert(0, 'Apples')
# print(basket)

# print(basket.count('Apples'))
# basket.clear()

# print(basket)






# exercice4:

# 1  a float is a not full number  1.2, 5.5 .  and an integer is a full number 2, 3, 4....

# 2
# numbers = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(numbers)






# exercice 5:

# numbers = range(1,21)
# for number in numbers:
#  print(number)
 
# for i in range(1, 21):
    
#     if i % 2 == 0:
#         print(i)





# exercice 6:

# my_name = 'miko'
# while True:
#     user_name = input('what is your name??')
#     if user_name == my_name:
#         print('Nice Name')
#         break
#     else:
#       print('Try Again')




# exercice 7:

# fav_fruits = input('what are your fav fruits?')
# fav_fruits_list = fav_fruits.split()
# chosen_fruits = input('choose a fruit')
# if chosen_fruits in fav_fruits_list:
#     print('you chose a fav fruit. enjoy!')
# else:
#     print('not your fav fruit. hope you will love it!')







# exercice 8:


# pizza_price = 10
# toppings = []  


# while True:
#     topping = input("enter a topping for your pizz or 'quit' is done: ")
    
#     if topping == 'quit':
#         break  
    
#     toppings.append(topping)                                      dans ma liste toppings je rajoute ce que lutilisateur rajoutera dans topping
#     print(f"you add {topping} to your pizza.")  


# total_price = pizza_price + (2.5 * len(toppings))           mon prix total qui est = a mon prix de base de la pizz x 2.5$ pour chaque (ca se compte avec (len)) elements quil y a dans ma liste toppings


# print("\ntoppings on your pizza :")
# for topping in toppings:
#     print(f"- {topping}")

# print(f"\n total price of your pizza : {total_price}$")







# exercice 9:
 

# # Initialiser le cout total des billets
# total_cost = 0

# # Demande combien de personnes sont dans la famille
# number_of_people = int(input("how many family members ? "))

# # Boucle pour demander lage de chaque personne
# for person in range(1, number_of_people + 1):
#     age = int(input(f"how old are person {person} ? "))
    
#     # Determiner le prix du billet en fonction de lage
#     if age < 3:
#         print("ticket is free.")
#     elif 3 <= age <= 12:
#         print("ticket cost 10$.")
#         total_cost += 10
#     else:
#         print("ticket cost 15$.")
#         total_cost += 15

# # Afficher le cout total de tous les billets
# print(f"total cost for the family is {total_cost} $.")



#      # Liste des noms des adolescents
# teenagers = ["miko", "uriel", "elsa", "eden", "lior"]

# #  Boucle pour demander lage de chaque adolescent
# for name in teenagers[:]:  # jutilise [:] pour pas modifier la liste pendant quelle se repete
#      age = int(input(f"how old is {name} ? "))
    
#      # Verifie si ladolescent peut voir le film
#      if 16 <= age <= 21:
#          print(f"{name} cannot watch this movie. will be delete from the list")
#          teenagers.remove(name)  # Retire ladolescent de la liste

# # Affiche la liste finale des adolescents qui peuvent voir le film
# print("\nfinal list of teenagers who can watch this movie :")
# print(teenagers)





# exercice10:

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# while 'Pastrami sandwich' in sandwich_orders:                         
#      sandwich_orders.remove('Pastrami sandwich')    
# #     print(sandwich_orders)   tant que ya des pastrami dans order -- je veux les supprimer (commande .remove)

# finished_sandwiches = []

# while sandwich_orders:                                   
#     finished_sandwiches.append(sandwich_orders.pop(0)) 
#     # print(finished_sandwiches)               tant que je suis dans orders je veux ajouter tous mes sandwiches un part un dans finished
#     for sandwich in finished_sandwiches:
#      print(f'i made your {sandwich.lower()}')
    



#     in exercice 10 i dont understand why but when i print (line 308) it prints every sentence more than once 