
from header_builder import HeaderBuilder
from body_builder import BodyBuilder

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



