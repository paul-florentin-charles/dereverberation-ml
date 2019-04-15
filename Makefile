REQ = requirements.txt

MAIN = main.py
DEMO = demo.py
CLEAN = clean.py

help:
	@echo "INSTALL w/ pip: make install"
	@echo "RUN: make run dry=path/to/dry fx=path/to/fx [wet=output/path]"
	@echo "DEMO: make demo"
	@echo "CLEAN: make clean[all]"

install:
	@sudo pip3 install -r $(REQ)

run: 
	@python3 $(MAIN) $(dry) $(fx) $(wet)

demo: 
	@python3 $(DEMO)

clean:
	@rm -rf `find -name "*~" ; find -name "#*#" ; find -name ".#* ; "find -name "*.pyc" ; find -name "__pycache__"`

cleanall:
	@python3 $(CLEAN)
	@rm -rf `find -name "*~" ; find -name "#*#" ; find -name ".#* ; "find -name "*.pyc" ; find -name "__pycache__"`
