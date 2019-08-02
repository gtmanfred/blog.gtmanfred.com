build:
	for talk in $(shell find . -maxdepth 1 -mindepth 1 -type d); do \
		make -C $$talk html; \
	done

clean:
	rm -rf $(shell find . -type d -name _build)
