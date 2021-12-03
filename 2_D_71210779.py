day=input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
matkul1=["1 Algoritma Graf","3 Sistem Operasi","4 PAK"]
matkul2=["2 Matematika Teknik","4 Bhs Indonesia","6 PKN"]
matkul3=["2 Sistem Basis Data","4 Praktikum Sistem Basis Data"]
matkul4=["1 IMK","3 LogMat","4 Prakekkom"]
if "senin" in day:
    for jadwal in matkul1:
        print("kelas ke-{}".format(jadwal))
elif "selasa" in day:
    for jadwal in matkul2:
        print("kelas ke-{}".format(jadwal))
elif "rabu" in day:
    for jadwal in matkul3:
        print("kelas ke-{}".format(jadwal))
elif "kamis" in day:
    for jadwal in matkul4:
        print("kelas ke-{}".format(jadwal))
elif "jumat" in day:
    print("Hari Jumat Anda tidak ada kelas")