#imports_tester.py

from importlib import import_module
import modules

def main():
    for module in [
        'codecs',
        'colorama',
        'configparser',
        'copy',
        'ctypes',
        'datetime',
        'netifaces',
        'os',
        'pings',
        'sys',
        'threading',
        'time',
        'unicodedata',
    ]:
        try:
            import_module(module)
            print(modules.nowTime(), f'{module:20} is found!!!')
        except:
            print(modules.nowTime(), f'{module:20} is not found...')
    print('--- Finish modules import test ---')

if __name__ == '__main__':
    print('--- Start modules import test ---')
    main()
