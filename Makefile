ifeq (, $(shell python -V ))
  $(error "PYTHON=$(PYTHON) not found in $(PATH)")
endif

PYTHON_VERSION_MIN=3.11
PYTHON_VERSION=$(shell python -c 'import sys; print("%d.%d"% sys.version_info[0:2])' )
PYTHON_VERSION_OK=$(shell python -c 'import sys;\
  print(int(float("%d.%d"% sys.version_info[0:2]) >= $(PYTHON_VERSION_MIN)))' )

ifeq ($(PYTHON_VERSION_OK),0)
  $(error "Need python $(PYTHON_VERSION) >= $(PYTHON_VERSION_MIN)")
endif

run:
	@echo "Running app"
	@python main.py

check:
	@echo "Everything is fine"
	@echo "Python version is $(PYTHON_VERSION)"

install:
	@echo "Installing requirements"
	@pip install -r requirements.txt	

install-package:
	@echo "Installing package"
	@echo "installing $(package)"
	@pip install $(package) && pip freeze | grep $(package) >> requirements.txt

add-at-requirements:
	@echo "Adding package to requirements"
	$(pip freeze | grep $(package) >> requirements.txt)
