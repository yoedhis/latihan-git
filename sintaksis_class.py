class segitiga():
    def hitung_luas_segitiga(self, alas, tinggi):
        return(alas*tinggi)/2

segitiga = segitiga()
print(segitiga.hitung_luas_segitiga(2, 5))

class segitiga():
    def hitung_luas(self, alas, tinggi):
        return(alas*tinggi)/2

segitiga = segitiga ()
print(segitiga.hitung_luas(2, 5))

class segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        return (self.alas*tinggi)/2

    def get_info(self):
        print('informasi alas = ', self.alas, 'tinggi = ', self.tinggi)
segitiga = segitiga(2, 5)
segitiga.get_info()
print(segitiga.hitung_luas())
