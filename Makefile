default:
	@echo "Type \"make help\" to get started"

install:
	@sudo pip3 install -r requirements.txt

run: 
	@python3 main.py $(dry) $(fx) $(wet)

demo: 
	@python3 demo.py

clean:
	@rm -rf `find -name "*~" ; find -name "#*#" ; find -name "*.pyc" ; find -name "__pycache__"`

cleanall: clean
	@python3 clean.py

help:
	@echo "INSTALL w/ pip: make install"
	@echo "RUN: make run dry=path/to/dry fx=path/to/fx [wet=output/path]"
	@echo "DEMO: make demo"
	@echo "CLEAN: make clean[all]"
