def my_range(start, stop, step=1):
    """Generator that works like Python's built-in range()"""
    if step == 0:
        raise ValueError("step cannot be zero")

    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step
