from pytube import YouTube  # Video indirebilmek için Pytube kütüphaneyi ekliyoruz
from pytube import Playlist  # Playlist indirebilmek için Pytube kütüphaneyi ekliyoruz
from tkinter import *
from tkinter.filedialog import askdirectory  # İndirilen dosyayı kaydedeceğimiz yolu sorabilmek için bu kütüphaneyi ekliyorz.


# region FONKSİONLAR
def Video():  # Video indirme fonksiyonumuz.
    label2.configure(text="İŞLEME BAŞLANIYOR")
    try:  # Hata yok ise bu kısım çalışıyor
        video = YouTube(link.get()) # Youtube nesnesi oluşturup içine alacağı string'i ikinci link Entry'sine girilen değer olarak atıyoruz.
        stream = video.streams.get_highest_resolution()  # Yüksek çözünürlükte video indirme komutu veriyoruz.
        stream.download(dosyaYolu.get())  # Burada download("x") içine dosyanın hangi konuma indirileceği parametresini alır. dosyaYolu adlı Entry'de seçilen konuma indiriyoruz.
        label.configure(text="{} Adlı Video başarıyla indirildi".format(video.title))

    except: # Eğer hata varsa bu kısım çalışıyor ve ekrandaki label'a hata var yazdırıyoruz
        label.configure(text="Something went wrong with the VIDEO download process")


def Audio():  # Ses indirme fonksiyonumuz
    label2.configure(text="İŞLEME BAŞLANIYOR")
    try:
        label2.configure(text="İŞLEME BAŞLANIYOR")
        audio = YouTube(link.get())
        label.configure(text="{}Adlı SES başarıyla indirildi".format(audio.title))
        stream = audio.streams.get_audio_only() #Burada streams.get_audio_only() diyerek videonun sadece sesini indirmek istediğimizi belirtiyoruz.
        stream.download(dosyaYolu.get())
    except:
        label.configure(text="Something went wrong with the AUDIO download process")


def PlayList():  # Playlist indirme fonksiyonumuz
    try:
        label2.configure(text="İŞLEME BAŞLANIYOR")
        playlist = Playlist(link.get())
        label.configure(
            text="{0} Adlı Playlistin {1} \t Elemanı Başarıyla İndirildi".format(playlist.title, playlist.length))

        for a in playlist.videos[
                 :2]:  # Burada for döngüsü yardımıyla playlist nesnesinin içindeki videolara erişip tek tek indiriyoruz.
            a.streams.first().download(dosyaYolu.get())

    except:
        label.configure(text="something went wrong with the PLAYLİST download process")


def PlaceHolder():
    # Burası dosyYolu adlı Entry'e tıklandığı zaman çalışıyor. Hatırlarsanız Entry'lerin text Attribute'lerine hangi işlem için kullanılacağını yazmıştık.
    # Örneğin "Dosya konumunu seç" veya "Link" gibi. Tıklandığında text Attribute'sini temizlemek ve place holder eklemek için bu fonksiyonu kullanıyoruz..
    dosyaYolu.delete(0, END)  # İlk ve son karakter aralığında olan tüm karakterleri siliyoruz.
    filename = str(askdirectory())  # Tkinter sayesinde kullanıcıdan indirilen dosyanın yolunu alıp string'e çevirdikten sonra daha sonra kullanabilmek için bir değişkene atıyoruz.
    dosyaYolu.insert(END,filename)  # Kullanıcı görebilsin diye dosyYolu adlı Entry'nin text'ine dosya yolunu yazdırıyoruz.
    filepath = filename.replace(" ", "") # Yukarıda oluşturduğumuz dosya yolunu bir dizi süzgeç işleminden geçiriyorum.

# endregion
# region TKİNTER ARAYÜZÜ
window = Tk()  # Pencere oluşturuyoruz
window.title("Python Youtube Video Downloader")  # Pencerenin başlığını yazıyoruz.
window.geometry("600x300")  # Pencere boyutunu ayarlıyoruz.
window.maxsize(width=700, height=400)  # Pencerenin maximum boyutunu giriyoruz.

label = Label(text="")  # Oluşturduğumuz pencereye label ekliyoruz
label.place(x=300, y=30, anchor="center")  # Label'in konumunu belirtiyoruz.

label2 = Label(text="")
label2.place(x=300, y=5, anchor="center")

dosyaYolu = Entry(window, width=50, justify="left")  # Pencerede Entry(textbox) oluşturuyoruz
dosyaYolu.bind("<Button-1>",lambda event: PlaceHolder())  # bind ile tıklandığı zaman PlaceHolder adlı fonksiyona yönlendiriyoruz.
dosyaYolu.place(x=80, y=50)  # Textbox'un konumunu belirtiyoruz
dosyaYolu.insert(0,"İndirmek istediğiniz dosya konumunu seçiniz")  # Kullanıcının anlaması için bu Entry'i ne amaçla kullanacağını yazdırıyoruz.

link = Entry(window, width=50, justify="left")
link.place(x=80, y=100)
link.insert(0, "Link")

buttonVideo = Button(window, text="Video", width=10, command=Video)  # Pencerede buton oluşturuyoruz.
# Command ile click event'inde hangi fonksiyonun çalıştırılacağını seçiyoruz.
buttonVideo.place(x=80, y=140)  # Butonun konumunu belirtiyoruz.

audioVideo = Button(window, text="Audio", width=10, command=Audio)
audioVideo.place(x=180, y=140)

playlistVideo = Button(window, text="Playlist", width=10, command=PlayList)
playlistVideo.place(x=280, y=140)
window.mainloop()

# endregion
