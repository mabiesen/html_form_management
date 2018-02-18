from url_form_manager import *

this_wrapper = url_form_manager("https://www.google.com/")
for x in this_wrapper.forms:
    for y in x.entries:
        print(y.current_value)
