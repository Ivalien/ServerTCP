import socket
# Se crea el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se inidica el nombre y puerto del host del servidor
server_address = ('localhost', 10000)
print('Conexion a: {} puerto: {}'.format(*server_address))
sock.connect(server_address)
amount_received = 0
#Se reciben los datos desde el servidor mediante la funcion recv()
data=sock.recv(256)
#Se imprime el valor recibido en formato hexadecimal
print("Valor random entregado por el servidor:")
print(bytes(data).hex())
print('Cerrando conexion')
sock.close()