.PHONY: install tests docs quality

install:
	@python -m build && \
	pip install dist/nexora-$(version)-py3-none-any.whl

tests:
	@python -m pytest tests/test1 && \
	python -m pytest tests/test2/test_dummy.py --param 1

docs:
	@cd docs && \
	chmod u+x docs.sh && \
	./docs.sh && \
	cd ..

quality:
	pre-commit install && \
	pre-commit run --all-files
