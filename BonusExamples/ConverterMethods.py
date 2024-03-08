def convert_to_meters(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


def convert_to_millimeters(fluid_ounces):
    equivalence = 29.57353

    millimeters = fluid_ounces * equivalence
    return millimeters
