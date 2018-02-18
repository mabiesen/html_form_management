import mechanize
#contains a list of inputs(type => class)

class form:

	def __init__(self, htmlsoup, url, namesoup):
		self.id = ""
		self.url = url
		self.html = str(htmlsoup)
		self.name = str(namesoup)
		self.entries = []
		self.nickname = ""
