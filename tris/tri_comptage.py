def tri_comptage(tab: list, reverse=False) -> list:
  """
  Implémente le tri comptage sur une liste.

  Args:
    tab (list): Le tableau à trier.

  Retourne:
    (list): Nouveau tableau trié.
  """

  # Liste vide
  if not tab:
    return []
  
  # Trouver la plus grande valeur
  max_plus_un = max(tab) + 1

  # Calculer le tableau de fréquences
  frequences = [tab.count(i) for i in range(max_plus_un)]
  
  # Assembler le tableau trié
  sorted = []
  for i in range(max_plus_un):
    sorted.extend([i] * frequences[i])

  # Retourner dans le bon ordre
  if reverse:
      return sorted[::-1]
  else:
    return sorted


if __name__ == '__main__':

  # Tableau à trier
  tab = [1, 9, 2, 5, 3, 0]

  # Afficher avant le tri
  print(f'Avant le tri : {tab}')

  # Trier le tableau
  tab_trie = tri_comptage(tab)

  # Afficher après le tri
  print(f'Après le tri : {tab_trie}')
  
