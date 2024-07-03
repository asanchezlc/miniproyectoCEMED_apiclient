
from datetime import datetime, timedelta


def partition_date_range(start_date, end_date, interval_minutes):
    try:
        start = datetime.strptime(start_date, "%Y/%m/%d %H:%M:%S")
        end = datetime.strptime(end_date, "%Y/%m/%d %H:%M:%S")
    except:
        start = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    delta = timedelta(minutes=interval_minutes)

    partitions = []
    current_start = start
    while current_start < end:
        current_end = min(current_start + delta, end)
        partitions.append((current_start.strftime(
            "%Y/%m/%d %H:%M:%S"), current_end.strftime("%Y/%m/%d %H:%M:%S")))
        current_start = current_end

    return partitions


def calculate_date_range(date, interval):
    """interval is given in minutes"""
    date = datetime.strptime(date, "%Y/%m/%d %H:%M:%S")
    interval = timedelta(minutes=interval)
    start_date = date - interval
    end_date = date + interval
    return start_date.strftime("%Y/%m/%d %H:%M:%S"), end_date.strftime("%Y/%m/%d %H:%M:%S")


def format_date(date_str):
    translation_table = str.maketrans({
        '/': '_',
        ':': '_',
        ' ': '_',
        '.': '_'
    })

    date_formatted = date_str.translate(translation_table)
    return date_formatted
