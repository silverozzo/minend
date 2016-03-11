import json
import tornado.ioloop
import tornado.web

from field import Field


field = None

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('view.html')


class StarterHandler(tornado.web.RequestHandler):
	def get(self):
		global field
		field = Field(3, 3, 2)
		print('---------new')
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(field.get_state()))


class OpeningHandler(tornado.web.RequestHandler):
	def get(self, row, col):
		global field
		result = {
			'state' : True,
			'stack' : field.open(int(row), int(col)),
		}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(result))


class MarkingHandler(tornado.web.RequestHandler):
	def get(self, row, col):
		global field
		result = {
			'state'  : True,
			'result' : field.mark(int(row), int(col)),
		}
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(result))


def make_app():
	return tornado.web.Application([
		(r'/',               MainHandler),
		(r'/start',          StarterHandler),
		(r'/open/(.*)/(.*)', OpeningHandler),
		(r'/mark/(.*)/(.*)', MarkingHandler),
	])

if __name__ == '__main__':
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
