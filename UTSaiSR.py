import os
import time
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:

    print(" ")
    print("****************************************")
    print("Program Belajar Berbicara Bahasa Inggris")
    print("****************************************")
    print(" ")
    print("1. Memulai latihan 'speaking' ")
    print("2. Panduan program ")
    print("3. Keluar program ")
    print(" ")
     
    pil = int(input("masukkan pilihan Anda :"))

    if pil == 1 :
        #letak utama
        print(" Katakan kalimat bahasa Inggris ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Anda mengatakan : {}".format(text))
        except:
            print("Periksa kembali pengucapan/pronunciation Anda")
    elif pil == 2:
        os.system("cls")
        print("Panduan")
        print("1. Cara kerja program adalah dengan menerima masukan berupa suara dari microfon.")
        print("2. Setelah menerima masukan program akan mengenali, apakah masukan tersebut dapat diterima atau tidak.")
        print("3. Beberapa kriteria penilaian :")
        print("     baik, Apabila kalimat yang diucapkan sama dengan output")
        print("     cukup, Apabila kalimat yang diucapkan hampir sama dengan output")
        print("     buruk, Apabila kalimat yang diucapkan tidak dikenali")
        print("4. Pilih menu 1 pada program untuk memulai latihan.")
    elif pil== 3 :
        print("*******************")
        print("Keluar Dari Program")
        print("*******************")
        print(" ")
        print("Program akan tertutup dalam 5 detik")
        time.sleep(1)
        os.system("cls")
    else :
        print("Masukkan Anda salah")
