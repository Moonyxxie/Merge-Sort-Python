def merge_sort(arr):
    if len(arr) > 1: # Mengecek apakah array berisi lebih dari satu elemen.
                     # Jika iya, array akan dibagi menjadi bagian yang lebih kecil.
        mid = len(arr) // 2 # Menentukan titik tengah array.
                            # // adalah pembagian bilangan bulat.
        left_half = arr[:mid] # Membagi array menjadi dua bagian, yaitu kiri dan kanan.
        right_half = arr[mid:]

        # Memanggil fungsi merge sort secara berulang untuk mengurutkan kedua bagian sampai setiap bagian hanya memiliki satu elemen.
        merge_sort(left_half)
        merge_sort(right_half)

        # Membuat tiga indeks untuk melacak posisi elemen:
        # i untuk bagian kiri.
        # j untuk bagian kanan.
        # k untuk posisi elemen dalam array utama.
        i = j = k = 0

        while i < len(left_half) and j < len(right_half): # Membandingkan elemen dari bagian kiri dan kanan selama keduanya masih memiliki elemen.
            if left_half[i] < right_half[j]: # Jika elemen kiri lebih kecil, elemen tersebut dimasukkan ke array utama terlebih dahulu.
                                             # Jika tidak, elemen kanan yang dimasukkan.
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half): # Memasukkan sisa elemen dari bagian kiri atau kanan yang belum masuk ke array utama.
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    # Example usage:
my_list = [8, 2, 3, 10, 1, 5, 7, 6, 4, 9] # Membuat daftar angka yang akan diurutkan.
merge_sort(my_list) # Menjalankan algoritma merge sort untuk mengurutkan angka dari terkecil ke terbesar.
print("merge sorted array:",my_list) # Menampilkan hasil pengurutan ke layar.
