class Mahasiswa:

	def __init__(self, nama, nilai):
		self.nama = nama
		self.__nilai = nilai

	@property
	def detail(self):
		return "Nama: {} \nNilai: {}".format(self.nama, self.__nilai)

	@property
	def nilai(self):
		pass

	@nilai.getter
	def nilai(self):
		return self.__nilai

	@nilai.setter
	def nilai(self, input):
		self.__nilai = input

	@nilai.deleter
	def nilai(self):
		self.__nilai = None

    
def main():
    mahasiswa = Mahasiswa(None, None)
    F = False
    while(not F):
        print('===== Program OOP =====')
        print('1. Mendeklarasikan Objek',
      '\n2. Menampilkan Objek',
      '\n3. Merubah Nilai Objek',
      '\n4. Menghapus Objek',
      '\n5. Keluar Dari Program\n')
        pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): "))
        if(pilihan == 1):
            nama = input("Masukkan Namamu: ")
            nilai = int(input("Masukkan Nilaimu: "))
            mahasiswa = Mahasiswa(nama, nilai)
            print("Data Berhasil Ditambahkan")
            print("\n")
        elif(pilihan == 2):
            print("\n")
            print(mahasiswa.detail)
            print("\n")
        elif(pilihan == 3):
            op = input("Apa yang ingin diubah (Nama/Nilai): ")
            if(op == "Nama" or op == "nama"):
                nama = input("Masukkan Nama: ")
                mahasiswa.nama = nama
                print("Data Nama Berhasil Dirubah")
                print("\n")
            elif(op == "Nilai" or op == "nilai"):
                nilai = int(input("Masukkan Nilai: "))
                mahasiswa.nilai = nilai
                print("Data Nilai Berhasil Dirubah")
                print("\n")
            else:
                print("Masukkan Opsi yang sesuai antara Nama/Nilai!")
                print("\n")
        elif(pilihan == 4):
            mahasiswa.nama = None
            del mahasiswa.nilai
            print("Data Berhasil Dihapus")
            print("\n")
        elif(pilihan == 5):
            print("Terima Kasih Sudah Menggunakan Program Saya")
            F = True
        else:
            print("Invalid Input!")
            print("\n")
            
main()

