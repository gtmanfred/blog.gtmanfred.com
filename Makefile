pelican:
	pipenv run pelican content -vvv -o output -s pelicanconf.py

sphinx:
	make -C talks build

build: pelican sphinx

publish: build
	mkdir output/talks/
	for talk in $(shell find talks/* -type d -depth 0); do \
		mv $$talk/_build/html output/$$talk; \
	done

clean:
	make -C talks clean
	rm -rf output
