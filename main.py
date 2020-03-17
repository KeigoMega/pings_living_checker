# v200317-1250

import os
import pings
import colorama
import time
import modules

colorama.init()
config_file = os.path.join(os.path.dirname(__file__), 'inifiles/config.ini')

def main():
    ret, ip_dict = modules.readDefault(config_file)
    if ret:
        p = pings.Ping()
        while True:
            texts = ''
            hb = 'seraching'
            for name, ip in ip_dict.items():
                res = p.ping(ip)
                if not res.is_reached():
                    texts += f'\033[41m{name} ({ip})\033[0m\n'
                else:
                    texts += f'\033[32m{name} ({ip})\033[0m\n'
                print(modules.nowTime(),  hb, end='\r')
                hb += '.'
            os.system('cls')
            print('<-- 通信機器生存チェッカー -->')
            print(texts)
    else:
        print('please save config.ini with IP List into inifiles...')

if __name__ == '__main__':
    main()
