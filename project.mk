# Custom Makefile
# Add your custom makefile commands here
#
PROJECT_NAME := test-pymongoarrow

test:
	python test.py

edit:
	$(EDITOR) test.py
