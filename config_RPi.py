import socket
#this file is the only file that is different on each reader device (mobile or fixed reader)
print(socket.gethostname())
print "config ok"

settings = {
"readerType": "mobile",
"readerID": socket.gethostname()
}
# types of readerID:
# Ingang1 Ingang2
# Premium1 Premium2 Premium3
# Kassa kassa2
# Bar1 (Bar2 ==> Kassa2)
# Stempaal1 Stempaal2 Stempaal3
# Playfield
# Gili ==> WCuit
# WC
# Lichtpaal
# Uitgang
