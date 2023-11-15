class PengetahuanMentalAnak:
    def __init__(self):
        self.fakta_mental = set()
        self.aturan_mental = []

    def tambah_fakta(self, fakta):
        self.fakta_mental.add(fakta)

    def tambah_aturan(self, aturan):
        self.aturan_mental.append(aturan)

    def evaluasi_kondisi_mental(self):
        for aturan in self.aturan_mental:
            premis, konklusi = aturan
            if all(premis in self.fakta_mental for premis in premis):
                print(f"Anak ini terlihat {konklusi}.")

# Inisialisasi pengetahuan tentang kondisi mental anak
pengetahuan_anak = PengetahuanMentalAnak()

# Menambahkan fakta tentang kondisi mental anak
pengetahuan_anak.tambah_fakta('Senang')
pengetahuan_anak.tambah_fakta('Stres')
pengetahuan_anak.tambah_fakta('bosan')

# Menambahkan aturan tentang kondisi mental anak
pengetahuan_anak.tambah_aturan((['Senang'], 'tidak sedih'))
pengetahuan_anak.tambah_aturan((['Stres'], 'tidak senang'))
pengetahuan_anak.tambah_aturan((['Bosan'], 'bisa jadi sedih'))

# Evaluasi kondisi mental anak berdasarkan pengetahuan
pengetahuan_anak.evaluasi_kondisi_mental()
