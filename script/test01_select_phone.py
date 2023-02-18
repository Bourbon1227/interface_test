import json
import logging
import os

import pytest
import requests
from werkzeug.utils import redirect

from api.api_select import ApiSelect
from config import DIR_PATH
from utils import common_assert, read_json


class TestSelect:
    def setup(self):
        # 获取session
        self.session = requests.session()
        # 实例化封装Select对象
        self.select = ApiSelect(self.session)

    def teardown(self):
        # 关闭session
        self.session.close()

    # 1.查询手机号信息 接口测试方法
    @pytest.mark.parametrize(("phone", "expect_response_code", "sp"), read_json("select_phone.json", "phone"))
    def test01_select_phone(self, phone, expect_response_code, sp):
        response = self.select.select_phone(phone)

        try:
            logging.info("查询手机号运营商的结果为：{}".format(response.json()))
            common_assert(response, response_code=expect_response_code)
            common_assert(response, sp=sp)
        except Exception as e:
            # 错误日志
            logging.error(e)
            raise
