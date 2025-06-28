def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    if y == 0:
        return "Sıfıra bölünemez!"
    return x / y

def main():
    while True:
        print("\n--- Basit Hesap Makinesi ---")
        print("1. Topla")
        print("2. Çıkar")
        print("3. Çarp")
        print("4. Böl")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın (1-5): ")

        if secim == "5":
            print("Çıkılıyor...")
            break

        sayi1 = float(input("1. sayıyı girin: "))
        sayi2 = float(input("2. sayıyı girin: "))

        if secim == "1":
            print("Sonuç:", topla(sayi1, sayi2))
        elif secim == "2":
            print("Sonuç:", cikar(sayi1, sayi2))
        elif secim == "3":
            print("Sonuç:", carp(sayi1, sayi2))
        elif secim == "4":
            print("Sonuç:", bol(sayi1, sayi2))
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
