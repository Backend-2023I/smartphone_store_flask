from tinydb import TinyDB, Query


class SmartphoneDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
    
    def brands(self):
        """Returns all brands in the database"""
        tables = self.db.tables()
        return tables
        
    def all_smartphone(self, brands):
        phones = []
        for brand in brands:
            table = self.db.table(brand)
            phones.extend(table.all())
        return phones
    
    def get_smartphone_by_brand(self, brand):
        """Returns all products by brand"""
        table = self.db.table(brand)
        return table.all()
    
    def get_smartphone_by_name(self, brand, name):
        """Returns a product by name"""

        User = Query()
        table = self.db.table(brand)

        return table.search(User.name == name)

    def get_smartphone_by_price(self, price):
        """Returns a product by price"""
        pass
    
    def add_smartphone(self, smartphone, brand):
        """Adds a product to the database"""
        pass
    
    def delete_smartphone(self, doc_id, brand):
        """Deletes a product from the database"""
        pass
    
