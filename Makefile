##

define HELP
Start installing pip packages
endef
export HELP

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:.* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

clean: # clean
	rm -fr env

venv: # install virtual environment
	virtualenv env

run: # run
	@echo $$HELP
	@echo
	test -d env || virtualenv env
	source env/bin/activate && pip install -r requirements.txt && nose2
