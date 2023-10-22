address_book = {
    'John': '123 Main St',
    'Alice': '456 Elm St',
    'Bob': '789 Oak St'
}

# Accessing an address:
name = 'Alice'
if name in address_book:
    address = address_book[name]
    print(f"{name}'s address is {address}")
else:
    print(f"{name} not found in the address book.")

# Adding a new entry:
new_name = 'Eve'
new_address = '101 Pine St'
address_book[new_name] = new_address

# Deleting an entry:
del address_book['John']
