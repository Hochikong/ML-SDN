from SOAPpy import SOAPServer
def minus(m,n):
    return m-n

def multi(m,n):
    return m*n

server = SOAPServer(("0.0.0.0",2010))
server.registerFunction(minus)
server.registerFunction(multi)
server.serve_forever()
