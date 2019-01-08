#!/usr/bin/env python

import json

class Builder:
    def add(self, key, value): pass
    def build(self): pass
    def status(self, code): pass

class HeaderBuilder(Builder):
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

class BodyBuilder(Builder):
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

class ResponseBuilder:

    def __init__(self):
        self.__header = HeaderBuilder()
        self.__body = BodyBuilder()
        self.__body.set_header(self.__header)
        self.__header.set_body(self.__body)

    def header(self):
        return self.__header

    def body(self):
        return self.__body

if __name__ == "__main__":
    print(ResponseBuilder()
            .header()
                .add('Access-Control-Allow-Origin', '*')
                .add('Accept', '*')
            .body()
                .add('body', json.dumps('hello', default=str))
            .status(204))

    print(ResponseBuilder()
            .header()
                .add('Age', '12')
                .add('Accept', '*')
            .body()
                .add('body', 'message comes here!')
            .header()
                .add('Access-Control-Allow-Origin', '*')
            .build()) # status is default to 200
