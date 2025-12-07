from functools import cache


def main():
    with open('day7/puzzle_input.txt') as f:
        puzzle_input = f.read()
    
    # Day 2
    grid = [list(c) for c in puzzle_input.split('\n') if c != '']

    @cache
    def walk_grid(x, y):
        if y >= len(grid):
            # Fully walked route until the end
            return 1

        match grid[y][x]:
            case '.' | 'S':
                return walk_grid(x, y+1)
            case '^':
                return walk_grid(x-1, y) + walk_grid(x+1, y)

    start_x = grid[0].index('S')

    total_timelines = walk_grid(x=start_x, y=0)

    print(f"Timelines: {total_timelines}")


if __name__ == "__main__":
    main()
