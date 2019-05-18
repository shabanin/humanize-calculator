# humanize-calculator
converts strings like "5+5 = 10" to "five plus five equals ten"

usage:
~~~~
>>> from humanize_calculator import humanize
>>> humanize("1*3=1000001")
'one multiply by three equals one million one'
~~~~
run tests:
~~~~
pytest test_int_to_text.py
pytest test_humanize.py
~~~~
