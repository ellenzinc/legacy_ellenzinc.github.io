#!/usr/bin/python

#=====================================================================================
# conversion from .bib file to Jekyll collection files (ver 1.0) 
# 
# Copyright (c) <2015> <Haining Wang>
# https://github.com/ellenzinc/

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



# usage example
#   bib2jekyllcol("st_ref.bib","./pub/")
#=====================================================================================



import bibtexparser
import os

# function parse names for bib authors
def parse_authors(authorStr):
    # parse author's names and output authors names in format of 
    # H. Wang (or Haining Wang depending on wether full name is provided)
    authors = authorStr.split(" and ");
    for idx in range(len(authors)):
        author = authors[idx].split(", ");
        if len(author) == 2:
            authors[idx] = author[1] + " " + author[0]    
    author_str = ""
    if len(authors) > 1:
        for idx in range(len(authors)-1):
            author_str += authors[idx]
            author_str += ", "
        author_str = author_str + "and " + authors[-1]
    else:
        author_str = authors[0]
    return author_str



# function bib2jekyllcol
def bib2jekyllcol (inputFile, outputDir):
    "This prints the bibtex file to output directory as jekyll collection folder(s)" 
           
    # read and parse bib file
    with open(inputFile) as bibtex_file:
        bibtex_str = bibtex_file.read()
         
    bib_database = bibtexparser.loads(bibtex_str)  
    
    # type names:
    type_list = ["type", "title", "author", "journal", "volume", "number",
                  "year", "month", "doi", "pages", "publisher", "booktitle"]
    
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    for entry in bib_database.entries:
        with open(outputDir+entry["id"]+'.md','w') as f:
            f.write("---\n")
            for bib_type in type_list:                
                if(entry.has_key(bib_type)):
                    if bib_type == "author":           
                        f.write(bib_type +": \"" +  parse_authors(entry[bib_type])+"\"\n")
                    else:
                        f.write(bib_type+": \""+entry[bib_type] + "\"\n")     
                else:
                    f.write(bib_type + ": \"" + "\"\n")                                                                
            f.write("---")
        

    


