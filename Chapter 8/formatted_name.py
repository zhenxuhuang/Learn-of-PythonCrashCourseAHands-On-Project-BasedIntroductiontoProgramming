"""
Python编程：从入门到实践
第8章 函数

8.2
"""


# 函数原型
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 设置中间名形参
def get_formatted_name_new(first_name, middle_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician_new = get_formatted_name_new('john', 'lee', 'hooker')
print(musician_new)


def get_formatted_name_newer(first_name, last_name, middle_name=''):
    """返回整洁的姓名。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:   # middle_name为空字符串执行
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician_newer = get_formatted_name_newer('jimi', 'hendrix')
print(musician_newer)
musician_newer = get_formatted_name_newer('john', 'hooker', 'lee')
print(musician_newer)