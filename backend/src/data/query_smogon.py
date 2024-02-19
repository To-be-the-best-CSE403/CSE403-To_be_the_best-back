import requests
from collections import defaultdict
from src.constants import SMOGON_STATS, DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE

cache_usage = {}


def get_usage(date=DEFAULT_DATE, tier=DEFAULT_TIER, baseline=DEFAULT_BASELINE):
    """
    Get the usage data for a given date, tier, and baseline
    See: https://www.smogon.com/forums/threads/gen-9-smogon-university-usage-statistics-discussion-thread.3711767/
    :param date: The date of the usage data
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    :return: The usage data for the given date, tier, and baseline

    Return format:
    {
        pokemon: {
            "usage_rate": float,
            "raw_count": int,
            "real_count": int,
        },
        ...
    }
    """
    if (date, tier, baseline) in cache_usage:
        print("query_smogon: cache hit for", (date, tier, baseline), flush=True)
        return cache_usage[(date, tier, baseline)]

    usage_data = defaultdict(None)
    url = f"{SMOGON_STATS}{date}/{tier}-{baseline}.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text

        # Skipping the header and footer
        lines = data.split("\n")
        start_index = 5
        end_index = len(lines) - 2

        for line in lines[start_index:end_index]:
            elements = line.replace(" ", "").split("|")[1:-1]
            name = elements[1]
            usage_rate = elements[2]
            raw_count = elements[3]
            real_count = elements[5]

            usage_data[name] = {
                "usage_rate": float(usage_rate.replace("%", "")),
                "raw_count": int(raw_count),
                "real_count": int(real_count),
            }

        cache_usage[(date, tier, baseline)] = usage_data
        return usage_data
    except requests.RequestException as e:
        print(f"query_smogon: error getting usage data: {e}", flush=True)
        return usage_data
