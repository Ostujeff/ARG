#This script connects to dcode site - keyboard shift cipher

import requests


def print_dict(mas):  # parse and print json
    print('result:\n', '-'*25)
    for k in mas['results']:
        print(k, '\t|', str(mas['results'][k]).replace('&quot;', '"'))
    print('-' * 25)
    return 0


def decode_shift(url, api, encrypted_str):  
    ses = requests.Session()
    ses.headers.update({'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                                       (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'})
    headers = {'x-requested-with': 'XMLHttpRequest', 'referer': url}
    ses.get(url, headers=headers)
    result = ses.post(api, headers=headers, data={'tool': 'keyboard-shift-cipher',
                                                          'ciphertext': encrypted_str, 'lang': 'en',
                                                          'layout': 'auto', 'shift': 'auto', 'alphanum': 'false'})
    print('source: ', encrypted_str)
    return print_dict(result.json())


api_url = 'https://www.dcode.fr/api/'
shift_url = 'https://www.dcode.fr/keyboard-shift-cipher'
enc_str = 'nd..l slf.c'

decode_shift(shift_url, api_url, enc_str)
