import logging

from config import BASE_URL


class ApiSelect:
    def __init__(self, session):
        # 初始化session
        self.session = session
        # 查询URL
        self.select_url = BASE_URL + "/phonearea.php?number={}"

    # 查询接口封装
    def select_phone(self, phone):
        response = self.session.get(self.select_url.format(phone))
        logging.info("查询手机号信息")
        return response

