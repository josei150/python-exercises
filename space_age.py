class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.period = 31557600
        self.earth = round(self.seconds / self.period, 2)
    
    def on_earth(self):
        return self.earth

    def on_mercury(self):
        self.period = 0.2408467
        return round(self.earth / self.period, 2)

    def on_venus(self):
        self.period = 0.61519726
        return round(self.earth / self.period, 2)

    def on_mars(self):
        self.period = 1.8808158
        return round(self.earth / self.period, 2)

    def on_jupiter(self):
        self.period = 11.862615
        return round(self.earth / self.period, 2)

    def on_saturn(self):
        self.period = 29.447498
        return round(self.earth / self.period, 2)

    def on_uranus(self):
        self.period = 84.016846
        return round(self.earth / self.period, 2)

    def on_neptune(self):
        self.period = 164.79132
        return round(self.earth / self.period, 2)


if __name__ == "__main__":
    print(SpaceAge(2134835688).on_earth())
    print(SpaceAge(2134835688).on_mercury())