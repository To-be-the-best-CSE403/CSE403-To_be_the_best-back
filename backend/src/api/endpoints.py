from typing import Optional
from collections import defaultdict
from src.constants import DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE
from src.data.query_smogon import get_usage


def get_usage_rate(
    pokemon: str,
    date: str = DEFAULT_DATE,
    tier: str = DEFAULT_TIER,
    baseline: int = DEFAULT_BASELINE,
) -> Optional[dict]:
    """
    Get the usage rate for a given Pokemon
    :param pokemon: The name of the Pokemon
    :param date: The date of the usage data
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    :return: The usage rate for the given Pokemon, or None if the Pokemon usage data is not found

    Return format:
    {
        "usage_rate": float,
        "raw_count": int,
        "real_count": int,
    }
    """
    usage = get_usage(date, tier, baseline)
    return usage[pokemon]


def get_usage_top(
    top_n: int,
    date: str = DEFAULT_DATE,
    tier: str = DEFAULT_TIER,
    baseline: int = DEFAULT_BASELINE,
) -> Optional[list]:
    """
    Get the top n Pokemon usage rates for a given date, tier, and baseline
    :param top_n: The top number of Pokemon to return
    :param date: The date of the usage data
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    :return: The top n Pokemon usage rates

    Return format:
    [
        {
            "name": str,
            "usage_rate": float,
            "raw_count": int,
            "real_count": int,
        },
        ...
    ]
    """
    usage = get_usage(date, tier, baseline)
    # Merge the name key with the usage data using dictionary unpacking and convert to list
    usage_list = [{"name": k, **v} for k, v in usage.items()]
    top_usage = sorted(usage_list, key=lambda x: x["usage_rate"], reverse=True)[:top_n]
    return top_usage


def get_usage_timeline(
    pokemons: list[str],
    start_date: str,
    duration: int = 1,
    tier: str = DEFAULT_TIER,
    baseline: int = DEFAULT_BASELINE,
) -> Optional[dict]:
    """
    Get the usage rates for a given set of Pokemon over a specified duration starting from a given date
    :param pokemons: The set of Pokemon to get usage rates for
    :param start_date: The start date of the usage data in the format "year-month"
    :param duration: The number of months to get usage data for
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    :return: The usage rates for the given set of Pokemon over the specified duration

    Return format:
    {
        "pokemon1": [
            {
                "usage_rate": float,
                "raw_count": int,
                "real_count": int,
            },
            ...
        ],
        "pokemon2": [
            {
                "usage_rate": float,
                "raw_count": int,
                "real_count": int,
            },
            ...
        ],
        ...
    }
    """
    usage_data = defaultdict(list)
    for _ in range(duration):
        current_date = start_date
        usage = get_usage(current_date, tier, baseline)

        for pokemon in pokemons:
            if usage[pokemon] is not None:
                usage_data[pokemon].append(usage[pokemon])

        # Increment the date for the next iteration
        year, month = map(int, current_date.split("-"))
        month += 1
        if month > 12:
            month = 1
            year += 1
        start_date = f"{year}-{month:02d}"

    return usage_data
