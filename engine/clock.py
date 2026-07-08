class Clock:
    """
    Controls simulation time.
    """

    def __init__(self):

        self.tick = 0
        self.day = 1
        self.year = 1

    def update(self):

        self.tick += 1

        if self.tick >= 100:

            self.tick = 0
            self.day += 1

            if self.day > 365:

                self.day = 1
                self.year += 1

    def __str__(self):

        return f"Year {self.year} | Day {self.day} | Tick {self.tick}"