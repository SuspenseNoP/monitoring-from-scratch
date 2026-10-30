from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import psutil

app = FastAPI()


class CPU:
    metric_name = "cpu_percent"
    type = "gauge"

    def get_percent(self):
        return psutil.cpu_percent()


class Memory:
    metric_name = "memory_percent"
    type = "gauge"

    def get_percent(self):
        return psutil.virtual_memory().percent


cpu = CPU()
memory = Memory()


def render_metric(*args):
    metrics = []
    for item in args:
        metric = f"# HELP {item.metric_name} show {item.metric_name} usage\n# TYPE {item.metric_name} {item.type}\n{item.metric_name} {item.get_percent()}"
        metrics.append(metric)
    return "\n".join(metrics)


@app.get("/metrics", response_class=PlainTextResponse)
async def metric():
    return render_metric(cpu, memory)
