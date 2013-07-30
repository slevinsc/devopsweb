# coding=utf-8

from django import template

# 这句是必须滴
register = template.Library()

# 这个类是用来处理Tag的Node的，逻辑很简单


class NavTagItem(template.Node):

    def __init__(self, nav_path, nav_displaytext):
        self.path = nav_path.strip('"')
        self.text = nav_displaytext.strip('"')

    def render(self, context):
        cur_path = context['request'].path
        # context['request']是views传入模板中的request对像，可以通过这种方法从上
        # 文对象context中取得

        current = False
        if self.path == '/':
            current = cur_path == '/'
        else:
            current = cur_path.startswith(self.path)

        cur_id = ''
        if current:
            cur_id = ' id="current" '
        return '<h3><li ><a  %s href="%s" class="bootstro" >%s </a></li></h3>' % (cur_id, self.path, self.text)

# 注册tag，函数基本就是这个样子，不怎么会有变化


@register.tag
def navtagitem(parser, token):
    try:
        tag_name, nav_path, nav_text = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, \
            "%r tag requires exactly two arguments: path and text" % \
            token.split_contents[0]

    return NavTagItem(nav_path, nav_text)
