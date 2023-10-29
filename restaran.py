

class Resturant:
    """Resturant classi"""

    def __init__(self,name,menu):
        self._name = name
        self.menu = menu

        self.tables = [1,2,3,4,7,8,9]
        self.booked_tables = dict()

    def set_free_table(self,a):
        self.tables.remove(a)
    def set_booked_table(self,a,b):
        self.booked_tables[a] = b
    def get_free_tables(self):
        return  self.tables
    def get_booked_tables(self):
        return  self.booked_tables.items()



    def get_menu(self):
        return  self.menu.show_menu()

    def get_name(self):
        return self._name


