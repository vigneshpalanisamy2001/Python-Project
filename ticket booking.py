import random
while True:
    print("1. Chennai To Bangalore")
    print("2. Chennai To Salem")
    print("3. Chennai To Coimbatore")
    print("4. Chennai to Trichy")
    print("5. Chennai to Attur")
    try:
        destination = int(input("Enter your destination number: "))
        if destination <=5 :
            print("You have chosen your destination.")
            break
        else:
            print("Please choose a valid destination number (1-5).")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Step 2: Bus Timing Selection
while True:
    print("Bus Timing")
    print("1. 6:00 AM to 9:00 AM")
    print("2. 10:00 AM to 1:00 PM")
    print("3. 2:00 PM to 4:00 PM")
    try:
        timing = int(input("Choose your bus timing: "))
        if timing <= 3:
            print("Bus timing chosen.")
            break
        else:
            print("Please choose a valid timing option (1-3).")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Step 3: Seat Type Selection
while True:
    print("Choice of Seat Type")
    print("1. AC")
    print("2. Non AC")
    print("3. Sleeper")
    try:
        seat_type = int(input("Enter the seat type number: "))
        if seat_type <=3:
            print("Seat type chosen.")
            break
        else:
            print("Please choose a valid seat type option (1-3).")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Step 4: Bus Service Selection
while True:
    print("Available Travel Bus Services")
    print("1. SVT Bus Service")
    print("2. Jayalakshmi Bus Service")
    print("3. NT Bus Service")
    print("4. MRR Bus Service")
    try:
        bus_service = int(input("Enter your bus service number: "))
        if bus_service <= 4:
            print("Bus service chosen.")
            break
        else:
            print("Please choose a valid bus service option (1-4).")
    except ValueError:
       print("Invalid input. Please enter a number.")

# Step 5: Seat Number Selection
while True:
    try:
        seat_number = int(input("Enter your seat number (1-10): "))
        if seat_number <=10:
            print("Seat number chosen.")
            break
        else:
            print("Please choose a seat number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Step 6: User Details Input
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")

# Step 7: OTP Generation and Verification
otp = random.randint(1000, 9999)
print("Your OTP is:", otp)

while True:
    try:
        entered_otp = int(input("Please enter the OTP: "))
        if entered_otp == otp:
            print(f"Successful booking! Happy journey, {name}!")
            print("Thank you! Visit again.")
            break
        else:
            print("Invalid OTP. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
