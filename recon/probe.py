"""First recon probe: confirm we can reach the target and its API.

Juice Shop is an Angular SPA, so GET / only ever returns an empty shell
(<div id="app">) — a plain crawler can't see anything past that. Its real
attack surface lives behind /rest/* and /api/* JSON endpoints, which is
what we probe here instead. The real recon module (next step) will use
ZAP's spider, which runs a headless browser and can actually see what the
SPA renders.
"""

import requests

TARGET = "http://localhost:3000"

ENDPOINTS = [
    "/",
    "/rest/products",
    "/rest/admin/application-version",
    "/api/Users",
]


def probe(path: str) -> None:
    url = TARGET + path
    resp = requests.get(url, timeout=5)
    print(f"{resp.status_code}  {len(resp.content):>6} bytes  {url}")


if __name__ == "__main__":
    for endpoint in ENDPOINTS:
        probe(endpoint)
