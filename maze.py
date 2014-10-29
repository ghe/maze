import random

class Room(object):
    directions = ["North", "South", "East", "West", "Up", "Down"]
    next_id = 65

    def __init__(self):
        self._hallways = {}
        self._name = chr(Room.next_id)
        Room.next_id += 1

    def __str__(self):
        s = "%s: " % (self.name,)
        for d in self._hallways:
            s += "%s -> %s, " % (d, self.adjacent(d).name)
        return s

    @property
    def name(self):
        return self._name

    def connect(self, direction, room):
        if direction in Room.directions:
            if not direction in self._hallways:
                self._hallways[direction] = room
                return True
        return False

    def connected_dirs(self):
        return list(set(Room.directions).intersection(self._hallways))

    def free_dirs(self):
        return list(set(Room.directions).difference(self._hallways))

    def can_connect(self):
        return len(self.free_dirs) > 0

    def rand_connect(self, room):
        free = self.free_dirs()
        if len(free) > 0:
            freedir = random.choice(free)
            return self.connect(freedir, room)
        return False

    def adjacent(self, direction):
        if direction in Room.directions:
            if direction in self._hallways:
                return self._hallways[direction]
        return None

rooms = [Room() for _ in range(4)]

def bidir_connect(room_a, room_b):
    if room_a.can_connect:
        if room_b.rand_connect(room_a):
            return room_a.rand_connect(room_b)
    return False

#connect all rooms in a chain
last_room = None
for room in rooms:
    if last_room:
        bidir_connect(last_room, room)
    last_room = room

#add some more connections
for room in rooms:
    bidir_connect(room, random.choice(rooms))

for room in rooms:
    print(room)



