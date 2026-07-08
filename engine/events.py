class EventSystem:
    """
    Handles global simulation events.
    """

    def __init__(self):

        self.events = []

    def emit(self, event):

        self.events.append(event)

    def process(self):

        while self.events:

            event = self.events.pop(0)

            print(f"[EVENT] {event}")