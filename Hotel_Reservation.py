import os
import time
from datetime import datetime
import random

def tryparse(value):
    try:
        return int (value)
    except ValueError:
        return None
   
def confirmloop(prompt):
    while True:
        confirm = input(prompt)

        if len(confirm) == 1 and confirm in ("Y", "y"):
            return True
        elif len(confirm) == 1 and confirm in ("N", "n"):
            return False
        else:
            print("Invalid input. Please enter only Y or N (no spaces).")
            
def generate_reservationID():
    while True: 
        ResID = random.randint(100,999)
        if ResID not in bookings:
            return ResID
        
Hotelroom = {
    1: {"Room Name": "Regular", "Rate": 150 },
    2: {"Room Name": "Deluxe", "Rate": 250},
    3: {"Room Name": "Suite", "Rate": 400}

}

bookings = {}

def hotelreservation():
    os.system('cls')

    print("=== HOTEL'S AVAILABLE ROOMS (Per Hour) ===")
    for num, info in Hotelroom.items():
        print(f"{num}. {info['Room Name']} - ₱{info['Rate']}/hr")
    print("0. Cancel and go back")

    while True:
        roomchoice = tryparse(input("Choose Room (1-3, 0 to cancel): "))
        if roomchoice == 0:
            return
        if roomchoice in Hotelroom:
            break
        print("Invalid Room. Try again...")

    while True:
        hour = tryparse(input("Enter number of hours (0 to cancel): "))
        if hour == 0:
            return
        if hour and hour > 0:
            break
        print("Invalid Hours. Try again...")

    roomname = Hotelroom[roomchoice]["Room Name"]
    rate = Hotelroom[roomchoice]["Rate"]
    total = rate * hour

    print(f"""
=== BOOKING RESERVATION SUMMARY ===
Room Type   : {roomname}
Hours       : {hour}
Rate/hr     : ₱{rate}
Total       : ₱{total}
""")

    if confirmloop("Confirm booking? (Y/N): "):
        ResID = generate_reservationID()
        bookings[ResID] = {
            "Room Type": roomname,
            "Hours": hour,
            "Rate per hour": rate,
            "Total Price": total,
            "Booking time": datetime.now().strftime("%Y-%m-%d %I:%M %p")
        }
        print("Booking Confirmed")
    else:
        print("Booking Cancelled")

    time.sleep(2)
            
def adminpanel():
    while True:
        os.system('cls')
        print("=== ADMIN HOTEL CONTROL ===")
        print("1. View bookings")
        print("2. Cancel booking")
        print("3. Update booking")
        print("4. Edit room")
        print("0. Back")

        choice = tryparse(input("> "))

        if choice == 0:
            return
        elif choice == 1:
            viewbooking()
        elif choice == 2:
            cancelbooking()
        elif choice == 3:
            updatebooking()
        elif choice == 4:
            editroom()
        else:
            print("Invalid choice.")
            time.sleep(1)

#View booking
def viewbooking():
    os.system('cls')
    if not bookings:
        print("No booking reservation found.")
        time.sleep(1)
        return

    print("=== ALL BOOKINGS ===")
    for ResID, info in bookings.items():
        print(
            f"Booking ID: {ResID} | "
            f"Room: {info['Room Type']} | "
            f"Hours: {info['Hours']} | "
            f"Total: ₱{info['Total Price']} | "
            f"Time: {info['Booking time']}"
        )

    input("\nPress Enter to continue...")

#Cancel booking
def cancelbooking():
    viewbooking()
    ResID = tryparse(input("> Enter Booking ID to cancel: "))

    if ResID not in bookings:
        print("Booking ID not found.")
        time.sleep(1)
        return

    if confirmloop("Are you sure you want to cancel the booking? (Y/N)"):
        del bookings[ResID]
        print("Booking cancelled.")
    else:
        print("Cancellation aborted.")

    time.sleep(1)

#Booking update - kung gusto baguhin ng user or yung nag reserve yung room na pinareserve niya.
def updatebooking():
    viewbooking()
    ResID = tryparse(input("> Enter Booking ID to update: "))

    if ResID not in bookings:
        print("Booking ID not found.")
        time.sleep(1)
        return

    booking = bookings[ResID]

    print("Select new room type (or 0 to keep current):")
    for num, info in Hotelroom.items():
        print(f"{num}. {info['Room Name']} - ₱{info['Rate']}/hr")

    newroom = tryparse(input("> "))
    if newroom in Hotelroom:
        booking["Room Type"] = Hotelroom[newroom]["Room Name"]
        booking["Rate per hour"] = Hotelroom[newroom]["Rate"]

    newhours = tryparse(input(f"Enter new hours (current {booking['Hours']}, 0 to keep): "))
    if newhours and newhours > 0:
        booking["Hours"] = newhours

    booking["Total Price"] = booking["Hours"] * booking["Rate per hour"]
    bookings[ResID] = booking

    print("Booking updated successfully.")
    time.sleep(2)

#Edit rooms kapag gusto ng admin or ng hotel palitan yung room and prices ng mga rooms
def editroom():
    while True:
        os.system('cls')
        print("=== EDIT / ADD ROOM TYPES ===")
        for num, info in Hotelroom.items():
            print(f"{num}. {info['Room Name']} - ₱{info['Rate']}/hr")
        print("0. Back")

        choice = tryparse(input("> "))

        if choice == 0:
            return
        elif choice in Hotelroom:
            newname = input("Enter new name (leave blank to keep): ")
            rate_input = input("Enter new rate (leave blank to keep): ")

            if newname:
                Hotelroom[choice]["Room Name"] = newname
            if rate_input:
                Hotelroom[choice]["Rate"] = int(rate_input)

            print("Room updated successfully.")
            time.sleep(1)
        else:
            newname = input("Enter new room name: ")
            newrate = tryparse(input("Enter rate per hour: "))

            if newname and newrate:
                Hotelroom[choice] = {"Room Name": newname, "Rate": newrate}
                print("New room added successfully.")
                time.sleep(1)

#Eto yung Main ---
while True:
    os.system('cls')
    print("=== Welcome To Hotel Reservation System ===")
    print("0. Exit")
    print("1. Book a Room")
    print("2. Admin Control Panel")

    userinput = tryparse(input("> "))

    if userinput == 0:
        break
    elif userinput == 1:
        hotelreservation()
    elif userinput == 2:
        adminpanel()
    else:
        print("Invalid Choice. Try again...")
        time.sleep(1)