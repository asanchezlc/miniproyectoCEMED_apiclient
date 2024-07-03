
import requests
import helpers.outils as outils


class APIRestClient:
    def __init__(self, config):
        self.base_url = config['base_url']

    def get_date_range(self, start_date, end_date, db_type='accelerations',
                       decimation_factor=1, interval_minutes=0.1):
        url = f"{self.base_url}/getDateRange.php"
        partitions = outils.partition_date_range(
            start_date, end_date, interval_minutes)
        all_results = []
        for partition_start, partition_end in partitions:
            data = {'params': {
                        'start_date': partition_start,
                        'end_date': partition_end,
                        'db_type': db_type,
                        'decimation_factor': decimation_factor
                    }
                    }
            response = requests.post(url, json=data)
            try:
                result = response.json()
                all_results.extend(result)

            except ValueError:
                print("Failed to decode JSON from the response.")
                continue
        return all_results

    def get_last_minutes_range(self, minutes, db_type='accelerations'):
        # Update with the actual PHP file name
        url = f"{self.base_url}/requestDate.php"
        data = {
            'params': {
                'minutes': minutes,
                'db_type': db_type,
            }
        }
        response = requests.post(url, json=data)
        try:
            result = response.json()
            return result
        except ValueError:
            print("Failed to decode JSON from the response.")
            return None
