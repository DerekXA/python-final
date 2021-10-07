#load the data, get the list of products
from os import name


def load_data(path):
    list = []
    with open(path,'r') as data:
        for line in data: 
            info = line.split(',')
            list.append(info)
    return list

products = load_data("./products.txt")


# search with name of product, make sure product = product name, find and return as a dictionary
def product_search (name):

    for product in products:
        if name in product [1].lower():
            return{
                "price" : float(product[2]),
                "quantity" : float(product[3]), 
                #"total" : product([2][3]) 
            }
        #elif start_search == True:
            #search_again()
    return {
        "error": 'product not found'
    }
       


# check and display the error 
def display_product(product):
    if 'error' in product:
        print(product['error'])
        return

    # print(f"price: {product['price']}")
    # print(f"quantity:{product['quantity']} ")
    # print(f"Total: ${float(product[2])*float(product[3])}")
    print(f'Price: {product["price"]} Quantity: {product["quantity"]} Total: {product["price"] * product["quantity"]}')

# ask for product name, call on product_search for results, show results
product = input('enter product name: ').lower()
result = product_search(product)
display_product(result)

# def search_again():
#     search = input('search again, y/n')
#     if search == 'y':
#         start_search()
#     else: return

# def start_search(product_name): 
#     product_name = product_search()
# start_search()

