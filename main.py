print("Hello SalihosCode")
name = "Saliha"
age = 25
une_liste = ["Salih", "Kadour", "Amar", 1, 2, 3545]
is_adult = age >= 18
# --------------------------------------------------------------------------------------------
if is_adult:
    print("Hello " + name + " Tu as " + str(age) + " ans " + "Majeure est : " + str(is_adult))
else:
    """
        * is_adult change en false automatiquement en False si age < 18
        * Pas la peine de mettre "not is_adult"
        * Jouer avec la variable age est vous verrez exple: age = 15
    """
    print("Hello " + name + " Tu as " + str(age) + " ans " + "Majeure est : " + str(is_adult))

# -----------------------------------------------------------------------------------------
print("Tu as les oives suivants avec : " + str(une_liste))
print(name.upper())
other_name = name.replace("S", "m").upper()

# Entoure "MALIHA par des * =====> **MALIHA**
# le premier chiffre représente le nbre total des * plus MALIHA (* + other_name)
print(other_name.center(10, "*"))
print("La longueur de other_name = 'MELIHA' est égal à : " + str(len(other_name)))
# -----------------------------------------------------------------------------------------
print("est ce que 'LIHA' est dans other_name ? " + str("LIHA" in other_name))
# -----------------------------------------------------------------------------------------
commentaire = """
Salut les copains
    Salut les loulous
        brefs c'est le Ramadhan
"""
print("le commentaire multiligne est égal à :")
print(commentaire)
# -----------------------------------------------------------------------------------------
# -----------Les F Strings ----------------------------------------------------------------
name = "Salih"
age = 56
email = f"""
        Hello {name} how are you?
        you are {age} years old.
        """
print("Ton message de mail : ")
print(email)
# -----------------------------------------------------------------------------------------
# -------------------------------LES COMPARAISONS  ----------------------------------------
print(14 >= 11)
print((14 != 11) and (10 <= 4) and ("A" == "a"))
print(not ((14 != 11) and (10 <= 4) and ("A" == "a")))
# -----------------------------------------------------------------------------------------
# -------LES AFFECTATIONS -----------------------------------------------------------------
brand = "Amigoscode"
print(brand)
# -----------------------------------------------------------------------------------------
# ------------------------------FLOW CONTROL ----------------------------------------------
number = int(input("Donner votre variable à evaluer :"))
if number > 0:
    print(f"la variable number = {number} est positive.")
elif number == 0:
    print(f"la variable number = {number} est nulle")
else:
    print(f"la variable number = {number} est négative")
# ------------------------------Autre Méthode térnaire ------------------------------------
number = int(input("Donner votre variable à evaluer :"))
message = "Positive" if number > 0 else "0 ou négative"
print(f"la variable number est:  {message}")
# ----------------------------LES LISTES ---------------------------------------------------
liste = [14, 7, 31, 0, -12, 63, -10]
liste.sort()
print(liste.sort())  # ======> Retourne None, il faut faire un print sur "liste"
print(f"La liste triée est : {liste}")
print(f"La liste triée à l'envers est : {liste.reverse()}")

liste.append(1000)
print(f"La liste avec 1000 ajouté est :{liste}")
print(liste.sort())  # ======> Retourne None, il faut faire un print sur "liste"
print(f"La liste triée est : {liste}")
print(f"La longueur de la liste est: {len(liste)}")

liste.extend([20, 21, 30])  # Rajoute des elts à liste impérativement entre crochets []
print(f"La liste étendue est : {liste}")

liste.remove(1000)
print(f"La liste sans 1000 est : {liste}")
del liste[2]  # Supprime un elt de la liste à l'index liste[n]
print(f"la liste sans le troisème elt est : {liste}")
del liste[0: 2]  # Suprime les deux premiers elts ======> [-12, -10, 7, 14, 31, 63, 20, 21, 30]
# ======================================================> [7, 14, 31, 63, 20, 21, 30]
print(f"La liste sans les 2 premiers elts : {liste}")

print(liste)
variable = liste.pop()  # pop() suprime le dernier elt de la liste
print(f"la liste sans la dernière valeur {variable} est : {liste}")
print(f"La liste sans 1000 est : {liste}")

liste.clear()  # efface toute la liste
print(f"La liste est vide : {liste}")

liste = [-12, -10, 0, 7, 14, 31, 63, 20, 21, 30, 1000]
message = "vrai" if 35 in liste else "faux"  # ======> Condition ternaire
print(f"est ce que 25 est dans la liste ? : {message}")

# -------------------------Les SETS ------------------------------------------------------------
number_set = {1, 1, 2, 3, 7, 0}
print(f"Le set est égal à : {number_set}")  # Ne permet pas la duplication des elts ====> {0, 1, 2, 3, 7}

lettersA = {"A", "B", "C", "F", "K", "X"}
lettersB = {"K", "B", "E", "T", "Y"}

union = lettersA | lettersB  # =======> {'T', 'E', 'K', 'X', 'Y', 'A', 'C', 'F', 'B'}
print(f"L'union égal à : {union}")  # Dans le désordre, l'ordre n'est pas garantie
intersection = lettersA & lettersB  # =====> {'B', 'K'}
print(f"L'intersection égal à : {intersection}")  # Dans le désordre, l'ordre n'est pas garantie
difference = lettersA - lettersB  # ======> {'C', 'F', 'A', 'X'}
print(f"La différence est égal à : {difference}")  # Dans le désordre, l'ordre n'est pas garantie

# ------------------------LES DICTIONNAIRES --------------------------------------------------------
personne = {
    "nom": "Salih",
    "age": 56,
    "adresse": "Veneux les sablons"
}
print(f"la personne est : {personne}")
age = personne["age"]
print(f"L'age de la personne est : {age}")

print(f"Les clés de ce dictionnaires : {personne.keys()}")  # Les clés du dict
print(f"Les Valeurs de ce dictionnaires : {personne.values()}")  # ====> [Salih', 56, 'Veneux les sablons']

list_personne = list(personne)  # ====> ['nom', 'age', 'adresse'] , donne que la liste des clés mais pas les Valeurs
print(f"Transformation dict ==> liste : {list_personne}")

items = personne.items()  # Donne une liste de tuple ===> (key , value) du dictionnaires
# ========================> [('nom', 'Salih'), ('age', 56), ('adresse', 'Veneux les sablons')]
# personne.clear() ===> supprime le dictionnaire

personne["age"] = 100
print(f"la liste aprés changement d'age est  : {personne}")
age_changed = personne.get("age")  # donne l'age d'une autre manière  <====> age_changed = personne["age"]
print(f"la liste aprés changement d'age est  : {age_changed}")

