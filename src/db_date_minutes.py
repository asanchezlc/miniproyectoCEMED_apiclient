import json
import os

import helpers.outils as outils

from config import get_config
from APIRestClient import APIRestClient

"""
REQUEST:
    - date: exact day/hour at which we want to request data
    - delta_minutes: data requested will be:
    downloaded data is between (date - delta_minutes, date + delta_minutes)
"""

# --------------------------------
# Data for request
# --------------------------------
date = "2024/07/03 14:08:04"
delta_minutes = 1
decimation_factor = 1
interval_minutes = 0.05
# --------------------------------

config = get_config()
client = APIRestClient(config)

start_date, end_date = outils.calculate_date_range(date, delta_minutes)

# A) ACCELERATIONS
result = client.get_date_range(start_date, end_date, db_type='accelerations',
                               decimation_factor=decimation_factor,
                               interval_minutes=interval_minutes)
if result:
    filename = f"APIRest_acc_{outils.format_date(start_date)}_delta_{outils.format_date(str(delta_minutes))}_minutes.json"
    print(f"Downloading results in {config['db_download_path']} as {filename}")
    with open(os.path.join(config['db_download_path'], filename), 'w') as f:
        json.dump(result, f)
else:
    print("Failed to get date range.")

# B) TEMPERATURE & HUMIDITY
result = client.get_date_range(start_date, end_date, db_type='temperature_humidity',
                               decimation_factor=decimation_factor,
                               interval_minutes=interval_minutes)
if result:
    filename = f"APIRest_th_{outils.format_date(start_date)}_delta_{outils.format_date(str(delta_minutes))}_minutes.json"
    print(f"Downloading results in {config['db_download_path']} as {filename}")
    with open(os.path.join(config['db_download_path'], filename), 'w') as f:
        json.dump(result, f)
else:
    print("Failed to get date range.")
