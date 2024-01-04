class Clock:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
        while self.minute < 0 or self.minute > 59:
            self.hour += self.minute // 60
            self.minute = self.minute % 60

        while self.hour < 0 or self.hour > 23:
                self.hour = self.hour % 24

    def __repr__(self):
        return "Clock(" + str(self.hour) + ", " + str(self.minute) + ")"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other: "Clock"):
        return self.__str__() == other.__str__()

    def __add__(self, minutes: int):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int):
        return Clock(self.hour, self.minute - minutes)


if __name__ == "__main__":
    clock = Clock(-5, 60)
    print(clock.__repr__())
    clock += 20
    print(clock)


    ["  +-+",
     "  | |",
     "+-+-+",
     "| | |",
     "+-+-+"]