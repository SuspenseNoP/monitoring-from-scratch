from tests.prometheus_smoke import parse_down


def test_dead_target():
    fake = {
        "status": "success",
        "data": {
            "resultType": "vector",
            "result": [
                {
                    "metric": {
                        "__name__": "up",
                        "instance": "localhost:9090",
                        "job": "prometheus",
                    },
                    "value": [1755690000, "1"],
                },
                {
                    "metric": {
                        "__name__": "up",
                        "instance": "node-exporter:9100",
                        "job": "node",
                    },
                    "value": [1755690000, "0"],
                },
            ],
        },
    }
    assert parse_down(fake) == ["node"]


def test_all_up():
    fake = {
        "status": "success",
        "data": {
            "resultType": "vector",
            "result": [
                {
                    "metric": {
                        "__name__": "up",
                        "instance": "localhost:9090",
                        "job": "prometheus",
                    },
                    "value": [1755690000, "1"],
                },
                {
                    "metric": {
                        "__name__": "up",
                        "instance": "node-exporter:9100",
                        "job": "node",
                    },
                    "value": [1755690000, "1"],
                },
            ],
        },
    }
    assert parse_down(fake) == []
