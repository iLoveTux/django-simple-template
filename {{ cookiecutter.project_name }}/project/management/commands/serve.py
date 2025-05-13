import os
import sys
import argparse
import cherrypy
from django.core.wsgi import get_wsgi_application
from django.core.management.base import BaseCommand

class DjangoCherryPyServer(object):
    def __init__(self, wsgi_app, host, port, server_config):
        self.wsgi_app = wsgi_app
        self.host = host
        self.port = port
        self.server_config = server_config

    def run(self):
        cherrypy.config.update({
            'server.socket_host': self.host,
            'server.socket_port': self.port,
            **self.server_config
        })
        cherrypy.tree.graft(self.wsgi_app, '/')
        cherrypy.engine.start()
        cherrypy.engine.block()

class Command(BaseCommand):
    help = 'Serve Django using CherryPy web server.'

    def add_arguments(self, parser):
        import os
        parser.add_argument('--host', default=os.environ.get('CHERRYPY_HOST', '127.0.0.1'), help='Host to bind CherryPy server (default: 127.0.0.1 or $CHERRYPY_HOST)')
        parser.add_argument('--port', type=int, default=int(os.environ.get('CHERRYPY_PORT', 8000)), help='Port to bind CherryPy server (default: 8000 or $CHERRYPY_PORT)')
        parser.add_argument('--threads', type=int, default=int(os.environ.get('CHERRYPY_THREADS', 10)), help='Number of CherryPy threads (default: 10 or $CHERRYPY_THREADS)')
        parser.add_argument('--ssl', action='store_true', default=os.environ.get('CHERRYPY_SSL', 'False').lower() in ('1','true','yes'), help='Enable SSL (requires cert and key, or $CHERRYPY_SSL)')
        parser.add_argument('--ssl-cert', default=os.environ.get('CHERRYPY_SSL_CERT', None), help='Path to SSL certificate file (or $CHERRYPY_SSL_CERT)')
        parser.add_argument('--ssl-key', default=os.environ.get('CHERRYPY_SSL_KEY', None), help='Path to SSL private key file (or $CHERRYPY_SSL_KEY)')
        parser.add_argument('--autoreload', action='store_true', default=os.environ.get('CHERRYPY_AUTORELOAD', 'False').lower() in ('1','true','yes'), help='Enable CherryPy autoreload (or $CHERRYPY_AUTORELOAD)')
        parser.add_argument('--max-requests', type=int, default=int(os.environ.get('CHERRYPY_MAX_REQUESTS', 0)), help='Max requests per thread (0 = unlimited, or $CHERRYPY_MAX_REQUESTS)')
        parser.add_argument('--timeout', type=int, default=int(os.environ.get('CHERRYPY_TIMEOUT', 60)), help='Socket timeout in seconds (default: 60 or $CHERRYPY_TIMEOUT)')

    def handle(self, *args, **options):
        import cherrypy
        from django.core.wsgi import get_wsgi_application

        class DjangoCherryPyServer(object):
            def __init__(self, wsgi_app, host, port, server_config):
                self.wsgi_app = wsgi_app
                self.host = host
                self.port = port
                self.server_config = server_config

            def run(self):
                cherrypy.config.update({
                    'server.socket_host': self.host,
                    'server.socket_port': self.port,
                    **self.server_config
                })
                cherrypy.tree.graft(self.wsgi_app, '/')
                cherrypy.engine.start()
                cherrypy.engine.block()

        server_config = {
            'server.thread_pool': options['threads'],
            'server.max_request_body_size': 0,  # unlimited
            'server.socket_timeout': options['timeout'],
            'engine.autoreload.on': options['autoreload'],
        }
        if options['max_requests'] > 0:
            server_config['server.max_requests'] = options['max_requests']
        if options['ssl']:
            if not options['ssl_cert'] or not options['ssl_key']:
                self.stderr.write(self.style.ERROR('--ssl-cert and --ssl-key are required for SSL.'))
                sys.exit(1)
            server_config['server.ssl_module'] = 'builtin'
            server_config['server.ssl_certificate'] = options['ssl_cert']
            server_config['server.ssl_private_key'] = options['ssl_key']

        application = get_wsgi_application()
        server = DjangoCherryPyServer(application, options['host'], options['port'], server_config)
        self.stdout.write(self.style.SUCCESS(f"Starting CherryPy server at http{'s' if options['ssl'] else ''}://{options['host']}:{options['port']}/"))
        server.run()
