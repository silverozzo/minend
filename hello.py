import json
import tornado.ioloop
import tornado.web

from field import Field


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('view.html')


class StarterHandler(tornado.web.RequestHandler):
	def get(self):
		field = Field(3, 3, 2)
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(field.get_state()))


def make_app():
	return tornado.web.Application([
		(r'/',      MainHandler),
		(r'/start', StarterHandler),
	])

if __name__ == '__main__':
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
