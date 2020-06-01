from game_elements.position import Position
from config.settings import item_to_collect_names



class ItemToCollect(Position):

    #recupere la liste des noms des objets à collecter
    names = item_to_collect_names
    #trie dans l'ordre alphabetique
    names.sort()
    index = 0
    #dictionaire pour stocker la position en clée et
    #   le nom en valeur de chaque Objets à collecter
    dict ={}

    def __init__(self, items_to_collects_positions):

        for positions in items_to_collects_positions:
            x, y = positions
            Position.__init__(self, x, y)
            #recupere le nom de l'objet
            self.name = ItemToCollect.names[ItemToCollect.index]
            #ajoute au dictionaire la position et le nom
            ItemToCollect.dict[self.position] = self.name
            #incremante l'index pour le prochain objet
            ItemToCollect.index += 1
