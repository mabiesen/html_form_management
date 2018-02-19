#  this input handles typical: number, text, submit
class form_input_general:

	def __init__(self, dbid, htmlsoup, namesoup, nickname, inputtype, valuesoup, uservalue, active):
		self.id = dbid
		self.html = str(htmlsoup)
		self.name = str(namesoup)
		self.nickname = nickname
		self.type = inputtype
		self.current_value = str(valuesoup)
		self.user_value = uservalue
		self.active = active


# class form_input_radio:
#
# 	def __init__(self, htmlsoup, namesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = ""
# 		self.type = "Radio"
# 		self.current_value = False
# 		self.user_value = False
# 		self.active = True
#
# class form_input_checkbox:
#
# 	def __init__(self, htmlsoup, namesoup, valuesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = ""
# 		self.type = "Checkbox"
# 		self.current_value = str(valuesoup)
# 		self.user_value = self.current_value
# 		self.active = True

# class form_input_text:
#
# 	def __init__(self, htmlsoup, namesoup, valuesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = ""
# 		self.type = "Text"
# 		self.current_value = str(valuesoup)
# 		self.user_value = self.current_value
# 		self.active = True
#
# class form_input_number:
#
# 	def __init__(self, htmlsoup, namesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = ""
# 		self.type = "Number"
# 		self.current_value = ""
# 		self.user_value = self.current_value
# 		self.active = True
#
# class form_input_submit:
#
# 	def __init__(self, htmlsoup, namesoup, valuesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = ""
# 		self.type = "Submit"
# 		self.current_value = str(valuesoup)
# 		self.user_value = self.current_value
# 		self.active = False
#
# class form_input_hidden:
#
# 	def __init__(self, htmlsoup, namesoup, valuesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = "Hidden"
# 		self.type = "Hidden"
# 		self.current_value = str(valuesoup)
# 		self.user_value = self.current_value
# 		self.active = True
#
# class form_input_email:
#
# 	def __init__(self, htmlsoup, namesoup, valuesoup):
# 		self.id = ""
# 		self.html = str(htmlsoup)
# 		self.name = str(namesoup)
# 		self.nickname = ""
# 		self.type = "Email"
# 		self.current_value = str(valuesoup)
# 		self.user_value = self.current_value
# 		self.active = True
