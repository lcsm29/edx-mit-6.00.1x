from math import tan, pi


def polysum(n: int, s: float) -> float:
    '''Returns the sum of the area and square of the perimeter of the polygon

        Args:
            n (int) -> number of sides of the regular polygon.

            s (float) -> the length of each side.

        Returns (float) -> the sum of area and square of perimeter of the 
                           regular polygon, rounded to 4th decimal places.
    '''
    assert n > 0 and type(n) == int, 'n should be a posive integer'
    assert type(s) in (int, float), 's should be either a float or an integer'
    area = 0.25 * n * s**2 / tan(pi / n)
    perisq = (n * s) ** 2                 # square of the perimeter  
    return round(area + perisq, 4)        # rounded to 4th decimal places
