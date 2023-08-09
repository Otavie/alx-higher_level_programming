#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("obj"):str.find("pro")] + str[str.find("with"):str.find("very")] + str[:len("Python")]
print(str)
