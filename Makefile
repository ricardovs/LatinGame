# Makefile for development

#Varibles
ENV_DIR = venv

#RULES
run: | $(ENV_DIR) requirements.txt
	@bash run.sh

$(ENV_DIR):
	@python3 -m venv ./$(ENV_DIR)
	@chmod +x run.sh
	@chmod +x depends.sh
	@make depends

requirements.txt, depends:
	@bash depends.sh

clear:
	@rm -r ./$(ENV_DIR)
	@chmod -x run.sh
	@chmod -x depends.sh
