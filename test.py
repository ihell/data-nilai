mahasiswa = {
    "G.1": ["Ryo", 97],
    "G.3": ["Nijika", 90],
    "G.2": ["Kita", 89]
}

def print_data(mahasiswa, title):
    print(title)
    for k in mahasiswa:
        print("Nama : ", mahasiswa[k][0], "\t",
              "NIM : ", k, "\t", "Nilai : ", mahasiswa[k][1])
    print("==================================")

def sort_data(mahasiswa, sorting_code):
    if sorting_code == "1":
        return {k: v for k, v in sorted(mahasiswa.items())}
    elif sorting_code == "2":
        return {k: v for k, v in sorted(mahasiswa.items(), key=lambda item: item[1][0])}
    elif sorting_code == "3":
        return {k: v for k, v in sorted(mahasiswa.items(), key=lambda item: item[1][1], reverse=True)}
    else:
        print("Kode sorting tidak valid")
        return None

while True:
    print("=======Data Nilai Mahasiswa=======")
    for k in mahasiswa:
        print("Nama : ", mahasiswa[k][0], "\t",
              "NIM : ", k, "\t", "Nilai : ", mahasiswa[k][1])
    print("==================================")
    
    code_sorting = {
        1: "Urutkan Berdasarkan NIM",
        2: "Urutkan Berdasarkan Nama",
        3: "Urutkan Berdasarkan Nilai Tertinggi"
    }
    
    print("=====Pilih Metode Pengurutan Data=====")
    for i in code_sorting:
        print("Code Sorting : ", i, "---", "Metode Sorting : ", code_sorting[i])
    
    sorting = input("Masukan Code Sorting : ")
    sorted_mahasiswa = sort_data(mahasiswa, sorting)
    
    if sorted_mahasiswa:
        if sorting == "1":
            print("=======Data Nilai Mahasiswa Berdasarkan NIM=======")
        elif sorting == "2":
            print("=======Data Nilai Mahasiswa Berdasarkan Nama=======")
        elif sorting == "3":
            print("=======Data Nilai Mahasiswa Berdasarkan Nilai Tertinggi=======")
        
        for n in sorted_mahasiswa:
            print("Nama : ", sorted_mahasiswa[n][0], "\t",
                  "NIM : ", n, "\t", "Nilai : ", sorted_mahasiswa[n][1])
        print("==================================")
    
    pilih_metode_lain = input("Pilih Metode Lain? (YES/NO) : ").upper()
    if pilih_metode_lain == "NO":
        break
    


