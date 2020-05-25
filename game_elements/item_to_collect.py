from position import Position



class ItemToCollect(Position):

    list = ['needle','tube','ether']
    list.sort()    #trie les elements de la liste dans l'ordre alphabetique
    list_index = 0

    def __init__(self, x, y, is_collectable): #pour ne pas pouvoir collecter un objet 2X
        Position.__init__(self, x, y)
        self.is_collectable = is_collectable
        self.name = ItemToCollect.list[ItemToCollect.list_index]
        ItemToCollect.list_index += 1

        self

    
    def is_no_longer_collectable(self):
        self.is_collectable = False
