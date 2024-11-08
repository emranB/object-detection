def calculate_distance(box):
    """Calculate the approximate distance of an object based on bounding box size."""
    return round(10 - box[2] / 50, 2)
