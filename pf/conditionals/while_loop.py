
inventory = 10
request = 3
original_inventory = 10 

print(f"Starting inventory: {inventory} units.")
print(f"Processing request for {request} units.")

while True:
    inventory = inventory - request 
    print(f"{request} unit processed.")
    
    if inventory == (original_inventory - request):
        print(f"Request of {request} units fulfilled.")
    print(f"Final inventory: {inventory} units.")
    break  
# ----------------------------------------------------------------------------------------------------------------------------------
age = 0
while age < 0:
    print("Invalid age. Please enter a valid age.")
    age = int(input("Enter patient your age: "))
    print("Age is recorded")