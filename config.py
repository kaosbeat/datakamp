import socket
#this file is the only file that is different on each reader device (mobile or fixed reader)
# settings = {
# "readerType": "fixed",
# "readerID": "Lichtpaal"
# }

print(socket.gethostname())
print "config ok"

settings = {
"readerType": "fixed",
"readerID": socket.gethostname()
}
# types of readerID:
# Ingang
# Premium
# Kassa
# Bar
# Stempaal
# Playfield
# Gili ==> WCuit
# WC
# Lichtpaal
# Uitgang
