from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    
    @classmethod
    def from_str(cls, color_str) -> 'Color':
        return Color[color_str.upper()]

assert Color.from_str("red") == Color.RED
