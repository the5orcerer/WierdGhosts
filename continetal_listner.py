import socket

def scraper(data_bits):
    valuableDbit = list()
    data = data_bits.keys()
    if len(data) != 0:
        for x in data:
            valuableDbit.append(f'{x} : {data_bits[x]}')
    else:
        valuableDbit.append("No data founded")
    return valuableDbit

def main(data, file='data_monster.dbit'):
    with open(file, 'a') as rwaOps:
        rwaOps.write('-'*20+'\n')
        for x in data:
            rwaOps.write(x+'\n')
        rwaOps.write('-'*20)
        rwaOps.close()
def server_handler():
    server_socket = socket.socket()
    server_socket.bind(('', 8787))
    server_socket.listen(3)
    try:
        while True:
            conn, address = server_socket.accept()
            print("Connection from: " + str(address))
            data = conn.recv(1024).decode()
            data_xbit = scraper(eval(data))
            main(data_xbit)
        conn.close()
    except:
        print('IGNORED')
server_handler()
