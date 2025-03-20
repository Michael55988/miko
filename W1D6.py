# exercices XP


# exercice 1

# keys = ['ten', 'twenty', 'thirty']
# values = [10, 20, 30]

# zipp = zip(keys, values)
# print(dict(zipp))             









# je cree un dictionnaire vide
# family = {}

# while True:
#     name = input("enter name (o'stop' to stop) : ")
#     if name.lower() == "stop":
#         break
#     age = int(input(f"enter age the of {name} : "))
#     family[name] = age

# # Calcul du cout total
# total_cost = 0

# for name, age in family.items():
#     if age < 3:
#         price = 0
#     elif 3 <= age <= 12:
#         price = 10
#     else:
#         price = 15

#     print(f"{name} must pay ${price}")
#     total_cost += price

# print(f"\ntotal cost for the family: ${total_cost}")















# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]
#     }
# }

# brand["number_stores"] = 2
# print(f"Zara's clients are people who buy clothes for {', '.join(brand['type_of_clothes'])}.")

# brand["country_creation"] = "Spain"
# if "international_competitors" in brand:
#     brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# print(brand.keys())
# more_on_zara = {
#     "creation_date": 1975,
#     "number_stores": 10000
# }
# brand.update(more_on_zara)
# print(brand["number_stores"])














# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# disney_users_A = {}
# for index, user in enumerate(users):
#     disney_users_A[user] = index

# print(disney_users_A)
# disney_users_B = {}
# for index, user in enumerate(users):
#     disney_users_B[index] = user

# print(disney_users_B)
# disney_users_C = {}
# sorted_users = sorted(users)  # Trie la liste par ordre alphabetique

# for index, user in enumerate(sorted_users):
#     disney_users_C[user] = index

# print(disney_users_C)
# disney_users_I = {}
# for index, user in enumerate(users):
#     if "i" in user.lower():
#         disney_users_I[user] = index

# print(disney_users_I)
# disney_users_MP = {}
# for index, user in enumerate(users):
#     if user[0].lower() in ['m', 'p']:
#         disney_users_MP[user] = index

# print(disney_users_MP)




























# daily challenge


# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

# word = input('enter a word:') 
# # le dict ligne 62 va contenir les lettre du mot choisi entant que 'key' et leurs position entant que 'value'  
# word_dict = {}       
# # len(word) donne la longueur du mot.  rang(len(word)) crer une boucle qui va parcourir chaque index(lettre) du mot 
# for i in range(len(word)):    
#     # word[i] cest la lettre a lemplacement i.  si la lettre existe deja dans word_dict on ajoute i (append(i))
#     if word[i] in word_dict:
#         word_dict[word[i]].append(i)
#         # si la lettre nexiste pas encore on cree un i
#     else:
#         word_dict[word[i]] = [i]

# print(word_dict)










