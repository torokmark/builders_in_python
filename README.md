# Response Builder

Is a simple tool to create http responses without hustle!

# Usage

```python
print(ResponseBuilder()
    .header()
      .add('Access-Control-Allow-Origin', '*')
      .add('Accept', '*')
    .body()
      .add('body', json.dumps('hello', default=str))
    .status(204))
```



