stack = []

def tambah_buku(stack, nama_buku, nama_pengarang):
    buku_baru = [nama_buku, nama_pengarang]
    stack.append(buku_baru)
    print(f"{buku_baru} berhasil ditambahkan ke dalam stack.")

def hapus_buku_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat dihapus.")
    else:
        buku_terakhir = stack.pop()
        print(f"{buku_terakhir} berhasil dihapus dari stack.")

def tampilan_buku_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat ditampilkan.")
    else:
        buku_teratas = stack[-1]
        print(f"Buku teratas di dalam stack adalah {buku_teratas}.")

while True:
    print("\nGudang saat ini:",stack)
    print("Menu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang Terakhir")
    print("3. Tampilkan Barang Teratas")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan Anda (1/2/3/4):")
    if pilihan == "1":
        nama_buku = input("Masukkan judul buku yang akan ditambahkan:")
        nama_pengarang = input("Masukkan nama pengarang: ")
        tambah_buku(stack, nama_buku, nama_pengarang)
    elif pilihan == "2":
        hapus_buku_terakhir(stack)
    elif pilihan == "3":
        tampilan_buku_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")    
        break
    else:
        print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar")