import json
from src.data.constants import DATA_DIR, DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE


def get_top_usage(
    top_n: int,
    date: str = DEFAULT_DATE,
    tier: str = DEFAULT_TIER,
    baseline: int = DEFAULT_BASELINE,
):
    """
    Get the top n Pokemon usage rates for a given date, tier, and baseline
    :param top_n: The top number of Pokemon to return
    :param date: The date of the usage data
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    """
    data_category = "usage"
    path = f"{DATA_DIR}/{data_category}/{date}_{tier}-{baseline}.json"
    with open(path) as file:
        usage = json.load(file)
        top_usage = usage[:top_n]

    return top_usage
