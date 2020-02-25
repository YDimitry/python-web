
def application(env, start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])

    return ['\n'.join(env['QUERY_STRING'].split('&')).encode('utf-8')]
