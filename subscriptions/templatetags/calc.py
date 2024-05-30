from django import template

register = template.Library()

@register.filter
def percentage(value, total):
    if not value == 0:
        calculated_perc = (float(value)/float(total)) * 100
        return calculated_perc
    else:
        return 0