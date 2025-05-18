


class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int, default=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def tick(self):
        if self.seconds < 59:
            self.seconds += 1
        elif self.seconds == 59:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            elif self.minutes == 59:
                self.minutes = 0
                if self.hours < 23:
                    self.hours += 1
                elif self.hours == 23:
                    self.hours = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

clock = Clock(23, 59, 55)
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)
clock.tick()
print(clock)

clock.set(12, 5)
print(clock)

# watch = Stopwatch()
# for i in range(3600):
#     print(watch)
#     watch.tick()