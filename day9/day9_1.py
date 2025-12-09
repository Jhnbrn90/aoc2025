from dataclasses import dataclass

@dataclass
class Tile:
    """Represent a tile's coordinates."""
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def calculate_squared_distance(p: Tile, q: Tile):
    """Return squared euclidian distance between tiles.

    For 2D coordinates (x,y), the Euclidian distance can be
    calculated as: sqrt((qx-px)^2 + (qy-py)^2).

    The squared distance is returned from this function for
    performance reasons. If the non-squared distance is required,
    it should be manually calculated with `math.sqrt()`.
    """
    return (q.x-p.x)**2 + (q.y-p.y)**2


def calculate_area(q: Tile, p: Tile):
    """Calculate area between tiles `p` and `q`.
    
    To properly account for the area in the grid, 1 is
    added to the difference in coordinates to include the
    corner pieces as well.

      0 1 2 3 4
    0 # . . . .
    1 . . . . .
    2 . . # . .
    3 . . . . .

    In this example, the area would equal:
     - (2-0) * (2-0) = 4; which is incorrect

    Addition of 1 resolves:
     - ((2-0)+1) * ((2-0)+1) = 6; which is correct
    """
    return (abs(q.x - p.x)+1) * (abs(q.y - p.y)+1)


def largest_euclidian_distances(tile_coordinates: list[Tile]) -> list[tuple[int, tuple[int, int]]]:
    """Return list of euclidian distances between two 2D points.
    
    The list values have the form (distance, (i,j)), where `i` and `j`
    are the indexes of the coordinates in the list of `coordinates`.
    """
    distances = []

    for i, tile in enumerate(tile_coordinates):
        if i == len(tile_coordinates)-1:  # last element
            break

        for j in range(i+1, len(tile_coordinates)):
            distances.append(
                (calculate_squared_distance(tile_coordinates[i], tile_coordinates[j]), (i, j))
            )

    return sorted(distances, reverse=True)


def find_largest_area_n_distances(n: int, distances: list[tuple[int, tuple[int, int]]], tiles: list[Tile]) -> int:
    """Get the largest area from a list of highest euclidian distances."""

    highest_area = 0
    
    # Check area for the top-n euclidian distances
    for (distance, (tile_i, tile_j)) in distances[:n]:
        area = calculate_area(tiles[tile_i], tiles[tile_j])
        if area > highest_area:
            highest_area = area

    return highest_area
