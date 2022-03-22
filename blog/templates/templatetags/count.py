from django import template
register = template.Library() #例項化

@register.simple_tag
def current_time():
    return datetime.datetime.now().strftime('%Y年%m月%d日  %H:%M:%S')