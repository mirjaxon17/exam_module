from base import Base


class Basic():
    @staticmethod
    def select (table):
        query = f"""SELECT * FROM  {table}"""
        return Base.connect(query,"select")

    @staticmethod
    def update (query):
        return Base.connect(query,"update")

    @staticmethod
    def delete (collumn,name,table):
        query = f"""DELETE FROM  {table} WHERE {collumn}"= '{name}'"""
        return Base.connect(query,"delete")

class Country(Basic):
    def __init__(self,name,create_date):
        self.name = name
        self.create_date = create_date
    @staticmethod
    def select (table):
        query = f"""SELECT * FROM  {table}"""
        return Base.connect(query,"select")

    @staticmethod
    def update (query):
        return Base.connect(query,"update")

    @staticmethod
    def delete (collumn,name,table):
        query = f"""DELETE FROM  {table} WHERE {collumn}"= '{name}'"""
        return Base.connect(query,"delete")

    def insert(self,table):
        query = f"""INSERT INTO  {table:"country"} (name,create_date) VALUES ('{self.name}','{self.create_date}')"""
        return Base.connect(query, "insert")

class City(Country):
    def __init__(self,country_id,name,create_date):
        super().__init__(name,create_date)
        self.country_id = country_id

    def insert(self, table):
        query = f"""INSERT INTO  {table:"city"} (country_id,name,create_date) VALUES ('{self.country_id}','{self.name}','{self.create_date}')"""
        return Base.connect(query, "insert")


class Adress(Country):
    def __init__(self,city_id,name,create_date):
        super().__init__(name,create_date)
        self.city_id = city_id

    def insert(self,table):
        query = f"""INSERT INTO  {table:"adress"} (city_id,name,create_date) VALUES ('{self.city_id}','{self.name}','{self.create_date}')"""
        return Base.connect(query, "insert")

class Punkt(Country):
    def __init(self,name,adress_id,create_date):
        super().__init(name,create_date)
        self.adress_id = adress_id

    def insert(self, table):
        query = f"""INSERT INTO  {table:"punkt"} (adress_id,name,create_date) VALUES ('{self.adress_id}','{self.name}','{self.create_date}')"""
        return Base.connect(query, "insert")

class Store(Basic):
    def __init(self,name,adress_id,create_date):
        self.name = name
        self.adress_id = adress_id
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO  {table:"store"} (name,adress_id,create_date) VALUES ('{self.name}','{self.adress_id}','{self.create_date}')"""
        return Base.connect(query, "insert")



class Product(Basic):
    def __init__(self,name,description,store_id,price,create_date):
        self.name = name
        self.description = description
        self.store_id= store_id
        self.price = price
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO  {table:"product"} (name,description,store_id,pricecreate_date) VALUES ('{self.name}','{self.description}','{self.store_id}','{self.price}','{self.create_date}')"""
        return Base.connect(query, "insert")


class Customer(Basic):
    def __init__(self,adress_id,product_id,first_name,last_name,user_name,password,create_date):
        self.adress_id = adress_id
        self.product_id = product_id
        self.first_name = first_name
        self.last_name =last_name
        self.user_name = user_name
        self.password = password
        self.create_date = create_date

    def insert(self, table):
        query = f"""INSERT INTO  {table:"customer"} (adress_id,product_id,first_name,last_name,user_name,password,create_date) VALUES ('{self.adress_id}','{self.product_id}','{self.store_id}','{self.price}','{self.create_date}')"""
        return Base.connect(query, "insert")


class PaymentType(Basic):
    def __init__(self,name):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO  {table:"payment_type"} (name) VALUES ('{self.name}')"""
        return Base.connect(query, "insert")


class Payment(Basic):
    def __init__(self,payment_type_id,product_id,customer_id):
        self.payment_type_id = payment_type_id
        self.product_id = product_id
        self.customer_id = customer_id

    def insert(self, table):
        query = f"""INSERT INTO  {table:"payment"} (payment_type_id,product_id,customer_id) VALUES ('{self.payment_type_id}','{self.product_id}','{self.customer_id}')"""
        return Base.connect(query, "insert")


class Delivery(Basic):
    def __init__(self,product_id,customer_id,adress_id):
        self.product_id = product_id
        self.customer_id = customer_id
        self.adress_id = adress_id

    def insert(self, table):
        query = f"""INSERT INTO  {table:"delivery"} (product_id,customer_id) VALUES ('{self.product_id}','{self.customer_id}')"""
        return Base.connect(query, "insert")








