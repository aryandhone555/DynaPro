def calculate_status(
    value,
    warning,
    critical,
    metric_name=None
):

    if warning is None or critical is None:
        return "GREEN"

    lower_is_bad = [
        "Availability"
    ]

    if metric_name in lower_is_bad:

        if value <= critical:
            return "RED"

        if value <= warning:
            return "AMBER"

        return "GREEN"

    if value >= critical:
        return "RED"

    if value >= warning:
        return "AMBER"

    return "GREEN"