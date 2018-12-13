import tkinter as tk
import time as t
import datetime as dt
import webbrowser as wb



class Clock:
    """
    Class untuk menjalankan program Clock & Timer begitu di panggil
    """
    def __init__(self, master):
        # Menyatakan instance variable untuk di pakai nanti
        self.time = t.strftime("%H : %M : %S") # waktu sekarang
        self.calendar = t.strftime("%a, %B %Y") # tanggal sekarang
        self.music_url = "https://youtu.be/0VCD1GraOAs?t=51"

        # Mengatur beberapa bagian dari windows seperti root, judul, luas dan ikon
        self.master = master
        self.master.iconbitmap("Clock & Timer3.ico")
        self.master.configure(background='#5d5f60')
        self.master.title("Clock & Timer")
        self.master.geometry("504x530")
        self.master.resizable(0,0)

        # Membuat kanvas untuk display jam dan timer
        self.clock_canvas = tk.Canvas(self.master, bg="#5d5f60",
                                        width=500, height=500,
                                        bd=0, highlightthickness=0)
        self.timer_canvas = tk.Canvas(self.master, bg="#5d5f60",
                                        width=500, height=475,
                                        bd=0, highlightthickness=0)

        # Membuat beberapa tombol yang di modifikasi pada program
        self.clock_button = HoverButton(self.master, text="Clock",
                                        command=self.clock_layout,
                                        padx=30, pady=10,
                                        font='verdana 12 bold',
                                        bg="#5d5f60",
                                        activebackground="#848991", bd=0)
        self.timer_button = HoverButton(self.master, text="Timer",
                                        command=self.timer_layout,
                                        padx=30, pady=10,
                                        font='verdana 12 bold', bg="#5d5f60",
                                        activebackground="#848991", bd=0)
        self.start_button = HoverButton(self.master, text="Start",
                                        command=self.timer, fg="white",
                                        bg="#079b23", relief=tk.GROOVE,
                                        activeforeground="#079b23", bd=3,
                                        activebackground='#2ee853', padx=15)
        self.reset_button = HoverButton(self.master, text="Reset",
                                        command=self.reset, fg="white",
                                        bg="#ed0909", relief=tk.GROOVE,
                                        activeforeground="#e01a0f", bd=3,
                                        activebackground='#e24444',padx=40)

        # Membuat input untuk timer
        self.timer_entry_hour = tk.Entry(self.master, justify='center',
                                        validate='all',
                                        validatecommand=(self.master.register(self.only_int), '%P'),
                                        bg="#848991", bd=0,
                                        font="verdana 10 bold", width=13) # Input Jam
        self.seperate_label1 = tk.Label(self.master, text=":",
                                        bg="#5d5f60", font="verdana 10 bold") # Label pemisah " : "
        self.timer_entry_minute = tk.Entry(self.master, justify='center',
                                        validate='all',
                                        validatecommand=(self.master.register(self.only_int), '%P'),
                                        bg="#848991", bd=0,
                                        font="verdana 10 bold", width=13) # Input menit
        self.seperate_label2 = tk.Label(self.master, text=":",
                                        bg="#5d5f60", font="verdana 10 bold") # Label pemisah " : "
        self.timer_entry_second = tk.Entry(self.master, justify='center',
                                        validate='all',
                                        validatecommand=(self.master.register(self.only_int), '%P'),
                                        bg="#848991", bd=0,
                                        font="verdana 10 bold", width=13) # Input detik

        # Menggambar text di kanvas untuk bagian awalnya
        self.timer_canvas.create_text(245, 225, text="0:00:00", font="verdana 30") # Mengatur 0:00:00 pada timer
        self.clock_canvas.create_text(245, 450, text="Created by SEAN", font="algerian 10") # Watermark
        self.timer_canvas.create_text(245, 422, text="Created by SEAN", font="algerian 10") # Watermark

        # Menaruh tombol dan kanvas jam
        self.clock_button.grid(row=0,column=0, columnspan=2) # Menampilkan jam untuk pertama kali
        self.clock_canvas.grid(row=1,column=0, columnspan=6)
        self.timer_button.grid(row=0,column=4, columnspan=2)



    def tick(self):
        """
        Membuat jam selalu update dengan waktu terbaru dengan menghapus
        dan menggambar ulang setiap 200ms
        """
        self.clock_canvas.delete("all") # Menghapus Semua yang ada di kanvas agar dapat di gambar ulanng
        self.time = t.strftime("%H : %M : %S") # Mengupdate waktu terbaru
        self.calendar = t.strftime("%a, %B %Y") # Mengupdate tanggal baru
        self.clock_canvas.create_text(245, 225, text=self.time,
                                        font="verdana 30") # Menggambar ulang waktu
        self.clock_canvas.create_text(245, 270, text=self.calendar,
                                        font="verdana 15") # Menggambar ulang tanggal
        self.clock_canvas.create_text(245, 450, text="Created by SEAN",
                                        font="algerian 10") # Menggambar ulang watermark
        self.clock_canvas.after(200, self.tick) # Mengulangi fungsi ini setiap 200ms

    def reset(self):
        """
        Untuk mengatur kembali semua menjadi seperti awal
        """
        self.all_sec = -3 # Di teruskan ke method timer


    def timer(self):
        """
        Menjalankan perhitungan mundur dengan menghapus dan menulis ulang,
        Jika sudah mencapai 0:00:00 akan membuka url sebagai penanda suara,
        method ini hanya akan berfungsi jika salah satu dari input memiliki nilai
        """
        # mengecek apakah semua input kosong
        if len(self.timer_entry_hour.get()) != 0 or len(self.timer_entry_minute.get()) != 0 or len(self.timer_entry_second.get()) != 0:

            # Mengecek apakan input jam kosong
            if self.timer_entry_hour.get().isdecimal():
                hour_in_sec = int(self.timer_entry_hour.get())*3600 # Menjadikan detik
            else:
                hour_in_sec = 0

            # Mengecek apakan input menit kosong
            if self.timer_entry_minute.get().isdecimal():
                minute_in_sec = int(self.timer_entry_minute.get())*60 # Menjadikan detik
            else:
                minute_in_sec = 0

            # Mengecek apakan input detik kosong
            if self.timer_entry_second.get().isdecimal():
                sec = int(self.timer_entry_second.get())
            else:
                sec = 0
            self.all_sec = hour_in_sec + minute_in_sec + sec
            self.displayed_time = dt.timedelta(seconds=self.all_sec) # j:mm:dd

            def counting():
                """
                Akan menjalankan dan mendisplay perhitungan mundur,
                dihitung dengan mengurangi detik(all_sec) dengan 1 setiap 1 detik
                dan menampilkannya dengan j:mm:dd,
                saat perhitungan mundur tidak dapat berpindah kanvas jika tidak di reset,
                dipicu oleh tombol "Start"
                """
                self.timer_canvas.delete("all")
                self.timer_canvas.create_text(245, 225, text=str(self.displayed_time),
                                            font="verdana 30") # Menggambar waktu
                self.timer_canvas.create_text(245, 469, text="Created by SEAN",
                                            font="algerian 10") # Watermark
                # Jika detik masih lebih besar dari -1 akan terus di kurangi
                if self.all_sec > -1: # Agar tetap menampilkan 0:00:00
                    self.all_sec -= 1

                self.displayed_time = dt.timedelta(seconds=self.all_sec) # Menjadikan detik yg telah dikurangi ke j:mm:dd

                # Jika detik sudah sama dengan -1 maka akan berhenti dan menggambar"Times Up!!"
                if self.all_sec == -1:
                    self.timer_canvas.delete("all")
                    self.timer_canvas.create_text(245, 225, text="Times Up !!",
                                            font="verdana 30")
                    self.timer_canvas.create_text(245, 422, text="Created by SEAN",
                                            font="algerian 10")

                    # Membuka url untuk penanda suara
                    wb.open_new_tab(self.music_url)

                    # Menampilkan tombol yang hilang
                    self.start_button.grid(row=1, column=5)
                    self.clock_button.grid(row=0,column=0, columnspan=2)
                    self.timer_button.grid(row=0,column=4, columnspan=2)

                    # mengambalikan input yang hilang
                    self.timer_entry_hour.grid(row=1,column=0)
                    self.seperate_label1.grid(row=1,column=1)
                    self.timer_entry_minute.grid(row=1,column=2)
                    self.seperate_label2.grid(row=1,column=3)
                    self.timer_entry_second.grid(row=1,column=4)

                    # Menghilangkan tombol reset
                    self.reset_button.grid_forget()

                # Yang di eksekusi jika menekan tombol reset
                elif self.all_sec == -3:
                    self.timer_canvas.delete("all")
                    self.timer_canvas.create_text(245, 225, text="0:00:00",
                                                font="verdana 30") # Menset ke angka 0:00:00
                    self.timer_canvas.create_text(245, 422, text="Created by SEAN",
                                                font="algerian 10")
                    # Mengembalikan tombol-tombol
                    self.clock_button.grid(row=0,column=0, columnspan=2)
                    self.start_button.grid(row=1, column=5)
                    self.timer_button.grid(row=0,column=4, columnspan=2)

                    # Mengembalikan input yang hilang
                    self.timer_entry_hour.grid(row=1,column=0)
                    self.seperate_label1.grid(row=1,column=1)
                    self.timer_entry_minute.grid(row=1,column=2)
                    self.seperate_label2.grid(row=1,column=3)
                    self.timer_entry_second.grid(row=1,column=4)

                    # Menghilangkan tombol reset
                    self.reset_button.grid_forget()
                # Jika detik tidak sama dengan -1 atau tidak menekan reset maka akan terus di hitung
                else:
                    self.timer_canvas.after(1000, counting) # Mengulang fungsi setiap detik

            counting() # Memicu fungsi counting berjalan

            # Karena menghilangkan tombol maka kanvas harus di besarkan
            self.timer_canvas.config(width=500, height=500)

            # Menghilangkan tombol-tombol
            self.start_button.grid_forget()
            self.clock_button.grid_forget()
            self.timer_button.grid_forget()

            # Menghilangka input waktu
            self.timer_entry_hour.grid_forget()
            self.seperate_label1.grid_forget()
            self.timer_entry_minute.grid_forget()
            self.seperate_label2.grid_forget()
            self.timer_entry_second.grid_forget()

            # Memunculkan tombol reset
            self.reset_button.grid(row=1, column=2, columnspan=2)


    def timer_layout(self):
        """
        menampilkan kanvas timer jika menekan tombol "Timer",
        menghilangkan kanvas jam
        """
        # Kanvas jam dihilangkan
        self.clock_canvas.grid_forget()

        # Memunculkan tombol start
        self.start_button.grid(row=1, column=5)

        # Memunculkan kanvas timer
        self.timer_canvas.grid(row=2,column=0, columnspan=6)

        # Mengembalikan ke display awal
        self.timer_canvas.delete("all")
        self.timer_canvas.create_text(245, 225, text="0:00:00",
                                                font="verdana 30") # Menset ke angka 0:00:00
        self.timer_canvas.create_text(245, 422, text="Created by SEAN",
                                                font="algerian 10") # Watermark

        # Memunculkan semua input waktu
        self.timer_entry_hour.grid(row=1,column=0)
        self.seperate_label1.grid(row=1,column=1)
        self.timer_entry_minute.grid(row=1,column=2)
        self.seperate_label2.grid(row=1,column=3)
        self.timer_entry_second.grid(row=1,column=4)

    def clock_layout(self):
        """
        Menampilkan kanvas jam,
        menghilangkan semua widget yang bersangkutan dengan timer
        """
        # Menghilangkan kanvas timer
        self.timer_canvas.grid_forget()

        # Menghilangkan input waktu
        self.timer_entry_hour.grid_forget()
        self.seperate_label1.grid_forget()
        self.timer_entry_minute.grid_forget()
        self.seperate_label2.grid_forget()
        self.timer_entry_second.grid_forget()

        # Menghilangkan tombol start
        self.start_button.grid_forget()

        # Memunculkan kanvas jam
        self.clock_canvas.grid(row=1,column=0, columnspan=6)


    def only_int(self, num):
        """
        Membatasi input yang di perbolehkan yaitu hanya angka dan hanya bisa 2 digit
        """
        # Pengecekan input
        if (str.isdigit(num) or num == "") and len(num) <= 2:
            return True

        # Selain angka dan lebih dari 2 digit maka tidak bisa
        else:
            return False



class HoverButton(tk.Button):
    """
    Memodifikasi tk.Button supaya saat kursor ada di atasnya maka dia akan berubah warna
    """
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter) # Saat kursor di atasnya
        self.bind("<Leave>", self.on_leave) # Saat Kursoe keluar

    def on_enter(self, e):
        """
        Mengubah warna background menjadi activebackground
        """
        self['background'] = self['activebackground']

    def on_leave(self, e):
        """
        Mengembalikan warna ke background semula
        """
        self['background'] = self.defaultBackground


def main():
    m = tk.Tk()
    a = Clock(m)
    a.tick()
    m.mainloop()

if __name__ == "__main__":
    main()
