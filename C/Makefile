.PHONY: login build run

IMAGE:=ubuntu-c

login:
	docker run -it --rm --entrypoint neofetch $(IMAGE) bash
	docker run -it -v $(PWD):/home/zelda $(IMAGE) bash

run: build
	docker run -it $(IMAGE) bash

build:
	docker build --tag $(IMAGE) .
