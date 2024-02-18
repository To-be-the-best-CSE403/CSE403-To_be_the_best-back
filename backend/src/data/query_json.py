import json
import os
from collections import defaultdict
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
    path = os.path.join(DATA_DIR, data_category, f"{date}_{tier}-{baseline}.json")
    with open(path) as file:
        usage = json.load(file)
        top_usage = usage[:top_n]

    return top_usage


def get_timeline_usage(
    pokemons: set[str],
    start_date: str,
    duration: int = 1,
    tier: str = DEFAULT_TIER,
    baseline: int = DEFAULT_BASELINE,
):
    """
    Get the usage rates for a given set of Pokemon over a specified duration starting from a given date
    :param pokemons: The set of Pokemon to get usage rates for
    :param start_date: The start date of the usage data in the format "year-month"
    :param duration: The number of months to get usage data for
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    """
    data_category = "usage"
    usage_data = defaultdict(list)

    for _ in range(duration):
        current_date = start_date
        path = os.path.join(
            DATA_DIR, data_category, f"{current_date}_{tier}-{baseline}.json"
        )

        with open(path) as file:
            usage = json.load(file)

        usage_pokemon = [entry for entry in usage if entry["name"] in pokemons]
        for entry in usage_pokemon:
            usage_data[entry["name"]].append(
                {
                    "usage_rate": entry["usage_rate"],
                    "raw_count": entry["raw_count"],
                    "real_count": entry["real_count"],
                }
            )

        # Increment the date for the next iteration
        year, month = map(int, current_date.split("-"))
        month += 1
        if month > 12:
            month = 1
            year += 1
        start_date = f"{year:04d}-{month:02d}"

    return usage_data
