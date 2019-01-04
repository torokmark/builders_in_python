#!/usr/bin/env python

import json
from response_builder import ResponseBuilder

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

