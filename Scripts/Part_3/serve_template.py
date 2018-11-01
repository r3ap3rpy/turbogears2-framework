from tg import expose, AppConfig, TGController
from wsgiref.simple_server import make_server

class CalculatorTemplate(TGController):
	@expose()
	def index(self):
		return 'Welcome to the templated demo!'

	@expose('calculator.xhtml')
	def calculator(self, title = 'Calculator', a = 5, b = 10):
		return dict(a = a, b = b, title = title)

if __name__ == '__main__':
	config = AppConfig(minimal = True, root_controller = CalculatorTemplate())
	config.renderers.append('kajiki')
	application = config.make_wsgi_app()
	httpd = make_server('',8080, application)
	httpd.serve_forever()
