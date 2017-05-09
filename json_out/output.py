import json

# json结果处理封装
import traceback


class JsonOuter:
    __success_code = 1
    __success_status = 'ok'
    __fail_code = 2
    __fail_status = 'fail'
    __data_code = 3
    __data_status = 'data'

    # 返回成功json数据字符串
    def success(self, message):
        data = {}
        data['code'] = self.__success_code
        data['status'] = self.__success_status
        data['message'] = message
        return json.dumps(data)

    # 返回成功json数据字符串
    def fail(self, message):
        data = {}
        data['code'] = self.__fail_code
        data['status'] = self.__fail_status
        data['message'] = message
        return json.dumps(data)

    # 输出数据
    def data(self, d):
        data = {}
        data['code'] = self.__data_code
        data['status'] = self.__data_status
        data['data'] = d
        return json.dumps(data)

    # 解析json
    def parse(self, json_str):
        try:
            data = json.load(json_str)
        except Exception as err:
            traceback.print_exc()
            print(err)
            data = False
        return data
