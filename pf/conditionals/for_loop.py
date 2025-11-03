donars = int(input("Enter number of donars: "))
for i in range(donars):
    print(f"Processing donar {i+1}")

# ----------------------------------------------------------------------------------------------------------------------------------

donor_list = ["A+", "O-", "B+", "O-", "AB+", "O-"]
for blood_type in donor_list:
    if blood_type == "O-":    
     print(" Universal donor found!")
     break
else:
    print("No Universal donor in the list.")
    