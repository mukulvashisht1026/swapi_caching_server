
.DEFAULT_GOAL := demo
 IMAGE ?= swapi-caching-server:demo
 .PHONY: build run
 build:
 	docker build -t $(IMAGE) .
 run:
 	docker run --rm $(IMAGE) $(ARGS)

.PHONY: demo demo-help
demo:
	python3 demo.py $(ARGS)
demo-help:
	python3 demo.py --help
