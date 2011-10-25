README.md
=========

This simple script grabs all the papers from [ISMIR 2011](http://ismir2011.ismir.net/) and  downloads all them into the current directory. The filenames are of the form: `(paper_number).pdf`. Additionally a tsv file `metadata.tsv` will be created in the same directory. This file will be populated with metadata (paper number, title, authors) about each paper as they are downloaded.

Running the script is very simple. On a *nix (including mac osx) system, open a terminal and do the following:

	>mkdir ismirpapers
	>cd ismirpapers
	>python path/to/ismirpapers.py
	
and that's it. Tested in python 2.6 on Mac OS X 10.7, though I'm sure it will work in other systems, only standard python libraries required.  If someone gets it to work on Windows, let me know how and I'll add the instructions.