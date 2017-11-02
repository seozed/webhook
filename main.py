# -*- coding:utf-8 -*-
from flask import request, Flask
import config
import json
from pipeline import MongoPipeline
import api

app = Flask(__name__)
db = MongoPipeline(config.MONGO_URI, config.MONGO_DATABASE)
dbApi = api.E7liuxueSQL()


@app.route('/record_weixin', methods=['POST'])
def record_weixin():
    """
    微信webhooks API，神箭手专用
    :return: data_key
    """

    formData = request.form
    item = json.loads(formData['data'])
    weixin_temp_url = item['weixin_tmp_url']
    item['weixin_permant_url'] = tmpLinkToPermantLink(weixin_temp_url)
    save_data(item)
    return formData['data_key']


def save_data(data, collection=None):
    if not collection:
        collection = "weixinArticle"
    db.process_item(data, collection)

def tmpLinkToPermantLink(url):


    link = api.LinkAPI()
    new_url = link.temporaryToPermant(url)
    return new_url

@app.route('/record_weibo', methods=['POST'])
def record_weibo():

    formData = request.form
    try:
        item = json.loads(formData['data'])
        item['source_content'] = json.dumps(item.pop("origin"))
        response = dbApi.pushToWeibo(item)

    finally:
        return formData['data_key']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)
