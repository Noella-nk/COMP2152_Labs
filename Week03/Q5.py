contacts = {
    "Alice": "123-456-7890", 
    "Bob": "234-567-8901", 
    "Charlie": "345-678-9012"
}
print("Alice's number:", contacts["Alice"])
contacts["Diana"] = "555-4342"
print(f"contacts after adding Diana: {contacts}")
contacts["Bob"] = "555-0000"
print(f" Contacts after updatingn Bob: {contacts}")
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")
print(f"All names {contacts.keys()}")
print(f"All numbers {contacts.values()}")
print(f"Total Contacts {len(contacts)}")