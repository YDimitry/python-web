
def application(env, start_response):
    data = '\n'.join(env['QUERY_STRING'].split('&')).encode('utf-8')
    start_response('200 OK', [('Content-Type', 'text/html'),
    ("Content-Length", str(len(data)))])


    return [data]
