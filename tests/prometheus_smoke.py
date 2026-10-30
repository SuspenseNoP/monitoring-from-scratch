import requests
import sys


def get_status_code():
    r = requests.get("http://localhost:9090/-/healthy", timeout=5)
    return r.status_code


def fetch_up():
    r = requests.get("http://localhost:9090/api/v1/query?query=up", timeout=5)
    return r.json()


def parse_down(data):
    down = []
    result = data["data"]["result"]
    for item in result:
        value = item["value"][1]
        job = item["metric"]["job"]
        if value != "1":
            down.append(job)
    return down


def main():
    try:
        status = get_status_code()
        data = fetch_up()
        down = parse_down(data)
    except requests.exceptions.RequestException:
        print("Unavailable")
        sys.exit(1)
    if status == 200 and not down:
        print("OK!")
        sys.exit(0)
    else:
        for member in down:
            print(member)
        sys.exit(1)


if __name__ == "__main__":
    main()
