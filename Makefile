SHELL := /bin/sh

BOT_IMAGE = alekspog/stepik-telegram-bot

.PHONY: docker-build
docker-build: ## Build docker image
	docker build -t ${BOT_IMAGE}:stable .

.PHONY: docker-push
docker-push: ## Push docker image
	docker push ${BOT_IMAGE}:stable	

.PHONY: docker-run
docker-run: ## Push results to the channel with docker container
	docker run --rm \
	-e API_ID=${API_ID} \
	-e API_HASH=${API_HASH} \
	-e BOT_TOKEN=${BOT_TOKEN} \
	-e CHANNEL_ID=${CHANNEL_ID} \
	-e COURSE_ID=${COURSE_ID} \
	-e CLIENT_ID=${CLIENT_ID} \
	-e CLIENT_SECRET=${CLIENT_SECRET} \
	${BOT_IMAGE}:stable

.PHONY: run
run: ## Push results to the channel
	python send_reviews.py

# Help
.PHONY: help
help: ## This help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
