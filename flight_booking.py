
from abc import ABC, abstractmethod


# Base class
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# Inheritance
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display_flight(self):
        print(
            self.code, "|", self.airline, "|",
            self.source, "to", self.destination,
            "| Seats:", self.seats,
            "| Fare: Rs.", self.fare
        )

    def reserve_seats(self, tickets):
        if tickets <= self.seats:
            self.seats -= tickets
            return True
        return False


# Booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = (
            self.subtotal * passenger.get_discount() / 100
        )
        self.total = self.subtotal - self.discount

    def display_summary(self):
        print("\n----- BOOKING SUMMARY -----")
        print("Booking ID:", self.booking_id)
        print("Flight Code:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to",
              self.flight.destination)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:",
              type(self.passenger).__name__)
        print("Tickets:", self.tickets)
        print("Base Fare per Ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount: Rs.", self.discount)
        print("Final Amount: Rs.", self.total)


# Flight booking system
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Air India", "Pune", "Delhi", 20, 4000),
            Flight("MB102", "IndiGo", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN103", "Akasa Air", "Pune", "Hyderabad", 25, 3000)
        ]

        self.bookings = []
        self.next_booking_id = 1001

    def display_flights(self):
        print("\n----- AVAILABLE FLIGHTS -----")
        for flight in self.flights:
            flight.display_flight()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code == code.upper():
                return flight
        return None

    def book_flight(self):
        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()

        if not name:
            print("Passenger name cannot be blank.")
            return

        try:
            age = int(input("Enter age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Invalid input! Enter numbers for age and tickets.")
            return

        if age <= 0:
            print("Age must be greater than 0.")
            return

        if tickets <= 0:
            print("Ticket count must be greater than 0.")
            return

        if tickets > flight.seats:
            print("Booking failed: Not enough seats available.")
            return

        passenger_type = input(
            "Passenger type (Regular/Student): "
        ).strip().lower()

        if passenger_type == "regular":
            passenger = RegularPassenger(name, age)
        elif passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            print("Invalid passenger type.")
            return

        # Confirm booking only after validation
        flight.reserve_seats(tickets)

        booking = Booking(
            "BK" + str(self.next_booking_id),
            flight,
            passenger,
            tickets
        )

        self.bookings.append(booking)
        self.next_booking_id += 1

        print("\nBooking confirmed!")
        booking.display_summary()

    def view_booking(self):
        if not self.bookings:
            print("No booking found.")
        else:
            self.bookings[-1].display_summary()

    def run(self):
        print("Welcome to Kiran Air Booking!")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice! Please select 1, 2, 3, or 4.")


# Start the application
app = FlightBookingSystem()
app.run()
