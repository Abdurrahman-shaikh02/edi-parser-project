class Tokenizer:
    def __init__(self):
        self.segment_sep = '~'
        self.element_sep = '*'
        self.sub_element_sep = ':'

    def detect_delimiters(self, content: str):
        """
        Robust delimiter detection from ISA segment
        """
        if content.startswith("ISA"):
            # Element separator is always the 4th character
            self.element_sep = content[3]
    
            # ISA segment ends with segment separator → find it dynamically
            isa_end = content.find("ISA")
            first_segment = content.split('\n')[0]
    
            # Last character of ISA segment is segment separator
            if '~' in first_segment:
                self.segment_sep = '~'
            else:
                # fallback: find first non-alphanumeric after ISA
                for ch in content:
                    if not ch.isalnum() and ch not in [' ', '*', ':']:
                        self.segment_sep = ch
                        break

            # Sub-element separator = last char before segment separator
            parts = first_segment.split(self.element_sep)
            if parts:
                last_part = parts[-1]
                if last_part:
                    self.sub_element_sep = last_part[0]
    
    def split_segments(self, content: str):
        """
        Split raw EDI into segments (handles newlines properly)
        """
        self.detect_delimiters(content)

        # 🔥 Normalize newlines (critical fix)
        content = content.replace('\n', '').replace('\r', '')
    
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
