import unittest
import main
import time
import tempfile
import json


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):

        self.app = main.app.test_client()



    def test_link_api(self):
        """
        测试用例：临时链接转换API
        :return:
        """
        from api import  LinkAPI
        link = LinkAPI()
        url = "https://mp.weixin.qq.com/s?src=11&timestamp=1509342128&ver=483&signature=DkbUCG3rOoMiJqzkInk2hdhvRSILVWgxHJdGZgIOv0JQyx2q*-mz*OowyHHYg2PRG2nHbLLvJPU7NEi0XUz761VI7KgNqid-Y-IkNjhgUIrYYcYYWyZZ7d-9u7abCDQs&new=1"
        result = link.temporaryToPermant(url)
        self.assertTrue("mp.weixin.qq.com/s" in result)

    def test_record_wx(self):
        """
        测试插入数据
        :return:
        """
        data = {
            'url': 'http://mp.weixin.com/#example',
            'weixin_tmp_url': 'https://mp.weixin.qq.com/s?src=11&timestamp=1509342128&ver=483&signature=DkbUCG3rOoMiJqzkInk2hdhvRSILVWgxHJdGZgIOv0JQyx2q*-mz*OowyHHYg2PRG2nHbLLvJPU7NEi0XUz761VI7KgNqid-Y-IkNjhgUIrYYcYYWyZZ7d-9u7abCDQs&new=1',
        }

        params = {
            'url': 'http://www.example.com',
            'timestamp': '1500000000000',
            'sign': 'some sign',
            'sign2': 'some sign2',
            'data': json.dumps(data),
            'event_type': 'data.new',
            'crawl_time': '1500000000000',
            'data_key': 'some key',
            'pk': 'some pk'
        }

        response = self.app.post('/record_weixin', data=params)
        self.assertTrue(response.data)

if __name__ == '__main__':
    unittest.main()
