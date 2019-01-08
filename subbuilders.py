#!/usr/bin/env python

class Builder:
    def build(self): pass

class HeaderBuilder(Builder):
    def __init__(self):
        self._header = {}

    def add(self, key, value):
        self._header[key] = value
        return self

    def build(self):
        return self._header

class BodyBuilder(Builder):
    def __init__(self):
        self._body = []

    def add(self, content):
        self._body.append(content)
        return self

    def build(self):
        return self._body

class ResponseBuilder(Builder):
    def __init__(self):
        self._header = None
        self._body = None
        self._status = None

    def header(self, header):
        self._header = header
        return self

    def body(self, body):
        self._body = body
        return self

    def status(self, status):
        self._status = status
        return self

    def build(self):
        ret = {}
        ret['statusCode'] = self._status
        ret['header'] = self._header
        ret['body'] = self._body
        return ret

if __name__ == '__main__':
    print(ResponseBuilder()
            .header(
                HeaderBuilder()
                    .add('Accept', '*')
                    .add('Age', 12)
                    .build()
            )
            .body(
                BodyBuilder()
                    .add('some message comes here')
                    .add('another message here...')
                    .build()
            )
            .status(200)
            .build()
    )
