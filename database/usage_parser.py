import requests
import json
import argparse


def get_usage(date="2024-01", tier="gen9ou", baseline=1500):
    """
    Get the usage data for a given date, tier, and baseline
    See: https://www.smogon.com/forums/threads/gen-9-smogon-university-usage-statistics-discussion-thread.3711767/
    :param date: The date of the usage data
    :param tier: The tier of the usage data
    :param baseline: The baseline of the usage data
    """
    url = f"https://www.smogon.com/stats/{date}/{tier}-{baseline}.txt"
    response = requests.get(url)
    data = response.text

    # Skipping the header and footer
    lines = data.split("\n")
    start_index = 5
    end_index = len(lines) - 2

    usage_data = []
    for line in lines[start_index:end_index]:
        elements = line.replace(" ", "").split("|")[1:-1]
        name = elements[1]
        usage_rate = elements[2]
        raw_count = elements[3]
        real_count = elements[5]

        usage = {
            "name": name,
            "usage_rate": float(usage_rate.replace("%", "")),
            "raw_count": int(raw_count),
            "real_count": int(real_count),
        }

        usage_data.append(usage)

    file_name = f"{date}_{tier}-{baseline}.json"
    with open(file_name, "w") as json_file:
        json.dump(usage_data, json_file, indent=2)

    print(f"Usage data saved to {file_name}")


# Example usage: python usage_parser.py --date 2024-01
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", type=str, default="2024-01")

    args = parser.parse_args()
    get_usage(args.date)
