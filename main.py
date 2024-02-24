
from base import Base
from classes import Basic,Country,City,Adress,Punkt,Store,Product,Customer,PaymentType,Payment,Delivery





def Service_Country():
    enter = input("""
    enter service
    1.Select
    2.Insert
    3.Delete
    4.Update
    0.Back 
    >>>>>
    """)
    if enter == "1":
        for i in Country.select('user'):
            print(i)
            return Service_Country()

    elif enter == "2":
        name = input("Enter name of user: ")
        create_date = input("Enter password: ")
        user = Country(name, create_date)
        print(user.insert("user"))
        return Service_Country()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "users_id":
            print(Country.delete(column, data, "country"))
        else:
            print(Country.delete_id(column, data, "country"))
        return Service_Country()

    elif enter == '4':
        name = input("Enter name of country:New ")
        id = int(input("Enter old name country"))
        query = f"""UPDATE user SET name='{name}' WHERE country_id='{id}';"""
        print(country.update(query))
        return Service_Country()

    elif enter == '0':
        return main()


def Service_City():
    enter = input("""
      enter service
      1.Select
      2.Insert
      3.Delete
      4.Update
      0.Back
      >>>>>""")
    if enter == "1":
        for i in City.select('city'):
            print(i)
            return Service_City()
    elif enter == "2":
        country_id = input("Enter country_id: ")
        name = input("Enter name")
        create_date = input("Enter create_date: ")
        city = City(country_id ,name ,create_date)
        print(city.insert("city"))
        return Service_City()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "student_id":
            print(City.delete(column, data, "city"))
        else:
            print(City.delete_id(column, data, "city"))
        return Service_City()

    elif enter == '4':
        city = input("Enter name of New city ")
        id = int(input("Enter old name city"))
        query = f"""UPDATE user SET name='{city}' WHERE city_id='{id}';"""
        print(city.update(query))
        return Service_City()

    elif enter == '0':
        return main()



def Service_Adress():
    enter = input("""
        enter service
        1.Select
        2.Insert
        3.Delete
        4.Update
        0.Back
        >>>>>""")
    if enter == "1":
        for i in Adress.select('adress'):
            print(i)
            return Service_Adress()

    elif enter == "2":
        city_id = input("Enter city_id: ")
        name = input("Enter name: ")
        create_date = input("Enter create_date")
        adress = Adress(city_id, name, create_date)
        print(adress.insert("adress"))
        return Service_Adress()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "adress_id":
            print(Adress.delete(column, data, "adress"))
        else:
            print(Adress.delete_id(column, data, "adress"))
        return Service_Adress()

    elif enter == '4':
        adress   = input("Enter name adress ")
        id = int(input("Enter old name adress"))
        query = f"""UPDATE user SET name='{adress}' WHERE adress_id='{id}';"""
        print(adress.update(query))
        return Service_Adress()

    elif enter == '0':
        return main()

def Service_Punkt():
    enter = input("""
            enter service
            1.Select
            2.Insert
            3.Delete
            4.Update
            0.Back
            >>>>>""")
    if enter == "1":
        for i in Punkt.select('punkt'):
            print(i)
            return Service_Punkt()

    elif enter == "2":
        name = input("Enter name: ")
        adress_id = input("Enter adress_id: ")
        create_date = input("Enter create_date")
        punkt= Punkt(name, adress_id, create_date)
        print(punkt.insert("punkt"))
        return Service_Punkt()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "Punkt_id":
            print(Punkt.delete(column, data, "punkt"))
        else:
            print(Punkt.delete_id(column, data, "punkt"))
        return Service_Punkt()

    elif enter == '4':
        punkt = input("Enter name Punkt ")
        id = int(input("Enter old name Punkt"))
        query = f"""UPDATE user SET name='{punkt}' WHERE punkt_id='{id}';"""
        print(punkt.update(query))
        return Service_Punkt()

    elif enter == '0':
        return main()


def Service_Store():
    enter = input("""
             enter service
             1.Select
             2.Insert
             3.Delete
             4.Update
             0.Back
             >>>>>""")
    if enter == "1":
        for i in Store.select('store'):
            print(i)
            return Service_Store()

    elif enter == "2":
        name = input("Enter name: ")
        adress_id = input("Enter adress_id: ")
        create_date = input("Enter create_date")
        store = Store(name, adress_id, create_date)
        print(store.insert("menthor"))
        return Service_Store()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "Menthor_id":
            print(Store.delete(column, data, "menthor"))
        else:
            print(Store.delete_id(column, data, "Store"))
        return Service_Store()

    elif enter == '4':
        store = input("Enter name Store ")
        id = int(input("Enter old name store"))
        query = f"""UPDATE user SET name='{store}' WHERE store_id='{id}';"""
        print(store.update(query))
        return Service_Store()

    elif enter == '0':
        return main()


def Service_Product():
    enter = input("""
               enter service
               1.Select
               2.Insert
               3.Delete
               4.Update
               0.Back
               >>>>>""")
    if enter == "1":
        for i in Product.select('product'):
            print(i)
            return Service_Product()

    elif enter == "2":
        name = input("Enter name: ")
        description = input("Enter description: ")
        store_id = input("Enter store_id")
        price = input("Enter price: ")
        create_date = input("Enter create_date")
        product = Product(name, description, store_id, price, create_date)
        print(product.insert("product"))
        return Service_Product()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "Product_id":
            print(Product.delete(column, data, "product"))
        else:
            print(Product.delete_id(column, data, "product"))
        return Service_Product()

    elif enter == '4':
        product = input("Enter name product ")
        id = int(input("Enter old name product"))
        query = f"""UPDATE user SET name='{product}' WHERE product_id='{id}';"""
        print(product.update(query))
        return Service_Product()

    elif enter == '0':
        return main()


def Service_Customer():
    enter = input("""
                   enter service
                   1.Select
                   2.Insert
                   3.Delete
                   4.Update
                   0.Back
                   >>>>>""")
    if enter == "1":
        for i in Customer.select("customer"):
            print(i)
            return Service_Customer()

    elif enter == "2":
        adress_id = input("Enter cadress_id: ")
        product_id = input("Enter product_id")
        first_name = input("Enter firt_name")
        last_name =  input("Enter last_name")
        user_name =  input("Enter user_name")
        password = input("Enter password")
        create_date = input("Enter create_date")

        customer = Customer(adress_id,product_id,first_name,last_name,user_name,password,create_date)
        print(customer.insert("customer"))
        return Service_Customer()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "Customer_id":
            print(Customer.delete(column, data, "customer"))
        else:
            print(Customer.delete_id(column, data, "customer"))
        return Service_Customer()

    elif enter == '4':
        customer = input("Enter name customer ")
        id = int(input("Enter old name customer"))
        query = f"""UPDATE user SET name='{customer}' WHERE customer_id='{id}';"""
        print(customer.update(query))
        return Service_Customer()

    elif enter == '0':
        return main()


def Service_Payment_type():
    enter = input("""
                    enter service
                    1.Select
                    2.Insert
                    3.Delete
                    4.Update
                    0.Back
                    >>>>>""")
    if enter == "1":
        for i in PaymentType.select('payment_type'):
            print(i)
            return Service_Payment_type()

    elif enter == "2":
        name = input("Enter name: ")
        payment_type = PaymentType(name)
        print(payment_type.insert("payment_type"))
        return Service_Payment_type()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "Payment_Type":
            print(PaymentType.delete(column, data, "payment_type"))
        else:
            print(PaymentType.delete_id(column, data, "payment_type"))
        return Service_Payment_type()

    elif enter == '4':
        payment_type = input("Enter name payment_type ")
        id = int(input("Enter old name payment_type"))
        query = f"""UPDATE user SET name='{payment_type}' WHERE payment_type_id='{id}';"""
        print(payment_type.update(query))
        return Service_Payment_type()

    elif enter == '0':
        return main()


def Service_Payment():
    enter = input("""
                     enter service
                     1.Select
                     2.Insert
                     3.Delete
                     4.Update
                     0.Back
                     >>>>>""")
    if enter == "1":
        for i in Payment.select('payment'):
            print(i)
            return Service_Payment()

    elif enter == "2":
        payment_type_id = input("Enter payment_type id: ")
        product_id = input("Enter product_id")
        customer_id = input("Enter customer_id")
        payment = Payment(payment_type_id, product_id, customer_id)
        print(payment.insert("payment"))
        return Service_Payment()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "Payment":
            print(Payment.delete(column, data, "payment"))
        else:
            print(Payment.delete_id(column, data, "payment"))
        return Service_Payment()

    elif enter == '4':
        payment = input("Enter name payment ")
        id = int(input("Enter old name payment"))
        query = f"""UPDATE user SET name='{payment}' WHERE payment_id='{id}';"""
        print(payment.update(query))
        return Service_Payment()

    elif enter == '0':
        return main()


def Service_Delivery():
    enter = input("""
                       enter service
                       1.Select
                       2.Insert
                       3.Delete
                       4.Update
                       0.Back
                       >>>>>""")
    if enter == "1":
        for i in Delivery.select('delivery'):
            print(i)
            return Service_Delivery()

    elif enter == "2":
        product_id = input("Enter product_id: ")
        customer_id = input("Enter customer_id")
        adress_id = input("Enter adress_id")
        delivery = Delivery(product_id, customer_id, adress_id)
        print(delivery.insert("delivery"))
        return Service_Delivery()

    elif enter == '3':
        column = input("Enter column name")
        data = input("Enter data")
        if column != "delivery_id":
            print(Delivery.delete(column, data, "delivery"))
        else:
            print(Delivery.delete_id(column, data, "delivery"))
        return Service_Delivery()

    elif enter == '4':
        delivery = input("Enter name delivery ")
        id = int(input("Enter old name delivery"))
        query = f"""UPDATE user SET name='{delivery}' WHERE delivery_id='{id}';"""
        print(delivery.update(query))
        return Service_Delivery()

    elif enter == '0':
        return main()


def main():
    enter = input("""Enter Table

    1.Country
    2.City
    3.Adress
    4.Punkt
    5.Store
    6.Product
    7.Customer
    8.Payment_type
    9 Payment
    10.Delivery
        >>>>>>
        """
                  )

    if enter == "1":
        return Service_Country()
    if enter == "2":
        return Service_City()
    if enter == "3":
        return Service_Adress()
    if enter == "4":
        return Service_Punkt()
    if enter == "5":
        return Service_Store()
    if enter == "6":
        retunr = Service_Product()
    if enter == "7":
        return Service_Customer()
    if enter == "8":
        return Service_Payment_type()
    if enter == "9":
        return Service_Payment()
    if enter == "10":
        return Service_Delivery()




if __name__ == '__main__':
    main