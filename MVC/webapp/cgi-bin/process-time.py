__author__ = 'Dixit_Patel'

import cgi
form = cgi.FieldStorage()
timing_value = form["TimeValue"].value