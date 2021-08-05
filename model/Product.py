from model.Model import Model

'''
 Product collection model
'''
class Product(Model):

    def __init__(self):
        super().__init__()
        self.collection = self.db.products

    def insertProduct(self, item):
        return self.collection.insert(item)


    def insertManyProduct(self, collections):
        return self.collection.insert(collections)
