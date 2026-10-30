from exporter.main import render_metric


class FakeMetric:
    metric_name = "fake"
    type = "gauge"

    def get_percent(self):
        return 33


fake = FakeMetric()


def test_metric_render():
    assert (
        render_metric(fake) == "# HELP fake show fake usage\n# TYPE fake gauge\nfake 33"
    )
