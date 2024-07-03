mahasiswa = {
    "G.1" : ["Ryo", 97],
    "G.3" : ["Nijika", 90],
    "G.2": ["Kita", 89]
}

print("=======Data Nilai Mahasiswa=======")
for k in mahasiswa:
    print("Nama : ", mahasiswa[k][0],"\t",
          "NIM : ", k, "\t", "Nilai : ", mahasiswa[k][1])
print("==================================")
code_sorting = {
    1 : "Urutkan Berdasarkan NIM",
    2 : "Urutkan Berdasarkan Nama",
    3 : "Urutkan Berdasarkan Nilai Tertinggi"
}
print("=====Pilih Metode Pengurutan Data=====")
for i in code_sorting:
    print("Code Sorting : ", i, "---", "Metode Sorting : ", code_sorting[i])

sorting = input("Masukan Code Sorting : ")
if sorting == "1":
    sorted_mahasiswa = {k:v for k, v in sorted(mahasiswa.items())}
    print("=======Data Nilai Mahasiswa Berdasarkan NIM=======")
    for n in sorted_mahasiswa:
        print("Nama : ", sorted_mahasiswa[n][0],"\t",
              "NIM : ", n, "\t", "Nilai : ", sorted_mahasiswa[n][1])
elif sorting == "2":
    sorted_mahasiswa = {k:v for k, v in sorted(mahasiswa.items(), key=lambda item: item[1][0])}
    print("=======Data Nilai Mahasiswa Berdasarkan Nama=======")
    for n in sorted_mahasiswa:
        print("Nama : ", sorted_mahasiswa[n][0],"\t",
              "NIM : ", n, "\t", "Nilai : ", sorted_mahasiswa[n][1])
elif sorting == "3":
    sorted_mahasiswa = {k:v for k, v in sorted(mahasiswa.items(), key=lambda item: item[1][1], reverse=True)}
    print("=======Data Nilai Mahasiswa Berdasarkan Nilai Tertinggi=======")
    for n in sorted_mahasiswa:
        print("Nama : ", sorted_mahasiswa[n][0],"\t",
              "NIM : ", n, "\t", "Nilai : ", sorted_mahasiswa[n][1])  
else:
    print("Kode sorting tidak valid")
