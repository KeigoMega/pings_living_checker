# v200317-1532

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
            i=0
            texts = ''
            hb = '  サーチ中'
            for name, ip in ip_dict.items():
                i+=1
                res = p.ping(ip)
                if not res.is_reached():
                    texts += f'{i:2} \033[41m消失 {name} ({ip})\033[0m\n'
                else:
                    texts += f'{i:2} \033[32m生存 {name} ({ip})\033[0m\n'
                print(hb, end='\r')
                hb += '.'
            os.system('cls')
            print('<-- 通信機器生存チェッカー -->')
            print(modules.nowTime(), '時点での生存確認')
            print(texts)
    else:
        print('please save config.ini with IP List into inifiles...')

if __name__ == '__main__':
    main()
