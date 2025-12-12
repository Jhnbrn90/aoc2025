def main():
    with open('day_12/puzzle_input.txt') as f:
        puzzle_input = f.read()

    gifts = {}
    regions = []

    for block in puzzle_input.strip().split("\n\n"):
        if ':\n' in block:
            # it's a gift
            idx, shape = block.split(':')
            gifts[int(idx)] = shape.count('#')
        if 'x' in block:
            # it's an area block
            for line in block.split("\n"):
                area, gift_indices = line.split(':')
                # width, height = area.split('x')
                # area = int(width) * int(height)
                regions.append(
                    (area, [int(i) for i in gift_indices.split(' ') if i != ''])
                )

    areas_that_can_fit = []

    for region in regions:
        available_area, number_of_gifts_by_index = region

        total_gifts_area = 0
        for i, times in enumerate(number_of_gifts_by_index):
            total_gifts_area += times*gifts[i]

        x_area, y_area = map(int, available_area.split("x"))
        total_available_area = x_area * y_area

        if total_gifts_area > total_available_area:
            areas_that_can_fit.append("NO")

        elif sum(number_of_gifts_by_index) <= (x_area//3)*(y_area//3):  # can fit each in its own 3x3
            areas_that_can_fit.append("YES")

        else:
            areas_that_can_fit.append("MAYBE")

    results = {
        "yes": areas_that_can_fit.count("YES"),
        "maybe": areas_that_can_fit.count("MAYBE"),
        "no": areas_that_can_fit.count("NO"),
    }

    print(results)


if __name__ == "__main__":
    main()
