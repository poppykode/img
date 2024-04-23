
from django.core.paginator import Paginator

def paginator(request,qs,number_of_item):
    """
    Creates a paginated view using the provided queryset and per_page setting.
    """
    paginator = Paginator(qs, number_of_item)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj