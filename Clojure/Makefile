
.PHONY:	shell
shell:
	$(MAKE) build
	$(MAKE) run

.PHONY: build
build:
	docker build -t clojure-dev .

.PHONY: run
run:
	docker run -it -v $(shell pwd):/tmp clojure-dev bash