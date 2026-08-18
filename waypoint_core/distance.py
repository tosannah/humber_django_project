class Distance:
    """
    Represents a distance in kilometres or miles.

    Mixed-unit arithmetic and comparisons are rejected with ValueError
    to avoid unexpected automatic conversions.
    """
    def __init__(self, magnitude, unit):
        if magnitude < 0:
            raise ValueError("Distance cannot be negative")

        if unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'")

        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        return self._magnitude

    @property
    def unit(self):
        return self._unit

    def convert(self, target_unit):
        if target_unit not in ("km", "mi"):
            raise ValueError("Unit must be 'km' or 'mi'")

        if target_unit == self._unit:
            return Distance(self._magnitude, self._unit)

        if self._unit == "km":
            new_magnitude = self._magnitude * 0.621371
        else:
            new_magnitude = self._magnitude * 1.60934

        return Distance(new_magnitude, target_unit)

    def __add__(self, other):
        if self.unit != other.unit:
            raise ValueError("Cannot add different units")

        return Distance(self.magnitude + other.magnitude, self.unit)

    def __sub__(self, other):
        if self.unit != other.unit:
            raise ValueError("Cannot subtract different units")

        result = self.magnitude - other.magnitude

        if result < 0:
            raise ValueError("Distance cannot be negative")

        return Distance(result, self.unit)

    def __eq__(self, other):
        if not isinstance(other, Distance):
            return False

        return self.unit == other.unit and self.magnitude == other.magnitude

    def __lt__(self, other):
        if self.unit != other.unit:
            raise ValueError("Cannot compare different units")

        return self.magnitude < other.magnitude

    def __gt__(self, other):
        if self.unit != other.unit:
            raise ValueError("Cannot compare different units")

        return self.magnitude > other.magnitude

    def __str__(self):
        return f"{self.magnitude} {self.unit}"

    def __repr__(self):
        return f"Distance({self.magnitude}, '{self.unit}')"