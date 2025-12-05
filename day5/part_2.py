def merge_overlapping_ranges(ranges: list[range]) -> list[range]:
    """Merge overlapping ranges."""
    intervals = [(r.start, r.stop) for r in ranges]
    intervals.sort()

    merged = []
    for start, stop in intervals:
        if merged == []:
            merged.append([start, stop])
        else:
            last_start, last_stop = merged[-1]
            # overlapping
            if start <= last_stop:
                merged[-1][-1] = max(last_stop, stop)
            else:
                merged.append([start, stop])

    return [range(start, end) for start, end in merged]
