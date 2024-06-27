git:
	git pull
	git add -A
	git commit 
	git push

install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	python -m textblob.download_corpora

format:
	black *.py

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv --cov=wiki_phrases --cov=nlplogic test_*.py

docker:
	docker run -p 127.0.0.1:8083:8081 e5e2ce2a8224

all: install format lint test git