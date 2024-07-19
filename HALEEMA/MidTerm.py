       # Welcome User
userName=input("Please Enter Your Name")
welcomeMessage=f"Welcome to BanoQabil Store{userName}"
lenWCMsg=len(welcomeMessage)
print("-"*lenWCMsg)
print(welcomeMessage)
print("-"*lenWCMsg)

   # Shopping cart program
products = []
prices = []
total = 0

while True:
    product = input("Enter a product to buy (q to quit): ")
    if product.lower() =="q":
        break
    else:
        price = int(input(f"Enter the price of a {product}: RS "))
        products.append(product)
        prices.append(price)

print("----- YOUR CART -----")

for product in products:
    print(product, end=" ")
    for price in prices:
        total+=price
        print()
        print(f"Your total is: RS{total}")

print("Thank you for buying from us, we look forward to having you another time")