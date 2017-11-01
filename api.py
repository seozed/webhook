# -*- coding:utf-8 -*-

import requests
import config

class LinkAPI(object):

    appid = config.APPID
    root_url = "http://api.shenjian.io/?appid="
    account = config.ACCOUNT

    def temporaryToPermant(self, url):
        """
        临时链接转换为永久链接
        :param url: temporary link
        :return: permant link
        """
        params = {
            "url": url,
            "account": self.account
        }
        response = requests.post(self.root_url + self.appid, data=params)
        item = response.json()

        if self.vailData(item):
            return item['data']["article_origin_url"]

    def vailData(self, data):
        if data['error_code'] == 0:
            return True

if __name__ == '__main__':
    api = LinkAPI()
    url = "https://mp.weixin.qq.com/s?src=11&timestamp=1509342128&ver=483&signature=DkbUCG3rOoMiJqzkInk2hdhvRSILVWgxHJdGZgIOv0JQyx2q*-mz*OowyHHYg2PRG2nHbLLvJPU7NEi0XUz761VI7KgNqid-Y-IkNjhgUIrYYcYYWyZZ7d-9u7abCDQs&new=1"
    data = api.temporaryToPermant(url)

