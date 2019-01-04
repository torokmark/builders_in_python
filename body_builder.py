
class BodyBuilder:
    def __init__(self):
        self._body = {}

    def add(self, key, value):
        self._body[key] = value
        return self

    def header(self):
        return self._header

    def build(self):
        return self.status(200)

    def status(self, code):
        ret = {}
        ret['status'] = code
        ret['header'] = self._header.__dict__.get('_header')
        ret['body'] = self._body
        return ret


    def set_header(self, header):
        self._header = header


