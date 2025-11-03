#Create a dictionary where product names are keys and prices are values.

#1.Use get() to print the price of a product entered by the user.
#2.Add a new product using setdefault().
#3.Remove the last inserted product using popitem().
#4.Show all items using items().
products = { }
n = int(input("Enter the number of products do you want: "))
for i in range(n):
    key =input(f"enter product {i+1}: ")
    value = float(input(f"Enter price of the {key}: "))
    products[key] = value
print("original products: ",products)
get = input("Enter the product name to get the price: ")
to_get = products.get(get,"product not found")
print(f"prince of {get}: ",to_get)
new_key = input("Enter new product: ")
new_value = float(input(f"Enter {new_key} price: "))
products.setdefault(new_key,new_value)
print("New product added dict: ",products)
products.popitem()
print("\nAll products after removing last inserted element: ")
for product,price in products.items():
    print(product," : ",price)