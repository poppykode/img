from datetime import datetime


def get_current_datetime(format_string="%Y-%m-%d %H:%M:%S"):
    now = datetime.now()
    formatted_datetime = now.strftime(format_string)
    return formatted_datetime


def convert_date_to_string(date_obj, format_string="%Y-%m-%d"):
    formatted_date = date_obj.strftime(format_string)
    return formatted_date
