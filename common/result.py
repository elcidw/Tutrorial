class Result:

    def send_to(self, code, msg, data):
        ret = {}
        ret['code'] = code
        ret['msg'] = msg
        ret['data'] = data
        return ret

    def succ(self, data):
        return self.send_to(200, "Success", data)

    def fail(self, data):
        return self.send_to(400, "failure", data)

    def fail(self, code, msg, data):
        return self.send_to(code, msg, data)
