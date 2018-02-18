class form_select:

	def __init__(self, htmlsoup, namesoup):
		self.id = ""
        self.html = str(htmlsoup)
        self.name = str(namesoup)
        self.nickname = ""
        self.type = "Select"
        self.current_value = ""
        self.user_value = ""
        self.active = True
        self.options = []
