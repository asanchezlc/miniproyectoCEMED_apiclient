import json
import os

import helpers.outils as outils

from config import get_config
from APIRestClient import APIRestClient
"""
REQUEST:
    - start_date:
    - end_date:
    downloaded data is between (start_date, end_date)
"""

# --------------------------------
# Data for request
# --------------------------------
start_date = "2024/07/03 14:08:04"
end_date = "2024/07/03 14:10:04"
decimation_factor = 1
interval_minutes = 0.05
# --------------------------------
config = get_config()
client = APIRestClient(config)

# A) GET ACCELERATIONS
result = client.get_date_range(start_date, end_date,
                               db_type='accelerations',
                               decimation_factor=decimation_factor,
                               interval_minutes=interval_minutes)
if result:
    filename = f"APIRest_acc_{outils.format_date(start_date)}_{outils.format_date(end_date)}.json"
    print(f"Downloading results in {config['db_download_path']} as {filename}")
    with open(os.path.join(config['db_download_path'], filename), 'w') as f:
        json.dump(result, f)
else:
    print("Failed to get date range.")

# B) GET TEMPERATURE & HUMIDITY
result = client.get_date_range(start_date, end_date,
                               db_type='temperature_humidity',
                               decimation_factor=decimation_factor,
                               interval_minutes=interval_minutes)
if result:
    filename = f"APIRest_th_{outils.format_date(start_date)}_{outils.format_date(end_date)}.json"
    print(f"Downloading results in {config['db_download_path']} as {filename}")
    with open(os.path.join(config['db_download_path'], filename), 'w') as f:
        json.dump(result, f)
else:
    print("Failed to get date range.")
