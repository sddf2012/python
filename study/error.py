import traceback

try:
    print(5/0)
except Exception as e:
    print(f'异常：{e}')
    # traceback.print_exc()
    raise
else:
    print('asdf')