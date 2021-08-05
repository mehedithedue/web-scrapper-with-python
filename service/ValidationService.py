class ValidationService:

    def productValidate(self, productData):
        '''
         to check validation of product data before
         insert to the  db
        '''
        for element in productData:
            if (element.get('product') is None) or (element.get('amount') is None):
                raise ValueError(" Validation Error, product and amount must be present")
            if not isinstance(element.get('amount'), int):
                raise ValueError(" Validation Error, amount must be integer")
