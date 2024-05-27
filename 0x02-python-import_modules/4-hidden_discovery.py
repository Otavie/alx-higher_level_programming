#!/usr/bin/python3

import importlib.util as iu
import sys
import os

def main():
    #Load the compiled module
    module_name = "hidden_4"
    file_path = "./hidden_4.pyc"
    
    # Load the module from the given file path
    spec = iu.spec_from_file_location(module_name, file_path)
    module = iu.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Get the name defined in the module
    names = dir(module)
    
    # Filter out names that start with __ and sort the remaining names
    filtered_names = sorted(name for name in names if not name.startswith('__'))
    
    # Print each name on a new line
    for name in filtered_names:
        print(name)
        
if __name__ == "__main__":
    main() 
    
# This code is not over yet