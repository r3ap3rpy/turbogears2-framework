from wsgiref.simple_server import make_server
from tg import expose, AppConfig, TGController

class PokeMaster(TGController):
	@expose()
	def index(self):
		return "The pokemaster is ready!"

	@expose()
	def _default(self):
		return "Gotta catch them all!"

if __name__ == '__main__':
	config = AppConfig(minimal = True, root_controller = PokeMaster())
	application = config.make_wsgi_app()
	httpd = make_server('',8080, application)
	httpd.serve_forever()