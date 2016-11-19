def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'you_can_change_here_by_input_your_content.')
    print('environ = ',environ)
    return [body.encode('utf-8')]


