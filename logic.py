import csv

def load_waste_data():
    waste_dict = {}
    try:
        with open('data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row and 'nama_sampah' in row:
                    waste_dict[row['nama_sampah'].lower()] = {
                        'kategori': row['kategori'],
                        'penanganan': row['penanganan']
                    }
    except FileNotFoundError:
        print("File data.csv tidak ditemukan!")
    return waste_dict

def classify_waste(text):
    text = text.lower()
    waste_data = load_waste_data()
    
    # Cari kecocokan dengan data dari CSV
    for waste_name, info in waste_data.items():
        if waste_name in text:
            return info['kategori'].capitalize(), info['penanganan']
    
    return "Tidak diketahui", "Perlu identifikasi lebih lanjut"