class Distance:
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