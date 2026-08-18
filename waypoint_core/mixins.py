class ElevationMixin:
    def elevation_grade(self):
        if self.distance.magnitude == 0:
            return 0

        return self.elevation_gain_m / self.distance.magnitude


class RatingMixin:
    def average_rating(self):
        return 4.5