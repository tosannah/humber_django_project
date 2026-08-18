class Itinerary:
    def __init__(self):
        self.trails = []

    def add_trail(self, trail):
        self.trails.append(trail)

    def total_distance(self):
        total = 0

        for trail in self.trails:
            total += trail.distance.magnitude

        return total