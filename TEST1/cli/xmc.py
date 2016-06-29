from xmlrpclib import ServerProxy
address = raw_input('Enter the address: ')
server = ServerProxy(address)
print('plus')
m = input("Enter a num: ")
n = input("Enter another num: ")
print(server.cal(m,n))
