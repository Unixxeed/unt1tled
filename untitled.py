import os
import sys
import webbrowser
import time
import PIL #Untuk modul pil jika eror, install Plugin "Pillow" terlebih dahulu.
from PIL import Image
from time import sleep
def function(input_nama,input_pass):
  print("\n")
  print(f"\tNames : " , input_nama)
  print(f"\tPassword : " , input_pass)
os.system("clear") 
input_nama = input("\tName : ")
input_pass = input("\tPasswd : ")
function(input_nama,input_pass)
account_verification = input("\n\tAre the information is Correct?\n\t(yes/no)> ")
if account_verification == "yes":
  os.system("clear")
  def lanjut_skrip():
    print("\n\n")
    print("\t>>>MENU<<<")
    print("\t1.>games")
    print("\t2.>icp")
    print("\t3.>calculator")
    print("\t4.>install ngrok")
    print("\t5.>sosmed\n\n")
    wich_one = input("\tSelec Menu >")
    if wich_one == "1":
      def games(score):
        print("\n")
        print("\tQuestions:if you have >\n\t'true true and not false and not false not true and not false'")
        answ_ = input("\tThe Answer Is> ")
        if answ_ == "true":
          print("\tGood!\n\tScore +10")
          def Questions_2():
            print("\n")
            print("\tQuestions:if you have >\n\t'if you have red flags with sickle and hammer on the middle and yellow\n\tstarts on the top of flags. What a kind of flags is it? ")
            answ_ = input("\tThe Answer Is> ")
            if answ_ == "ussr" and "USSR":
              print("\tgood!\n\tscore: +10 ")
              verify_continue_Q3_nolimit = input("\tDo you want to continue?(y/n) ")
              if verify_continue_Q3_nolimit == "y":
                def Questions_3():
                  print("\t\t\t>>>>coming soon!<<<<")
                  os.system("clear")
                  return lanjut_skrip()
                Questions_3()
              elif verify_continue_Q3_nolimit == "n":
                print("\tStay tune for Question's 3 !")
                sleep(3)
                return lanjut_skrip()
            else:
              print("\tYou Fuckin Bitch!")
              return Questions_2()
          Questions_2()
        else:
          print("\t Try again! ")
          return games("score")
      games("score")
    elif wich_one == "5":
      def sosmed():
        print("\t=============================")
        print("\t\t >youtube: @FlashCodmyt ")
        print("\t\t >github : @FlashId ")
        print("\t=============================\n")
        account_visit = input("\tDo you want to visit?.(y/n)")
        if account_visit == "n":
          os.system("clear")
          return lanjut_skrip()
        elif account_visit == "y":
          os.system("clear")
          def continue__():
            print("\t=============================")
            print("\t\t1.>youtube: @FlashCodmyt ")
            print("\t\t2.>github : @FlashId ")
            print("\t=============================")
            print("\n")
            wich_account_visit = input("\twich one of number> ")
            if wich_account_visit == "1":
              open1 = "termux-open-url https://www.youtube.com/@FlashCodmyt"
              webbrowser.open("https://www.youtube.com/@FlashCodmyt") or os.system(open1)
            elif wich_account_visit == "2":
              open2 = "termux-open-url https://github.com/FlashId"
              webbrowser.open("https://github.com/FlashId") or os.system(open2)
            else:
              os.system("clear")
              return sosmed()
          continue__()
      sosmed()
    elif wich_one == "2":
      def imgcompressor():
        print("\n")
        print("\t>>>>IMAGE-Converter")
        print("\tImage Converter(IC)")
        print("\tExample: /sdcard/Download/name.png ")
        print("\t\tIC. by flash 2023-2024\n\n")
        input_img = input("\tSet the directory of img> ")
        output_img = input("\tOutput Image Dir> ")
        img = Image.open(input_img)
        img.save(output_img)
        print("\nE:Error (tidak diketahui).")
        time.sleep(4)
        return lanjut_skrip()
      imgcompressor()
    elif wich_one == "3":
      def calculator():
        os.system("clear")
        print("\t>>>>>>>>>>CALCULATOR<<<<<<<<<<")
        print("\tCalculating machine in python.")
        print("\t(/):Bagi,(+):Tambah,(-):Kurang,")
        print("\t(%):Modulus.\n")
        print("\t\t\t\tCalculator by flash 2023-2024.\n")
        input_value = int(input("\tMasukan Angka> "))
        input_value_2nd = int(input("\tMasukan Angka> "))
        input_calculating_operation = (input("\tMasukan Jenis Operasi = "))
        operation_tambah = int(input_value) + int(input_value_2nd)
        operation_kurang = int(input_value) - int(input_value_2nd) #ini skrip kalkulator dari bulan lalu 
        operation_bagi = int(input_value) / int(input_value_2nd) #buatan Irsyad 2023-2024
        operation_modulus = int(input_value) % int(input_value_2nd)
        Hasil = "\tThe Result is > "
        if input_calculating_operation == "+" :
          print( str(Hasil) + str(operation_tambah))
        elif input_calculating_operation == "-" :
          print( str(Hasil) + str(operation_kurang))
        elif input_calculating_operation == "/" :
          print( str(Hasil) + str(operation_bagi))
        elif input_calculating_operation == "%" :
          print( str(Hasil) + str(operation_modulus))
        else:
          print("\n\tPlease Enter CORRECTLY!\n")
          return calculator()
      calculator()
    elif wich_one == "4":
      def ngrok_installer():
        os.system("clear")
        print("\tWARNING")
        print("=================================PROCESSING=================================")
        os.system("apt update -y")
        os.system("apt upgrade -y")
        print("============================================================================")
        sleep(3)
        os.system("clear")
        print("Login dulu,baru lanjut")
        sleep(2)
        os.system("clear")
        print("====================================LOGIN===================================")
        a = "Login dengan akun anda"
        print(a)
        sleep(3)
        b2 = "termux-open-url https://dashboard.ngrok.com/signup"
        os.system(b2)
        sleep(5)
        print("Sesudah Login lanjut ke step berikutnya...")
        os.system("clear")
        print("============================================================================")
        sleep(10)
        os.system("clear")
        os.system("figlet OK Bang")
        sleep(3)
        os.system("clear")

        print("=================================DOWNLOADING================================")
        url_untuk_wget = "wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.tgz"
        os.system(url_untuk_wget)
        print("============================================================================")
        sleep(2)
        print("|")
        print("=================================EXTRACTING=================================")
        extract = "tar -xvf ngrok-v3-stable-linux-arm.tgz"
        os.system(extract)
        print("============================================================================")
        sleep(3)
        print("|")
        print("=================================PROCESSING=================================")
        print(" *Exaple: ./ngrok config add-authtoken 2OVZ****************************_****")
        authtoken = input("Insert Ngrok Config = ")
        os.system(authtoken)
        print("============================================================================")
        print("Laman ini akan ditutup dalam 5 detik.....")
        sleep(5)
        os.system("clear")
      ngrok_installer()
  lanjut_skrip()
elif account_verification == "no":
  os.system("python untitled.py")