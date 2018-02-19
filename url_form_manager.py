import bs4
from fetch_html import *
from form import *
from form_entries.form_input import *
#from form_entries.form_textarea import *

class url_form_manager:

# fetches forms and inputs, creates instances, organizes
    def __init__(self, url):
        self.entrytype = ['select', 'input', 'textarea']
        self.url = url
        self.fetcher = fetch_html(url)
        self.html = self.fetcher.html
        self.forms = []
        self.soup = bs4.BeautifulSoup(self.html)

        # generate the forms
        self.generate_forms()

    def generate_forms(self):
        # fetch the forms
        html_forms = self.soup.findAll('form')

        # create forms with inputs
        for x in html_forms:

            try:
                form_name = x['name']
            except:
                form_name = ""

            thisform = form(x, self.url, form_name)

            # create inputs
            these_inputs = x.findAll('input')
            for g in these_inputs:
                thisform.entries.append(self.generate_input(g))

            # create select


            # create textarea

            # append form to list
            self.forms.append(thisform)

    # identify inputs by type, return appropriate
    def generate_input(self,inputsoup):

        try:
            input_type = inputsoup['type']
        except:
            input_type = "text"

        try:
            input_value = inputsoup['value']
        except:
            input_value = ""

        try:
            input_name = inputsoup['name']
        except:
            input_name = ""

        # set some variables needed for db, but not yet supplied
        dbid = ""
        nickname = ""
        uservalue = input_value
        active = True

        # create generic input: right now applies to all inputs
        return form_input_general(\
        dbid,\
        inputsoup,\
        input_name,\
        nickname,\
        input_type,\
        input_value,\
        uservalue,\
        active)

    def generate_select():
        pass

    def generate_textarea():
        pass
