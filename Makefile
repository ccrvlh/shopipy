file := VERSION
version := $(shell cat ${file})

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$))" | xargs rm -rf