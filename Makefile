.PHONY: clean-dangling-images setup build run build-run build-cold

-include .env

$(eval REGISTRY=$(shell grep '* Registry:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))
$(eval REPOSITORY=$(shell grep '* Repository name:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))
$(eval VERSION=$(shell grep '* Current version:' README.md | awk -F ':' '{print $$2}' | sed 's/ //g'))

clean-dangling-images:
	docker rmi -f $$(docker images -f 'dangling=true' -q)

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
	-v $(PWD)/data:/usr/src/data \
		$(REGISTRY)/$(REPOSITORY):$(VERSION)

run-prod:
	@docker run -it \
	-e PORT=8000 \
	-p 8000:8000 \
		desholmes/covid-19-uk-api:1.0.1

build-run:
	@make build
	@make run

build-cold:
	@make setup
	@make build-run