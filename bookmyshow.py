class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Seat {self.seat_number} booked.")
        else:
            print(f"Seat {self.seat_number} already booked.")


class Show:
    def __init__(self, movie_name, total_seats):
        self.movie_name = movie_name
        self.seats = [Seat(i) for i in range(1, total_seats + 1)]

    def book_seat(self, seat_number):
        if 1 <= seat_number <= len(self.seats):
            self.seats[seat_number - 1].book()
        else:
            print("Invalid Seat Number")

    def display_seats(self):
        for seat in self.seats:
            print(f"Seat {seat.seat_number}: {'Booked' if seat.is_booked else 'Available'}")


show = Show("SitaRamam", 5)
show.display_seats()
show.book_seat(2)
show.book_seat(2)
show.display_seats()
