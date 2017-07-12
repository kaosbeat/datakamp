import socket
#this file is the only file that is different on each reader device (mobile or fixed reader)
print(socket.gethostname())
print "config ok"

settings = {
"readerType": "mobile",
"readerID": socket.gethostname()
}
# types of readerID:
# Ingang
# Premium
# Kassa
# Bar
# Stempaal
# Playfield
# Gili
# WC
# Lichtpaal
# Uitgang
