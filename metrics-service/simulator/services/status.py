def calculate_status(value, warning, critical):

    if warning is None or critical is None:
        return "GREEN"

    if value >= critical:
        return "RED"

    if value >= warning:
        return "AMBER"

    return "GREEN"