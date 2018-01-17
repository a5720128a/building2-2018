#!/usr/bin/python

import cgi,cgitb,math
cgitb.enable()

print 'Content-type:text/html'
print ''

print '<html>'
print '<head><title>Sudoku</title>'
print '<style type="text/css">'
print 'td {border: 1px solid #000000; text-align: center; vertical-align: middle;}'
print 'input:disabled {background-color: #99CCFF;}'
print 'input {color: #000000;text-align: center;width: 48px;height: 48px;font-size: 24px;}'
print '</style>'
print '</head>'
print '<body>'
print '<div class="container">'
print '<h1>Sudoku</h1>'

form = cgi.FieldStorage()
if form.getvalue("c0")=="4" and form.getvalue("c3")=="6" and form.getvalue("c5")=="9" and form.getvalue("c6")=="7" and form.getvalue("c8")=="8" and form.getvalue("c9")=="5" and form.getvalue("c10")=="3" and form.getvalue("c13")=="8" and form.getvalue("c14")=="2" and form.getvalue("c16")=="4" and form.getvalue("c18")=="7" and form.getvalue("c20")=="9" and form.getvalue("c21")=="5" and form.getvalue("c23")=="4" and form.getvalue("c24")=="6" and form.getvalue("c27")=="8" and form.getvalue("c31")=="6" and form.getvalue("c32")=="5" and form.getvalue("c35")=="3" and form.getvalue("c37")=="6" and form.getvalue("c38")=="2" and form.getvalue("c39")=="3" and form.getvalue("c40")=="4" and form.getvalue("c41")=="7" and form.getvalue("c42")=="8" and form.getvalue("c43")=="9" and form.getvalue("c45")=="9" and form.getvalue("c48")=="1" and form.getvalue("c49")=="2" and form.getvalue("c53")=="6" and form.getvalue("c56")=="8" and form.getvalue("c57")=="4" and form.getvalue("c59")=="3" and form.getvalue("c60")=="5" and form.getvalue("c62")=="7" and form.getvalue("c64")=="9" and form.getvalue("c66")=="8" and form.getvalue("c67")=="5" and form.getvalue("c70")=="1" and form.getvalue("c71")=="4" and form.getvalue("c72")=="6" and form.getvalue("c74")=="5" and form.getvalue("c75")=="2" and form.getvalue("c77")=="1" and form.getvalue("c80")=="9" : print '<h1 style="color:green;">Well done !</h1><br />'
elif form.getvalue("c0" and "c3" and "c5" and "c6" and "c8" and "c9" and "c10" and "c13" and "c14" and "c16" and "c18" and "c20" and "c21" and "c23" and "c24" and "c27" and "c31" and "c32" and "c35" and "c37" and "c38" and "c39" and "c40" and "c41" and "c42" and "c43" and "c45" and "c48" and "c49" and "c53" and "c56" and "c57" and "c59" and "c60" and "c62" and "c64" and "c66" and "c67" and "c70" and "c71" and "c72" and "c74" and "c75" and "c77" and "c80") : print '<h1 style="color:red;">Please try again..</h1><br />'
else : print 'Please fill in the blank..<br />'

print '<form method="post" action="sudoku.py">'
print '<table id="grid">'

print '<tr>'
print '<td><input id="cell-0" name="c0"  type="text"></td>'
print '<td><input id="cell-1" name="c1" type="text" value="2" disabled></td>'
print '<td><input id="cell-2" name="c2" type="text" value="1" disabled></td>'

print '<td><input id="cell-3" name="c3" type="text"></td>'
print '<td><input id="cell-4" name="c4" type="text" value="3" disabled></td>'
print '<td><input id="cell-5" name="c5" type="text"></td>'

print '<td><input id="cell-6" name="c6" type="text"></td>'
print '<td><input id="cell-7" name="c7" type="text" value="5" disabled></td>'
print '<td><input id="cell-8" name="c8" type="text"></td>'
print '</tr>'

print '<tr>'
print '<td><input id="cell-9" name="c9" type="text"></td>'
print '<td><input id="cell-10" name="c10" type="text"></td>'
print '<td><input id="cell-11" name="c11" type="text" value="6" disabled></td>'
          
print '<td><input id="cell-12" name="c12" type="text" value="7" disabled></td>'
print '<td><input id="cell-13" name="c13" type="text"></td>'
print '<td><input id="cell-14" name="c14" type="text"></td>'
          
print '<td><input id="cell-15" name="c15" type="text" value="9" disabled></td>'
print '<td><input id="cell-16" name="c16" type="text"></td>'
print '<td><input id="cell-17" name="c17" type="text" value="1" disabled></td>'
print '</tr>'

print '<tr>'          
print '<td><input id="cell-18" name="c18" type="text"></td>'
print '<td><input id="cell-19" name="c19" type="text" value="8" disabled></td>'
print '<td><input id="cell-20" name="c20" type="text"></td>'
          
print '<td><input id="cell-21" name="c21" type="text"></td>'
print '<td><input id="cell-22" name="c22" type="text" value="1" disabled></td>'
print '<td><input id="cell-23" name="c23" type="text"></td>'
          
print '<td><input id="cell-24" name="c24" type="text"></td>'
print '<td><input id="cell-25" name="c25" type="text" value="3" disabled></td>'
print '<td><input id="cell-26" name="c26" type="text" value="2" disabled></td>'
print '</tr>'

print '<tr>'       
print '<td><input id="cell-27" name="c27" type="text"></td>'
print '<td><input id="cell-28" name="c28" type="text" value="7" disabled></td>'
print '<td><input id="cell-29" name="c29" type="text" value="4" disabled></td>'
          
print '<td><input id="cell-30" name="c30" type="text" value="9" disabled></td>'
print '<td><input id="cell-31" name="c31" type="text"></td>'
print '<td><input id="cell-32" name="c32" type="text"></td>'
          
print '<td><input id="cell-33" name="c33" type="text" value="1" disabled></td>'
print '<td><input id="cell-34" name="c34" type="text" value="2" disabled></td>'
print '<td><input id="cell-35" name="c35" type="text"></td>'
print '</tr>'

print '<tr>'          
print '<td><input id="cell-36" name="c36" type="text" value="1" disabled></td>'
print '<td><input id="cell-37" name="c37" type="text"></td>'
print '<td><input id="cell-38" name="c38" type="text"></td>'
          
print '<td><input id="cell-39" name="c39" type="text"></td>'
print '<td><input id="cell-40" name="c40" type="text"></td>'
print '<td><input id="cell-41" name="c41" type="text"></td>'
          
print '<td><input id="cell-42" name="c42" type="text"></td>'
print '<td><input id="cell-43" name="c43" type="text"></td>'
print '<td><input id="cell-44" name="c44" type="text" value="5" disabled></td>'
print '</tr>'

print '<tr>'          
print '<td><input id="cell-45" name="c45" type="text"></td>'
print '<td><input id="cell-46" name="c46" type="text" value="5" disabled></td>'
print '<td><input id="cell-47" name="c47" type="text" value="3" disabled></td>'
          
print '<td><input id="cell-48" name="c48" type="text"></td>'
print '<td><input id="cell-49" name="c49" type="text"></td>'
print '<td><input id="cell-50" name="c50" type="text" value="8" disabled></td>'
          
print '<td><input id="cell-51" name="c51" type="text" value="4" disabled></td>'
print '<td><input id="cell-52" name="c52" type="text" value="7" disabled></td>'
print '<td><input id="cell-53" name="c53" type="text"></td>'
print '</tr>'

print '<tr>'          
print '<td><input id="cell-54" name="c54" type="text" value="2" disabled></td>'
print '<td><input id="cell-55" name="c55" type="text" value="1" disabled></td>'
print '<td><input id="cell-56" name="c56" type="text"></td>'
          
print '<td><input id="cell-57" name="c57" type="text"></td>'
print '<td><input id="cell-58" name="c58" type="text" value="9" disabled></td>'
print '<td><input id="cell-59" name="c59" type="text"></td>'
          
print '<td><input id="cell-60" name="c60" type="text"></td>'
print '<td><input id="cell-61" name="c61" type="text" value="6" disabled></td>'
print '<td><input id="cell-62" name="c62" type="text"></td>'
print '</tr>'

print '<tr>'          
print '<td><input id="cell-63" name="c63" type="text" value="3" disabled></td>'
print '<td><input id="cell-64" name="c64" type="text"></td>'
print '<td><input id="cell-65" name="c65" type="text" value="7" disabled></td>'
          
print '<td><input id="cell-66" name="c66" type="text"></td>'
print '<td><input id="cell-67" name="c67" type="text"></td>'
print '<td><input id="cell-68" name="c68" type="text" value="6" disabled></td>'
          
print '<td><input id="cell-69" name="c69" type="text" value="2" disabled></td>'
print '<td><input id="cell-70" name="c70" type="text"></td>'
print '<td><input id="cell-71" name="c71" type="text"></td>'
print '</tr>'

print '<tr>'          
print '<td><input id="cell-72" name="c72" type="text"></td>'
print '<td><input id="cell-73" name="c73" type="text" value="4" disabled></td>'
print '<td><input id="cell-74" name="c74" type="text"></td>'
          
print '<td><input id="cell-75" name="c75" type="text"></td>'
print '<td><input id="cell-76" name="c76" type="text" value="7" disabled></td>'
print '<td><input id="cell-77" name="c77" type="text"></td>'
          
print '<td><input id="cell-78" name="c78" type="text" value="3" disabled></td>'
print '<td><input id="cell-79" name="c79" type="text" value="8" disabled></td>'
print '<td><input id="cell-80" name="c80" type="text"></td>'
print '</tr>'

print '</table>'

print '<br /><input style="width: 200px" type="submit" value="Submit" />'

print '</div>'

print '</body>'
print '</html>'
