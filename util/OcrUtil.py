# -*- coding: utf-8 -*- 
# @Time : 2019/6/26 下午3:05 
# @Author : CcphAmy 
# @Site :  
# @File : OcrUtil.py.py 
# @Software: PyCharm

import requests
import json
import logging

class SouGoOcr(object):
    """docstring for SouGoOcr"""

    def __init__(self):
        super(SouGoOcr, self).__init__()

    @staticmethod
    def trans(image):
        url = "http://ocr.shouji.sogou.com/v2/ocr/json"
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        file = open(image,'rb')
        files = {'pic': ('pic.jpg', file)}
        try:
            r = requests.post(url=url, files=files, headers=headers).text
            content = SouGoOcr.conversion(r)
        except Exception as e:
            logging.error(e)
            return e
        finally:
            file.close()
        return content

    @staticmethod
    def conversion(jsonStr):
        # 转换为json
        try:
            transform = json.loads(jsonStr)
            if 'success' in transform and 'result' in transform:
                if transform['success'] == 1:
                    content = ''
                    for node in transform['result']:
                        content = content + node['content']
                    return content
                else:
                    return 'APIException'
            else:
                return jsonStr

            logging.debug(transform)
            # 检查
        except Exception as e:
            logging.error(e)
            return e

if __name__ == '__main__':
    print(SouGoOcr.trans('screenShot.jpg'))
