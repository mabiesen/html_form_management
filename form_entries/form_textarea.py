class form_textarea:

	def __init__(self, htmlsoup, namesoup):
		self.id = ""
		self.html = str(htmlsoup)
		self.name = str(namesoup)
		self.nickname = ""
		self.type = "Textarea"
        self.current_value = ""
		self.user_value = ""
        self.active = True
