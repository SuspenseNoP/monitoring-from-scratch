from exporter.exporter import render_down


class FakeMetric:
    metric_name = "fake"
    type = "gauge"

    def get_percent(self):
        return 33


fake = FakeMetric()


def test_metric_render():
    assert (
        render_down(fake) == "# HELP fake show fake usage\n# TYPE fake gauge\nfake 33"
    )
