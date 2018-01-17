#!/usr/bin/python

import cgi,cgitb,math
cgitb.enable()

print 'Content-type:text/html'
print ''

print '<html>'
print '<head><title>Simple Calculator</title></head>'
print '<body>'
print '<h1>Calculator</h1>'
form = cgi.FieldStorage()
if form.getvalue("x") and form.getvalue("y"):
	x = form.getvalue("x")
	print 'x = ' + x + '<br />'
	y = form.getvalue("y")
	print 'y = ' + y + '<br />'
if form.getvalue("x") and form.getvalue("y") and form.getvalue("operator"):
	x = form.getvalue("x")
	y = form.getvalue("y")
	operator = form.getvalue("operator")
	if operator=="+": ans = str(int(x)+int(y))
	elif operator=="-": ans = str(int(x)-int(y))
	elif operator=="*": ans = str(int(x)*int(y))
	elif operator=="/": ans = str(int(x)/int(y))
	print '<h3>x ' + operator + ' y = ' + ans + '</h3><br />'

print '<form method="post" action="calculator.py">'
print '<p>x: <input type="number" name="x"/></p>'
print '<p>y: <input type="number" name="y"/></p>'
print '<input type="radio" name="operator" value="+" /> +'
print '<input type="radio" name="operator" value="-" /> -'
print '<input type="radio" name="operator" value="*" /> *'
print '<input type="radio" name="operator" value="/" /> /'
print '<br /><input type="submit" value="Submit" />'
print '</form>'
print '</body>'
print '</html>'
