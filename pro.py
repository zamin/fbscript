import os, platform,time
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://www.facebook.com/aahilrana4072")
#os.system("clear")
#print("\t 30 April ko All Approvels Remove Krdea jaingy")
#print("\t Users Ko Again Buy Krna pady ga ")
#print("\t Shukriya.....")
#time.sleep(3)
#os.system("clear")
#print("\n\n")
#print("updating again please wait we have some errors")
#exit()
#os.system("pip install requests-random-user-agent")
try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")

rana=platform.architecture()[0]
try:
    if rana=="32bit":
        __import__("pro32")
    elif rana=="64bit":
        __import__("pro").mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if rana == "32bit":
        import pro32
    elif rana == "64bit":
        import pro
        pro.mysecurity()
    else:
        print(" We have issue to launch script")
        exit()
