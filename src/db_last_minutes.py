import json
import os

import helpers.outils as outils

from config import get_config
from APIRestClient import APIRestClient
"""
REQUEST:
    - minutes:
    downloaded data is between (last_recording - minutes, last_recording)

REMARK:
It takes a long time
"""
# --------------------------------
# Data for request
# --------------------------------
minutes = 3
decimation_factor = 1
interval_minutes = 0.05
# --------------------------------

config = get_config()
client = APIRestClient(config)

date_range = client.get_last_minutes_range(minutes)
if date_range:
    start_date = date_range['timeBefore']
    end_date = date_range['latestTimestamp']

    # A) DOWNLOAD ACCELERATIONS
    result = client.get_date_range(start_date, end_date,
                                   db_type='accelerations',
                                   decimation_factor=decimation_factor,
                                   interval_minutes=interval_minutes)

    filename = f"APIRest_acc_last_{outils.format_date(str(minutes))}_minutes_{outils.format_date(start_date)}.json"
    print(f"Downloading results in {config['db_download_path']} as {filename}")
    with open(os.path.join(config['db_download_path'], filename), 'w') as f:
        json.dump(result, f)

    # B) DOWNLOAD TEMPERATURE & HUMIDITY
    result = client.get_date_range(start_date, end_date,
                                   db_type='temperature_humidity',
                                   decimation_factor=decimation_factor,
                                   interval_minutes=interval_minutes)

    filename = f"APIRest_th_last_{outils.format_date(str(minutes))}_minutes_{outils.format_date(start_date)}.json"
    print(f"Downloading results in {config['db_download_path']} as {filename}")
    with open(os.path.join(config['db_download_path'], filename), 'w') as f:
        json.dump(result, f)
else:
    print("Failed to get date range.")
