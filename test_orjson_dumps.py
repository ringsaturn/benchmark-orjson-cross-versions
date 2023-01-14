import orjson

with open("github.json") as f:
    content = f.read()

data = orjson.loads(content)


def _test_loads():
    _ = orjson.loads(content)


def test_loads(benchmark):
    benchmark(_test_loads)


def _test_dumps():
    _ = orjson.dumps(data)


def test_dumps(benchmark):
    benchmark(_test_dumps)
