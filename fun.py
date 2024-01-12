
def carre(nombre):
  
    return nombre ** 2

def est_pair(nombre):
    """Vérifie si un nombre est pair."""
    return nombre % 2 == 0

def somme_carres_nombres_pairs(liste):
    """Calcule la somme des carrés des nombres pairs dans une liste."""
    try:
        carres_nombres_pairs = [carre(x) for x in liste if est_pair(x)]
        return sum(carres_nombres_pairs)
    except TypeError:
        print("La liste doit contenir uniquement des nombres.")
        return None

