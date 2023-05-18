from django import template

register = template.Library()

@register.filter
def model_type(value):
    return type(value).__name__

@register.filter
def rank(review):
    return review.get_rating_display()