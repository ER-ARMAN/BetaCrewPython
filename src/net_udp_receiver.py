import socket

RECEIVER_ADDRESS = "0.0.0.0"
RECEIVER_PORT = 3000
BUFFER_SIZE = 4096

print("UDP IPv4 datagram socket receiver")

receivingSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("- socket created")

receiver = (RECEIVER_ADDRESS, RECEIVER_PORT);

receivingSocket.bind(receiver)
print("- socket bound on " + RECEIVER_ADDRESS + ":" + str(RECEIVER_PORT))

stop = False
while (stop == False):
    (buffer, peer) = receivingSocket.recvfrom(BUFFER_SIZE)
    received_length = len(buffer)
    msg = buffer.decode()
    (peer_address, peer_port) = peer
    print("- message " + str(received_length) + "B received from " + peer_address + ":" + str(peer_port) + " on port " + str(RECEIVER_PORT))
    print("|" + msg + "|")

    if msg == "stop":
        stop = True

receivingSocket.close()
print("- socket closed")
