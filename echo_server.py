import os
import socket
import nacl.bindings
from nacl import encoding

# Se crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se une el socket creado a puerto local 10000
server_address = ('localhost', 10000)
sock.bind(server_address)
# El servidor se mantiene a la escucha de una solicutd de conexion
sock.listen(1)

while True:
    #Esoerando la conexion mientras que no cambie el calor a 0
    print('Esperando Conexion entrante')
    connection, client_address = sock.accept()
    try:
        print('Conexion desde: ', client_address)
        # Generacion de la semilla con numeros random de acuerdo a los datos del sistema operativo
        def random(size: int = 32) -> bytes:
            return os.urandom(size)
        # De acuerdo al tmaño requerido de bytes de los numeros y la semilla del sistema operativo
        # La funcion randombytes_deterministic regresa un valor en raw de bytes
        def randombytes_deterministic(
                size: int, seed: bytes, encoder: encoding.Encoder = encoding.RawEncoder) -> bytes:
            """
            Returns ``size`` number of deterministically generated pseudorandom bytes
            from a seed

            :param size: int
            :param seed: bytes
            :param encoder: The encoder class used to encode the produced bytes
            :rtype: bytes
            """
            raw_data = nacl.bindings.randombytes_buf_deterministic(size, seed)
            return encoder.encode(raw_data)
        #El valor random generado por el servidor, se manda hacia el cliente que hizo conexion
        salt = randombytes_deterministic(256, bytes(random(32)))
        connection.sendall(salt)
#Se cierra la conexion cuando termina de recibir informacion
    finally:
        # Clean up the connection
        connection.close()