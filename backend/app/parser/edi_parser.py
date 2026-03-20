from .tokenizer import Tokenizer
from .segment import Segment


class EDIParser:
    def __init__(self):
        self.tokenizer = Tokenizer()

    def parse(self, content: str):
        """
        Convert raw EDI string into structured segments
        """
        raw_segments = self.tokenizer.split_segments(content)

        parsed_segments = []

        for raw_segment in raw_segments:
            name, elements = self.tokenizer.split_elements(raw_segment)
            segment = Segment(name, elements)
            parsed_segments.append(segment)

        return parsed_segments

    def parse_to_json(self, content: str):
        """
        Return JSON-friendly structure (for API)
        """
        segments = self.parse(content)
        return [seg.to_dict() for seg in segments]
