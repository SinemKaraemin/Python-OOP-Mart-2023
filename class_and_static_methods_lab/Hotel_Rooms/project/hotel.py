from Python_OOP_LAB.Class_and_Static_Methods.Hotel_Rooms.project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.take_room(people)

        if result:
            return result

        self.guests += people

    def free_room(self, room_number):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        result = room.free_room(room_number)
        guests = room.guests

        if result:
            return result

        self.guests -= guests

    def status(self):
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {", ".join(str(r.number) for r in self.rooms if not r.is_taken)}\n' \
               f'Taken rooms: {", ".join(str(r.number) for r in self.rooms if r.is_taken)}'

