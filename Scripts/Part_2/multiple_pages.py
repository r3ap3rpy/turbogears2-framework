from tg import expose, TGController, AppConfig
from wsgiref.simple_server import make_server

#http://localhost:8080/

class MultiPages(TGController):
	@expose()
	def index(self):
		return 'Welcome to the multi page webapp!'

	@expose()
	def add(self, a, b):
		a = int(a)
		b = int(b)
		return f"{a} + {b} = {a+b}"

	@expose()
	def multiply(self, a, b):
		a = int(a)
		b = int(b)
		return f"{a} * {b} = {a*b}"

if __name__ == '__main__':
	config = AppConfig(minimal = True, root_controller = MultiPages())
	application = config.make_wsgi_app()
	httpd = make_server('',8080, application)
	httpd.serve_forever()
