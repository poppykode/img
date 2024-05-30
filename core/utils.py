from datetime import datetime
from django.core.paginator import Paginator


def get_current_datetime(format_string="%Y-%m-%d %H:%M:%S"):
    now = datetime.now()
    formatted_datetime = now.strftime(format_string)
    return formatted_datetime


def convert_date_to_string(date_obj, format_string="%Y-%m-%d"):
    formatted_date = date_obj.strftime(format_string)
    return formatted_date


def paginator(request,qs,number_of_item):
    """
    Creates a paginated view using the provided queryset and per_page setting.
    """
    paginator = Paginator(qs, number_of_item)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj

