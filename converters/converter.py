class Converter:
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit
        self.to_unit = to_unit

    def convert_units(self, value):
        return (value * self.from_unit) / self.to_unit
