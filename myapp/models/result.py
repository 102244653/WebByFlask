
class Result:

    @staticmethod
    def success(msg=None, data=None):
        res = {"code": 10000, "msg": "操作成功", "data": None}
        if msg:
            res["msg"] = msg
        if data:
            res["data"] = data
        return res

    @staticmethod
    def fail(msg=None, data=None):
        res = {"code": 99999, "msg": "操作失败", "data": None}
        if msg:
            res["msg"] = msg
        if data:
            res["data"] = data
        return res
