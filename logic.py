def classify_waste(text):
    text = text.lower()

    if any(word in text for word in ["makanan", "daun", "sisa"]):
        return "Organik", "Dapat dijadikan kompos"
    
    elif any(word in text for word in ["plastik", "botol", "kertas", "kaleng"]):
        return "Anorganik", "Dapat didaur ulang"
    
    elif any(word in text for word in ["baterai", "lampu", "kimia"]):
        return "B3", "Buang ke tempat khusus limbah berbahaya"
    
    else:
        return "Tidak diketahui", "Perlu identifikasi lebih lanjut"