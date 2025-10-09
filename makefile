.PHONY: run

run:
	export $$(cat .env | xargs) && uv run python main.py
