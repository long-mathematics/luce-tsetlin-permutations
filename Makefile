.PHONY: all pdf check test verify
all: pdf
pdf:
	python3 scripts/build.py
check:
	python3 scripts/build.py --check
test:
	python3 -m unittest discover -s tests -v
verify:
	python3 scripts/verify.py
