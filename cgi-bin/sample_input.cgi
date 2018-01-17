#!/usr/bin/python3

# Sample input using CGI

# Error if access via
# http://localhost:8000/cgi-bin
# http://localhost:8000/cgi-bin/sample_input.cgi

print("Content-Type: text/plain") # NOT HTML? (to be modified)
print()

# get input from request URL

import cgi

input = cgi.FieldStorage()

x = input["x"].value
y = input["y"].value

print("x= ", x)
print("y= ", y)

print("x+y= ", x+y) # as expected?

#print("<b>To be modified</b>")
