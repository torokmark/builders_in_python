
class HeaderBuilder:
    def __init__(self):
        self._header = {}

    def add(self, key, value):
        self._header[key] = value
        return self

    def body(self):
        return self._body

    def build(self):
        return self.status(200)

    def status(self, code):
        ret = {}
        ret['status'] = code
        ret['header'] = self._header
        ret['body'] = self._body.__dict__.get('_body')
        return ret

    def set_body(self, body):
        self._body = body
 
