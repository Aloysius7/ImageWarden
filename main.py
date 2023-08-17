from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

main_img = None
wm_img = None

#Upload File Function
def main_upload_file():
    global main_img
    f_types = [('Png Files', '*.png'),('Jpg Files','*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    main_img = Image.open(filename).convert("RGBA")

# Upload Watermark Function
def wm_upload_file():
    global wm_img
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    wm_img = Image.open(filename).convert("RGBA")

# Process Function
def process():
    global main_img
    global wm_img
    if main_img and wm_img:

        x, y = main_img.size
        wm_img = wm_img.resize((x, y))

        main_img.putalpha(225)
        wm_img.putalpha(150)

        img3 = Image.alpha_composite(main_img, wm_img)
        img3.show()
    else:
        messagebox.showwarning("Warning","Did not import an image")


#Window
window = Tk()
window.geometry('400x300')
window.title('WaterMark Adder')
window.config(bg="#2b2d30")
left_frame = Frame(window, width=370, height=270, bg="#1e1f22")
left_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
window.resizable(False,False)

#Import Main Image File
i_label = Label(text="Upload the Image here", bg= "#1e1f22", fg= "#9ca4a4").place(relx=0.5, rely=0.1, anchor=CENTER)
i_import_button = Button(window, text='Import', command=main_upload_file, bg= "#2b2d30", fg= "#9ca4a4").place(relx=0.5, rely=0.2, anchor=CENTER, width=100)

#Import WaterMark Image File
w_label = Label(text="Upload the watermark here", bg= "#1e1f22", fg= "#9ca4a4").place(relx=0.5, rely=0.3, anchor=CENTER)
w_import_button = Button(window, text='Import', command=wm_upload_file,bg= "#2b2d30", fg= "#9ca4a4").place(relx=0.5, rely=0.4, anchor=CENTER, width=100)

#Process Button
process_button = Button(window, text='Process', command=process, bg= "#2b2d30", fg= "#9ca4a4").place(relx=0.5, rely=0.8, anchor=CENTER, width=200)

window.mainloop()