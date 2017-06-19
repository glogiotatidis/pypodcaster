install:
	python setup.py install

uninstall:
	python setup.py install --record pypodcaster-files.txt
	cat pypodcaster-files.txt | xargs rm -rf
	rm -f pypodcaster-files.txt

build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

upload:
	gpg --detach-sign -a dist/pypodcaster-*.tar.gz
	twine upload dist/pypodcaster-*

clean:
	rm -rf build dist pypodcaster.egg-info
