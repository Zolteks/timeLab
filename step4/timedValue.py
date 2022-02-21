class TimedValue():
    def __init__(self, value, clock, duration=60):
        self.target = value
        self.v = 0
        self.duration = duration
        self.clock = clock
        self.birth = clock.now()
        self.speed = self.target/self.duration

    def value(self):
        curVal = (self.now()-self.birth)*self.speed
        if curVal < self.target:
            return curVal
        return self.target

    def now(self):
        return self.clock.now()