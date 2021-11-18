
from tkinter import*
from random import randint
pencere =Tk()
pencere.geometry("300x300+200+200")
pencere.title("Sayısal Loto")
pencere.configure(bg="grey")

giris = Label(pencere,text="Günün Şanslıları",fg="red", bg="white")
giris.pack()
giris.config(font=("Arial", 20))
giris.grid()

def sayisal():
    i = 0
    secilenler = [0,0,0,0,0,0]
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i+=1
        siralanan = (sorted(secilenler))
        i=0

        buton = Label(pencere,text=siralanan)
        buton.config(font=("Arial",12 ))
        buton.grid(column=10, row=10)
        buton.grid()

numaralar= Button (pencere, text="Yeni Rakam Listele" ,fg="black", bg="white", command=sayisal)
numaralar.config(font=("Arial", 12))
numaralar.grid(column=0, row=10)
numaralar.grid()

def bilgi():
    dosya ="Yardım sayfasına hoş geldiniz. 1. Yeni Rakam Listesi adlı butona her tıklamanızda 6 adet yeni sayı dizisi sizi karşılayacaktır. 2. Çıkış adlı butona tıkladığınızda sistemden tamamen ayrılmış olacaksınız "
    bilgi = Label(pencere, text= dosya)
    bilgi.config(font=("Arial", 11))
    bilgi.grid(column=10, row=11)
    bilgi.grid()

yardım= Button(pencere, text=" Yardım", fg="black", bg="white", command= bilgi)
yardım.config(font=("Arial", 12))
yardım.grid()



cikis = Button (pencere, text="Çıkış Yap", command= pencere.quit,fg="black", bg="white")
cikis.config(font=("Arial", 12))
cikis.grid(column=0, row=20)
cikis.grid()
pencere.mainloop()


