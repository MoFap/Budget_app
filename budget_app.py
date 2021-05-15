class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} in {} category".format(amount, self.category)

    def check_balance(self):
        return "Your current balance in {} category is {}".format(self.category,self.amount)

    def transfer(self, amount, trf_category):
        if self.amount < amount:
            print("Insufficient funds")
            return False
        else:
            self.amount -= amount
            trf_category.amount += amount
            return True




food_category = Category("food", 1000)
clothing_category = Category("clothing", 2000)
car_repair_category = Category("car repair", 3000)
utilities_category = Category("utilities", 4000)
phone_bill_category = Category("phone bill", 5000)


print(food_category.deposit(1000))
print(food_category.transfer(500, utilities_category))

print(food_category.check_balance())
print(utilities_category.check_balance())
