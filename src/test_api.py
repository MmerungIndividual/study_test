import pytest
import json
import requests
from .const import *
class Test_httpbin():

    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        res= requests.get(url)
        print(res.headers)
        res_data = json.loads(res.text)
        print(res_data)
        assert 200 == res.status_code
        assert LOCAL_IP == res_data['origin']
    def post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name":"yourname","pwd":123456}
        res = requests.post(url,data=post_data)
        print(res.headers)
        print(res.text)
        res_data = res.json()
        assert 200 == res.status_code
        assert post_data["name"] == res_data["form"]["name"]
        assert post_data["name"] == res_data["form"]["pwd"]