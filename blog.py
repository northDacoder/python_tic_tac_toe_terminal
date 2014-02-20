#BLOG POSTS

#AUTHORS
class Author(object):
	def __init__(self, name, age, genre):
		self.name = name 
		self.age = age
		self.genre = genre
		self.blogs = []

	def __repr__(self):
		return "Author: {0}".format(self.name)

#BLOG
class Blog(object):
	def __init__(self, title, date, subject):
		self.title = title
		self.date = date
		self.subject = subject

	def __repr__(self):
		return "Blog Title: {0}".format(self.title)