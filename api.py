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


import requests

class E7liuxueSQL(object):

    _TOKEN = "123456789abcdefg"
    _ROOT_URL = "http://data.100zhaosheng.com/api/"

    def push(self, url, data):
        headers = {
            'API-AUTH-TOKEN': self._TOKEN,
            'Accept-Language': 'zh-CN,en,*'
        }
        response = requests.post(url, data=data, headers=headers)
        return response

    def pushToWeixin(self, item):
        return self.push(url=self._ROOT_URL + 'weixin', data=item)

    def pushToWeibo(self, item):
        return self.push(url=self._ROOT_URL + 'weibo', data=item)
