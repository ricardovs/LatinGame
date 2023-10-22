# Makefile for development

#Varibles
ENV_DIR = venv
ACTIVATE_MSG = You will have to run: source ./$(ENV_DIR)/bin/activate

#RULES
run: | $(ENV_DIR)
	@if [ -z ${VIRTUAL_ENV} ]; then echo "$(ACTIVATE_MSG)"; else python3 main.py; fi

$(ENV_DIR):
	python3 -m venv ./$(ENV_DIR)
	@echo "$(ACTIVATE_MSG)"

depends:
	@if [ -z ${VIRTUAL_ENV} ]; then echo "$(ACTIVATE_MSG)"; else pip3 install -r requirements.txt; fi

clear:
	@if [ -z ${VIRTUAL_ENV} ]; then rm -r ./$(ENV_DIR); else echo "You will have to run: deactivate"; fi
