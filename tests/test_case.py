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


    def test_record_weibo(self):


        data = {'origin': {'origin_post_video': '', 'origin_attitudes_count': '', 'origin_userid': '', 'origin_isLongText': '', 'origin_post_time': '', 'origin_post_img': [], 'origin_source': '', 'origin_nickname': '', 'origin_avatar': '', 'origin_reposts_count': '', 'origin_post_content': '', 'origin_comments_count': ''}, 'userid': '2823209931', 'followers_count': '51181', 'post_content': 'The end ，is only the beginning.刚刚结束了一段恋情，同时也意味着新的恋情即将开始。伤心不再属于我，爱情之箭已经悬在空中。 \u200b\u200b\u200b', 'nickname': '新东方雅思考试', 'comments_count': '0', 'comments': [], 'avatar': 'https://tvax3.sinaimg.cn/crop.0.0.180.180.180/a846c3cbly8fjvv9h95kxj2050050aav.jpg', 'video': '', 'isLongText': 'false', 'follow_count': '146', 'post_time': '1346652729', 'reposts_count': '0', 'url': 'http://m.weibo.cn/2823209931/3486176579156771', 'hot_comments': [], 'is_repost': 'false', 'pics': ['https://ww3.sinaimg.cn/large/a846c3cbjw1dwjayk98p8j.jpg'], 'source': '微博 weibo.com', 'reposts': [], 'post_content_txt': 'The end ，is only the beginning.刚刚结束了一段恋情，同时也意味着新的恋情即将开始。伤心不再属于我，爱情之箭已经悬在空中。 \u200b\u200b\u200b', 'attitudes_count': '0'}

        params = {
            'data': json.dumps(data),
            'crawl_time': '1509549077',
            'data_key': '796190:419054',
            'event_type': 'data.new',
            'pk': '389504bb443a7c0e62dea703b4215375',
            'sign': 'a243bcdd951b6258a1249779f98d4f43',
            'sign2': '352ef93105033a5244b89bd6583cce5b',
            'timestamp': '1509585942',
            'url': 'http://m.weibo.cn/2823209931/3486176579156771'
        }
        response = self.app.post('/record_weibo', data=params)
        self.assertTrue(response.data)

if __name__ == '__main__':
    unittest.main()
