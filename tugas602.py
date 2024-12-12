import math

def main():
    # Menerima input angka dari pengguna
    angka = float(input("Masukkan sebuah angka: "))

    # Menghitung akar kuadrat dari angka
    if angka < 0:
        print("Akar kuadrat tidak dapat dihitung untuk angka negatif.")
    else:
        akar_kuadrat = math.sqrt(angka)
        print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat}")

    # Menghitung logaritma (logaritma natural / ln)
    if angka <= 0:
        print("Logaritma tidak dapat dihitung untuk angka kurang dari atau sama dengan 0.")
    else:
        logaritma = math.log(angka)
        print(f"Logaritma natural (ln) dari {angka} adalah {logaritma}")

if __name__ == "__main__":
    main()

