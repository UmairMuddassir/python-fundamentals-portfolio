# Create a tuple (immutable)
log_entry = ("DON-001", "2024-01-15", "O-")

# Attempting to change it will cause a TypeError.
# Tuples are immutable, meaning their elements cannot be changed after creation.
# log_entry[2] = "O+"  # Uncommenting this line would raise an error

# Access and print the first element (ID)
print(f"Donation ID: {log_entry[0]}")