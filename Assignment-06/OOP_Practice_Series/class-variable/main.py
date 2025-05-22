class Bank:
    # Class variable (shared by all instances)
    bank_name = "Default Bank"

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def show_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Bank Name    : {Bank.bank_name}")

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"\nBank name changed to: {cls.bank_name}")

# Creating instances of the Bank class
customer1 = Bank("Alice")
customer2 = Bank("Bob")

# Showing initial details
print("=== Before Changing Bank Name ===")
customer1.show_details()
customer2.show_details()

# Changing bank name using class method
Bank.change_bank_name("Future Bank")

# Showing updated details
print("\n=== After Changing Bank Name ===")
customer1.show_details()
customer2.show_details()
