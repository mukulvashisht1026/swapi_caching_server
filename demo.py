"""Offline demonstration; no external services or credentials required."""
import argparse, json, time

class Cache:
    def __init__(self, ttl, clock=time.monotonic):
        self.ttl, self.clock, self.values, self.loads = ttl, clock, {}, 0

    def get(self, key):
        now = self.clock()
        if key in self.values and self.values[key][0] > now:
            return {"hit": True, "data": self.values[key][1]}
        self.loads += 1
        fixtures = {"1": {"name": "Luke Skywalker", "source": "local fixture"},
                    "2": {"name": "C-3PO", "source": "local fixture"}}
        if key not in fixtures: raise KeyError(key)
        value = fixtures[key]
        self.values[key] = (now + self.ttl, value)
        return {"hit": False, "data": value}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Offline TTL cache demonstration using local character fixtures.")
    p.add_argument("--person", choices=["1", "2"], default="1")
    p.add_argument("--ttl", type=int, default=60)
    a = p.parse_args()
    if a.ttl <= 0: p.error("ttl must be positive")
    cache = Cache(a.ttl)
    print(json.dumps({"mode": "mock; no HTTP server or upstream request", "requests": [cache.get(a.person), cache.get(a.person)],
                      "fixture_loads": cache.loads}, indent=2))
