# swapi_caching_server

## Offline demo and current scope

 Only a license existed. The demo implements an in-memory TTL cache over two local character fixtures and shows a miss followed by a hit. This explicitly labeled demo is a local prototype; it does not
 contact external services, use credentials, or persist data between executions.
 Requires Python 3.10+ and optionally Make. From this repository root:

 ```sh
 make demo
 python3 demo.py --help
 # Pass options: make demo ARGS="--help"
 ```

 The root Dockerfile runs this offline demo only. With Docker running:

 ```sh
 docker build -t swapi-caching-server:demo .
 docker run --rm swapi-caching-server:demo
 ```

 Docker's first build needs access to the Python base image registry.


## Concrete remaining work

- [ ] Implement the actual HTTP server and SWAPI client with timeouts and structured errors.
- [ ] Bound the cache, define expiry/eviction policy, and avoid caching upstream failures.
- [ ] Add concurrent request coalescing, cache metrics, and HTTP integration tests.
