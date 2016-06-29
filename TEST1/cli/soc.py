import SOAPpy
address = raw_input('Enter the address: ')
server = SOAPpy.SOAPProxy(address)
print('multi')
m = input("Enter a num: ")
n = input("Enter another num: ")
print(server.multi(m,n))
