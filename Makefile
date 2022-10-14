pelican:
	pelican content -vvv -o output -s pelicanconf.py

sphinx:
	make -C talks build

build: pelican sphinx

publish: build
	mkdir output/talks/
	for talk in $(shell find talks/ -maxdepth 1 -mindepth 1 -type d); do \
		mv $$talk/_build/html output/$$talk; \
	done
	# github pages ignores files starting with an underscore
	# https://help.github.com/en/articles/files-that-start-with-an-underscore-are-missing
	touch output/.nojekyll

clean:
	make -C talks clean
	rm -rf output
