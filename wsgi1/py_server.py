#Web Server Gateway Interface

from wsgiref.simple_server import make_server
from pyweb import application


httpd = make_server('', 8081, application)
print('Serving HTTP on port 8081...')
httpd.serve_forever()


