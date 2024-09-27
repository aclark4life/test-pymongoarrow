# Custom Makefile
# Add your custom makefile commands here
#
# PROJECT_NAME := my-new-project

test:
	python test.py

edit:
	$(EDITOR) test.py
