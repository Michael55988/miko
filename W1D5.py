# daily challenge



# number = int(input('enter a number'))
# lenght = int(input('enter a lenght'))

# multiplies = []

# for i in range(0,lenght+1):
#     multiplies.append(number * (i+1))
#     print('number:', number, '-', 'lenght', lenght,  '->')
#     print(multiplies)
    





# chalenge 2

string = input('enter a string')
new_string = ''
# ligne 25-- je cree une boucle for pour repeter mon code sur chaque caractere de string.    (len(string)) donne la longueur de mon string. et en rajoutant range ca le produit.
for i in range(len(string)):
    # ligne 27---     cela verifie si le caractere actuel [i] est different de son precedent [i-1]
   
    if i == 0 or string[i] != string[i-1]:
      #ligne 29---- ajoute le caractere actuel au nouveau string  
   
        new_string += string[i] 
        print('new string without double letters:', new_string)
       

