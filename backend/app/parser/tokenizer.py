class Tokenizer:
    def __init__(self):
        self.segment_sep = '~'
        self.element_sep = '*'
        self.sub_element_sep = ':'

    def detect_delimiters(self, content: str):
        """
        Detect separators using ISA segment
        """
        if content.startswith("ISA"):
            self.element_sep = content[3]
            self.sub_element_sep = content[104]
            self.segment_sep = content[105]

    def split_segments(self, content: str):
        """
        Split raw EDI into segments
        """
        self.detect_delimiters(content)

        segments = content.split(self.segment_sep)
        return [seg.strip() for seg in segments if seg.strip()]

    def split_elements(self, segment: str):
        """
        Split a segment into elements
        """
        parts = segment.split(self.element_sep)
        name = parts[0]
        elements = parts[1:]
        return name, elements
