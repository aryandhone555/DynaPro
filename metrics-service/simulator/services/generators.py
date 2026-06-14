
import random
from datetime import datetime


def get_traffic_multiplier():

    hour = datetime.now().hour

    if 0 <= hour < 6:
        return 0.3

    elif 6 <= hour < 12:
        return 0.6

    elif 12 <= hour < 18:
        return 0.8

    elif 18 <= hour < 23:
        return 1.0

    return 0.5

def generate_app_metric(metric_name):

    traffic = get_traffic_multiplier()

    generators = {

        "CPU Usage":
            lambda: round(random.uniform(20, 90) * traffic, 2),

        "Memory Usage":
            lambda: round(random.uniform(30, 85), 2),

        "Response Time":
            lambda: round(random.uniform(100, 800) * traffic, 2),

        "Request Rate":
            lambda: round(random.uniform(100, 2000) * traffic, 2),

        "Error Rate":
            lambda: round(random.uniform(0, 5), 2),

        "Availability":
            lambda: round(random.uniform(98, 100), 2),
    }

    return generators[metric_name]()

def generate_db_metric(metric_name):

    traffic = get_traffic_multiplier()

    generators = {

        "CPU Usage":
            lambda: round(random.uniform(25, 95) * traffic, 2),

        "Memory Usage":
            lambda: round(random.uniform(40, 90), 2),

        "Connections":
            lambda: int(random.uniform(100, 900) * traffic),

        "Query Latency":
            lambda: round(random.uniform(20, 300) * traffic, 2),

        "Disk Usage":
            lambda: round(random.uniform(50, 90), 2),

        "TPS":
            lambda: round(random.uniform(50, 3000) * traffic, 2),
    }

    return generators[metric_name]()