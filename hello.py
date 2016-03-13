import json
import tornado.ioloop
import tornado.web

from field import Field


field = None
bonus = 0


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('view.html')


class StarterHandler(tornado.web.RequestHandler):
	def get(self):
		global field
		global bonus
		
		field = Field(10, 10, 9 + bonus)
		print('---------new')
		
		result = {
			'state' : field.get_state(),
			'rest'  : field.rest
		}
		
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(result))


class OpeningHandler(tornado.web.RequestHandler):
	def get(self, row, col):
		global field
		global bonus
		
		can_bonus = False
		if not field.finished:
			can_bonus = True
		
		result = {
			'state'    : True,
			'stack'    : field.open(int(row), int(col)),
			'finished' : field.finished,
			'loose'    : field.loosed,
		}
		
		if can_bonus and field.finished and not field.loosed:
			bonus += 1
		
		if can_bonus and field.finished and field.loosed:
			bonus = 0
		
		self.set_header('Content-Type', 'application/json')
		self.write(json.dumps(result))


class MarkingHandler(tornado.web.RequestHandler):
	def get(self, row, col):
		global field
		marked = field.mark(int(row), int(col))
		
		result = {
			'state'  : True,
			'rest'   : field.rest,
			'result' : marked,
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
