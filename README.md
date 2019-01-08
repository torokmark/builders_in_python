# Builders in Python

Demo repo to the builder post (https://torokmark.github.io/2019/01/08/builders-in-python.html)

# Usage of multibuilder

```python
print(ResponseBuilder()
    .header()
      .add('Access-Control-Allow-Origin', '*')
      .add('Accept', '*')
    .body()
      .add('body', json.dumps('hello', default=str))
    .status(204))
```



