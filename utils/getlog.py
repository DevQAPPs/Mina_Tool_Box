##This script processes log files, filtering entries based on a specified time range. 
##It is specifically designed for log files that start with 'mina.log' and are formatted in JSON with timestamps.

import os
import json
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%fZ')

start_time = datetime.strptime("2024-01-15 07:41:16", "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime("2024-01-15 11:25:37", "%Y-%m-%d %H:%M:%S")
log_directory = ".mina-config"
output_file = "qapp.log"

with open(output_file, "w") as outfile:
    for filename in os.listdir(log_directory):
        if filename.startswith("mina.log"):
            with open(os.path.join(log_directory, filename), "r") as file:
                for line in file:
                    try:
                        log_entry = json.loads(line)
                        timestamp = parse_date(log_entry["timestamp"])
                        if start_time <= timestamp <= end_time:
                            outfile.write(line)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                    except KeyError as e:
                        print(f"Missing key in JSON: {e}")
                    except ValueError as e:
                        print(f"Error parsing date: {e}")

print(f"Processing complete. Output saved to {output_file}")
