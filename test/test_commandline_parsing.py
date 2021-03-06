#!/usr/bin/python3
#
#   A. Gnias
#
#   test_commandline_parsing.py - Interactive test to test handling commandline paramater processing
#
#   Linux 4.18.0-18-generic #19-Ubuntu
#   Python 3.7.5
#   Vim 8.0

import sys

sys.path.append("../")
import secret_santa


email, names_fname, exceptions_fname, exchange_date, email_function = secret_santa.process_commandline_parameters()
if isinstance(email, tuple):
    print(f"Email: {email[0], email[1]}")
else:
    print(f"Email: {email}")
print(f"Names csv: {names_fname}")
print(f"Exceptions csv: {exceptions_fname}")
print(f"Exchange date: {exchange_date}")
print(f"Function: {email_function.__name__}")
