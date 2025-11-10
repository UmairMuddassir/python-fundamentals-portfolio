# Create the initial dictionary
donor_profile = {
    "name": "Ahmed",
    "age": 25,
    "blood_type": "B+"
}

# Add a new key-value pair
donor_profile["last_donation_date"] = "2023-10-20"

# Access and print the blood type
print(f"Donor Blood Type: {donor_profile['blood_type']}")

# Update the age
donor_profile["age"] = 26

# Print the entire dictionary
print(f"Full Profile: {donor_profile}")