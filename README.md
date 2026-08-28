# Project: Monitoring System

## Exporter
A Python application that renders metrics from host

- cpu_percent; gauge
- memory_percent; gauge

The exporter has its own Dockerfile and runs from docker-compose.yaml file in the root
Prometheus scrapes python_app as a target


## Smoke tests

- What it is: Smoke test that checks Prometheus targets are alive
- Prerequisites: Running Prometheus (reachable on port 9090)
- Setup: Create venv, install dependencies from requirements.txt
- Run: `python prometheus_smoke_test.py` (code 0 means healthy, code 1 - something down)
- Test: run `python -m pytest`

## TODO:
- [ ] Split dependencies between `requirements.txt` and `requirements-dev.txt`

## Changelog

- Rewrote smoke-test.ps1 to Python. Dropped smoke-test.ps1