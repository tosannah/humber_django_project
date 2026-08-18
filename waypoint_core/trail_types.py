from waypoint_core.trail import Trail
from waypoint_core.mixins import ElevationMixin, RatingMixin


class DayHike(Trail):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)

    def estimated_time(self):
        return self.distance.magnitude / 4

    def summary(self):
        return f"Day hike: {self.name}"


class BackpackingRoute(Trail):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)

    def estimated_time(self):
        return self.distance.magnitude / 3

    def summary(self):
        return f"Backpacking route: {self.name}"


class TrailRun(Trail):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)

    def estimated_time(self):
        return self.distance.magnitude / 8

    def summary(self):
        return f"Trail run: {self.name}"


class GuidedDayHike(DayHike):
    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty, guide_name):
        super().__init__(trail_id, name, distance, elevation_gain_m, difficulty)
        self.guide_name = guide_name

    def summary(self):
        return super().summary() + f" - Guide: {self.guide_name}"


class RatedDayHike(ElevationMixin, RatingMixin, DayHike):
    pass


class FakeTrail:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def estimated_time(self):
        return self.time