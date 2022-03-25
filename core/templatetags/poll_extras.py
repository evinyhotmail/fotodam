import os
from django import template

#Nerver forged to call the templates libraru first, jajajja
register = template.Library()

# I can uses the decorator
# if I leave off the name argument
# so I need to use the filter with
# the same name of the fuction

@register.filter
def filename(value):
    return os.path.basename(value.image.name)

#TODO: Implement this fuction in another version ;)
# @register.filter
# def filetype(value):
#     return True

