mahasiswa = {
    "G.1" : ["Ryo", 97],
    "G,3" : ["Nijika", 90],
    "G,2": ["Kita", 89]
}

print("=======Data Nilai Mahasiswa=======")
for k in mahasiswa:
    print("Nama : ", mahasiswa [k][0],"\t",
          "NIM : ",k,"\t", "Nilai : ", mahasiswa [k][1])