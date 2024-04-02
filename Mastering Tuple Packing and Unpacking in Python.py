#Question 1
#Task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def display(orders):
    for order in orders:
        name, product, quantity= order
        print(f"Customer {name} ordered {quantity} {product}(s).")

display(orders)

#Task 2

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Adam", "adam@email.com", "345-678-9012")
    # More contacts...
]

def filter_by_name(contacts, initial):
    print(f"Displaying the contacts that begin with the letter {initial.upper()} in the contacts list.")
    for contact in sorted(contacts):
        if contact[0][0] == initial.upper():
            print(contact)
        

filter_by_name(contacts, 'a')