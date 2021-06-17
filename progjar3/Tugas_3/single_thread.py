from library import download_gambar, get_url_list, send_file
import time
import datetime

IP_SERVER = "192.168.122.244"
PORT = 5050

def kirim_semua():
    urls = get_url_list()
    catat = datetime.datetime.now()
    for k in urls:
        download_gambar(urls[k], k)
        print(f"mendownload {urls[k]}")
        waktu_proses = download_gambar(urls[k])
        print(f"completed {waktu_proses} detik")

        send_file(IP_SERVER, PORT, f"{k}.jpg")
        print('masuk server 1')
    selesai = datetime.datetime.now() - catat
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik")


#fungsi download_gambar akan dijalankan secara berurutan

if __name__=='__main__':
    kirim_semua()