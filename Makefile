

help: ## Help Command
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean: ## clear screen
	clear

install: clean ## Install yaml-editor
	rm -rf Yaml_Editor.egg-info/ build/ dist/
	pip install .
