default:
	@echo "Type \"make help\" to get started"

install:
	@sudo pip3 install -r requirements.txt

demo: 
	@python3 demo.py 

clean:
	@rm -rf `find -name "*~"`

cleanall: clean
	@rm -rf `find -name "__pycache__"`

help:
	@echo "INSTALL /w pip: make install"
	@echo "DEMO: make demo"
	@echo "CLEAN: make clean[all]"
