from waypoint_core.distance import Distance


class Trail:
    DEFAULT_UNIT = "km"
    ALLOWED_DIFFICULTIES = ("easy", "moderate", "hard", "expert")

    def __init__(self, trail_id, name, distance, elevation_gain_m, difficulty):
        if not isinstance(distance, Distance):
            raise ValueError("distance must be a Distance object")

        self.id = trail_id
        self.name = name
        self.distance = distance
        self.elevation_gain_m = elevation_gain_m

        self.set_difficulty(difficulty)

    def set_difficulty(self, difficulty):
        if not self.is_valid_difficulty(difficulty):
            raise ValueError("Invalid difficulty")

        self._difficulty = difficulty

    @property
    def difficulty(self):
        return self._difficulty

    @classmethod
    def from_dict(cls, data):
        distance = Distance(data["distance"], cls.DEFAULT_UNIT)

        return cls(
            data["id"],
            data["name"],
            distance,
            data["elevation_gain_m"],
            data["difficulty"]
        )

    @classmethod
    def set_default_unit(cls, unit):
        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'")

        cls.DEFAULT_UNIT = unit
    @staticmethod
    def is_valid_difficulty(difficulty):
        return difficulty in Trail.ALLOWED_DIFFICULTIES

    def __eq__(self, other):
        if not isinstance(other, Trail):
            return False

        return self.id == other.id