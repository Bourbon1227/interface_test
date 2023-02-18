# 设置日志
import json
import logging, logging.handlers
import os

from config import DIR_PATH


def get_log():
    # 设置格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 创建处理器
    log_file = DIR_PATH + os.sep + "log" + os.sep + "select.log"
    clq = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=3)

    # 设置格式处理器
    clq.setFormatter(formatter)
    # 创建日志器
    logger = logging.getLogger()
    # 将日志器添加到处理器
    logger.addHandler(clq)
    # 设置日志级别
    logger.setLevel(logging.INFO)


# 公共断言方法
def common_assert(response, response_code=None, sp=None):
    try:
        # 断言 response_code
        if response_code:
            assert response_code == str(response.status_code), "断言失败，期望结果为：{}，实际结果为：{}".format(response_code,
                                                                                               response.status_code)
        # 断言运营商
        if sp:
            assert sp == response.json().get("data", {}).get("sp"), "断言失败，期望结果为：{}，实际结果为：{}".format(sp,
                                                                                                    response.json().get(
                                                                                                        "sp"))
    except Exception:
        raise


# 读取json文件工具
def read_json(filename, type):
    file_path = DIR_PATH + os.sep + "data" + os.sep + filename
    with open(file_path, mode="r", encoding="utf-8") as f:
        json_data = json.load(f)
        list_data = []
        for data in json_data.get(type):
            list_data.append(tuple(data.values())[1:])
        return list_data


if __name__ == '__main__':
    print(read_json("select_phone.json", "phone"))
