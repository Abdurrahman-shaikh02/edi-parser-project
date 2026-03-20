class Segment:
    def __init__(self, name: str, elements: list[str]):
        self.name = name
        self.elements = elements

    def to_dict(self):
        return {
            "name": self.name,
            "elements": self.elements
        }

    def __repr__(self):
        return f"{self.name} -> {self.elements}"
