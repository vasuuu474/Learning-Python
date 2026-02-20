class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def apply_discount(self, discount_amount):
        if discount_amount > 0:
            if discount_amount <= self.price:
                self.price -= discount_amount
            else:
                print("Discount amount cannot exceed the actual price.")
        else:
            print("Discount amount must be positive.")
    def display_mobile(self):
        print(f"""
            Brand: {self.brand}
            Model: {self.model}
            Price: ${self.price}""")
        

br_name = input("Enter Brand Name: ")
mod = int(input("Enter Model : "))
pr = float(input("Enter Mobile Price : "))
mobile1 = Mobile(br_name,mod,pr)
mobile1.display_mobile()

disc=float(input("Enter Discount Price : "))
mobile1.apply_discount(disc)
mobile1.display_mobile()