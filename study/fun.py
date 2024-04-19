# def display_message(msg):
#     print(msg)

# msg=input("enter topic:")
# display_message(msg)
# def animal(type,name):
#     print(type,name)

# animal(123,123)


# def get_formatted_name(first_name, last_name, middle_name=''):
#    """返回标准格式的姓名"""
#    if middle_name:
#     full_name = f"{first_name} {middle_name} {last_name}"
#    else:
#     full_name = f"{first_name} {last_name}"
#    return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# def f1(*args):
#     #args[0]='123'
#     print(args)
# f1(1,2,3)

def f2(**kwargs):
    print(kwargs)
    kwargs[0]='jerry'
    print(kwargs)
f2(name='cat',age=20)