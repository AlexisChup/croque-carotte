class ValueNotInInterval(Exception):
    """
    Raised when the input value is not in the interval 
    (between the number of left rabbits of one's player)
    """
    pass

class PositionIncorrect(Exception):
    """
    Raised when the position got isn't valid
    """
    pass