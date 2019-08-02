build:
	for talk in $(shell find . -type d -depth 1); do \
		make -C $$talk html; \
	done

clean:
	rm -rf $(shell find . -type d -name _build)
