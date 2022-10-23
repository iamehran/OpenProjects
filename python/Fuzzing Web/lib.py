import random
from random import randrange,choice

class fuzzer():
    '''Public fuzzer mutation library'''
    def RetNothing(self, packet):
        string = ""
        return  string

    def intelli(self, packet):
        byte1 = choice(["\xff","\x80","\x41","\x00"])
        lon = randrange(1,25)
        payload = str(byte1)*lon
        final = str(byte1)+str(payload)

        return final

    def onerand(self, packet):
        byte = chr(randrange(256))
        return byte

    def doublerand(self, packet):
        byte = chr(randrange(256))
        byte2 = chr(randrange(256))
        final = str(byte)+str(byte2)
        return final

    def triplerand(self, packet):
        byte = chr(randrange(256))
        byte2 = chr(randrange(256))
        byte3 = chr(randrange(256))
        final = str(byte)+str(byte2)+str(byte3)
        return final

    def quadrand(self, packet):
        byte = chr(randrange(256))
        byte2 = chr(randrange(256))
        byte3 = chr(randrange(256))
        byte4 = chr(randrange(256))
        final = str(byte)+str(byte2)+str(byte3)+str(byte4)
        return final

    def longerrand(self, packet):
        byte = chr(randrange(128))
        lon = randrange(0,536) #modif target different len check
        final = str(byte)*lon
        return final

    def longernego(self, packet):
        byte = "\x02"+"A"+"\x00"
        lon = randrange(0,5536)
        final = str(byte)*lon
        return final


    def longerrand16le(self, packet):
        byte = chr(randrange(128))
        lon = randrange(0,300)
        final = str(byte*lon).encode('utf-16le')
        return final

    def longerrand16leMSFT(self, packet):
        byte = chr(randrange(128))
        lon = randrange(0,30)
        final = str(byte*lon).encode('utf-16le')+"\x00\x00"
        return final

    def opnum(self, packet):
        byte = chr(randrange(0,2))
        return byte

    def onenull(self, packet):
        null = "\x00"
        return null

    def oneff(self, packet):
        ff = choice(["\xff", "\xfe", "\x00", "\x01", "\xfd"])
        return ff

    def doubleopnum(self, packet):
        byte = chr(randrange(0,2))
        byte2 = chr(randrange(0,2))
        final = str(byte)+str(byte2)
        return final

    def quadopnum(self, packet):
        byte = chr(randrange(0,2))
        byte2 = chr(randrange(0,2))
        byte3 = chr(randrange(0,2))
        byte4 = chr(randrange(0,2))
        final = str(byte)+str(byte2)+str(byte3)+str(byte4)
        return final

    def octoopnum(self, packet):
        byte = chr(randrange(256))
        byte2 = chr(randrange(256))
        byte3 = chr(randrange(256))
        byte4 = chr(randrange(256))
        byte5 = chr(randrange(256))
        byte6 = chr(randrange(256))
        byte7 = chr(randrange(256))
        byte8 = chr(randrange(256))
        final = str(byte)+str(byte2)+str(byte3)+str(byte4)+str(byte5)+str(byte6)+str(byte7)+str(byte8)
        return final

    def doubleGen(self, packet):
        dblff = choice(["\xff\xff", "\xfe\xff", "\xff\xfe", "\x00\x00", "\x01\x00", "\x00\x01", "\x00\xff", "\xff\x00"])
        return dblff


    def quadGen(self, packet):
        fourff = choice(["\xff\xff\xff\xff", "\xff\xff\xff\xfe", "\x00\x00\x00\x01","\x00\x00\x00\x19", "\x01\x00\x00\x00", "\x00\x00\x00\x00", "\xfe\xff\xff\xff"])
        return fourff

    def octGen(self, packet):
        final = (["\x00\x00\x00\x00\xff\xff\xff\xfe","\x00\x00\x00\x00\xff\xff\xff\xff","\xff\xff\xff\xff\xff\xff\xff\xfe","\xff\xff\xff\xff\xff\xff\xff\xff","\x00\xff\x00\xff\x00\xff\x00\xff","\x00\x00\x00\x00\x00\x00\x00\x00","\x00\x01\x00\x01\x00\x01\x00\x01","\x00\x00\x00\x00\x00\x00\x00\x19"])
        return final

    def formatstr(self, packet):
        byte = "%s%x%n"
        lon = randrange(2,160)
        final = str(byte)*lon
        return final

    def Asn(self, packet):
        byte = choice(["\x00","\x01","\x02","\x30","\x04","\x05","\x0A","\x48","\x45","\x4c","\x4f","\x81","\x82","\x83","\x84"])
        return byte


    ### Sets char functions untuk in stringop()
    FunctionStrings = [longerrand, intelli, RetNothing]

    def stringop(self, packet):
        return choice(self.FunctionStrings)(self, packet)

    # ada stringop untuk memiliki cakupan lengkap dengan menggeser konten semua bidang mengikuti bidang yang di fuzzing.
    FunctionSingle = [oneff, onenull, onerand, opnum, stringop, RetNothing]

    def onechar(self, packet):
        return choice(self.FunctionSingle)(self, packet)

    FunctionDouble = [doubleopnum, doublerand, doubleGen, stringop, RetNothing]

    def doublechar(self, packet):
        return choice(self.FunctionDouble)(self, packet)


    FunctionQuad = [quadopnum, quadrand, quadGen, stringop, RetNothing]

    def quadchar(self, packet):
        return choice(self.FunctionQuad)(self, packet)

    FunctionOcto = [octoopnum, octGen, stringop, RetNothing]

    def octochar(self, packet):
        return choice(self.FunctionOcto)(self, packet)
    
    function = [onechar,doublechar,quadchar,octochar,stringop, RetNothing]

    def randfunc(self, packet):
        return choice(self.function)(self, packet)

    def DispatchPackets(self,packet):
	if len(packet) == 1:
           return self.onechar(packet)
	if len(packet) == 2:
	   return self.doublechar(packet)
	if len(packet) == 4:
	   return self.quadchar(packet)
	if len(packet) == 8:
	   return self.octochar(packet)
	else:
	   return self.stringop(packet) # kalau len (paket) adalah 0 atau selain yang disebutkan, lalu dikirim ke stringop.

