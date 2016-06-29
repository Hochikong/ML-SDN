from SimpleXMLRPCServer import SimpleXMLRPCServer
def cal(n,m):
    return n+m
server = SimpleXMLRPCServer(('0.0.0.0',1300))
print 'listen'
server.register_function(cal,'cal')
server.serve_forever()
