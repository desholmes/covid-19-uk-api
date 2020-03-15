.PHONY: setup build run build-run build-cold

-include .env

$(eval REGISTRY=$(shell grep '* Registry:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))
$(eval REPOSITORY=$(shell grep '* Repository name:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))
$(eval VERSION=$(shell grep '* Current version:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))

setup:
	cp ./.env-dist ./.env

build:
	@docker build \
		--no-cache \
		-f Dockerfile \
		-t $(REGISTRY)/$(REPOSITORY):$(VERSION) .

run:
	@docker run -it \
	-e PORT=$(PORT) \
	-e DEBUG=$(DEBUG) \
	-e DEV=$(DEV) \
	-e SECRET_KEY=$(SECRET_KEY) \
	-e QA=$(QA) \
	-p $(PORT):$(PORT) \
	-v $(PWD)/covid_19_uk:/usr/src/covid_19_uk \
		$(REGISTRY)/$(REPOSITORY):$(VERSION)

build-run:
	@make build
	@make run

build-cold:
	@make setup
	@make build-run