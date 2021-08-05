from django.shortcuts import render, redirect
from time import localtime, strftime
from django.utils import timezone
from django.utils.crypto import get_random_string #generar string aleatorio
import random, hashlib, os, requests



def root(request):
    return redirect ("/aleatorio")

def index_aleatorio(request):
    ###########################################################################
    def sha256(data):
        digest = hashlib.new("sha256")
        digest.update(data)
        return digest.digest()


    def ripemd160(x):
        d = hashlib.new("ripemd160")
        d.update(x)
        return d.digest()


    def b58(data):
        B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        if data[0] == 0:
            return "1" + b58(data[1:])

        x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
        ret = ""
        while x > 0:
            ret = B58[x % 58] + ret
            x = x // 58

        return ret


    class Point:
        def __init__(self,
            x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
            y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
            p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):
            self.x = x
            self.y = y
            self.p = p

        def __add__(self, other):
            return self.__radd__(other)

        def __mul__(self, other):
            return self.__rmul__(other)

        def __rmul__(self, other):
            n = self
            q = None

            for i in range(256):
                if other & (1 << i):
                    q = q + n
                n = n + n

            return q

        def __radd__(self, other):
            if other is None:
                return self
            x1 = other.x
            y1 = other.y
            x2 = self.x
            y2 = self.y
            p = self.p

            if self == other:
                l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p
            else:
                l = pow(x1 - x2, p-2, p) * (y1 - y2) % p

            newX = (l ** 2 - x2 - x1) % p
            newY = (l * x2 - l * newX - y2) % p

            return Point(newX, newY)

        def toBytes(self):
            x = self.x.to_bytes(32, "big")
            y = self.y.to_bytes(32, "big")
            return b"\x04" + x + y


    def getPublicKey(privkey):
        SPEC256k1 = Point()
        pk = int.from_bytes(privkey, "big")
        hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes()))
        address = b"\x00" + hash160

        address = b58(address + sha256(sha256(address))[:4])
        return address


    def getWif(privkey):
        wif = b"\x80" + privkey
        wif = b58(wif + sha256(sha256(wif))[:4])
        return wif


    randomBytes = os.urandom(32)
    #print("Address: " + getPublicKey(randomBytes))
    #print("Privkey: " + getWif(randomBytes))
    obteneraddress = getPublicKey(randomBytes)
    obtenerprivate = getWif(randomBytes)
    #print(obteneraddress)
    #print(obtenerprivate)
    saldo = requests.get('https://blockchain.info/q/addressbalance/' + obteneraddress)
    ###########################################################################
    #scraper = requests.get('https://btc-explorer.livepay.io/address/'+ obteneraddress)
    #print(scraper.text)
    #cadena = str(scraper.text)
    #subcadena = '<tr><td>Final Balance</td><td class="data">' #la subcadena que queremos localizar

    #posicion = cadena.index(subcadena)
    #print('La posición de la subcadena es', posicion)


    palabra = get_random_string(length=14)
    md5 = hashlib.md5(palabra.encode())
    #print(palabra)
    #print(md5.hexdigest())
    
    
    if 'cuenta' in request.session:
        request.session['cuenta']+=1
        print(request.session['cuenta'])
    else:
        request.session['cuenta']= random.randrange(0, 10, 1)    
    #    print(request.session['cuenta'])
    
    context = {
        "palabra": palabra,
        "hashmd5": md5.hexdigest(),
        "sesion": request.session['cuenta'],
        "address": obteneraddress,
        "privkey": obtenerprivate,
        "saldobitcoin": saldo.text
        
    }

    return render(request,'default_aleatorio.html', context)

    #if request.method == "GET":
    #    return render(request,'default_aleatorio.html', context)
    #if request.method == "POST":
    #    return render(request,'default_aleatorio.html', context)
    #    #return redirect("/aleatorio")


def vaciar(request):
    request.session['cuenta']= 0
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return redirect ("/aleatorio")