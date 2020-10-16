from bs4 import BeautifulSoup
import requests
import tkinter as tk
import tkinter.messagebox




def GUI():
    root = tk.Tk()


    root.title('CPU Stat Finder')

    # empty variables for radio buttons and entry widgets
    GUI.brand = tk.StringVar(None, 'AMD')

    GUI.model = tk.StringVar()

    # Window size/resizing lock
    root.geometry('285x240')
    root.wm_resizable(width=False, height=False)
    root.resizable(0, 0)

    # Widgets
    
    canvas = tk.Canvas(root,bg='white')
    canvas.place(relwidth=1, relheight=1)

    label = tk.Label(root, text='Brand:', bg = 'white',bd =3)
    label.place(relx=.2, rely=.3)

    label2 = tk.Label(root, text='Model:',bg='white')
    label2.place(relx=.2, rely=.5)

    entry = tk.Entry(root, textvariable=GUI.model, bg = '#d4d6d5')
    entry.place(relx=.4, rely=.5)

    rad_amd = tk.Radiobutton(text='AMD', variable=GUI.brand, value='AMD', bg='white')
    rad_amd.place(relx=.6, rely=.3)

    rad_intel = tk.Radiobutton(text='Intel', variable=GUI.brand, value='Intel',bg='white')
    rad_intel.place(relx=.4, rely=.3)

    # Use beautiful soup to parse URL, based on user's input
    def info():
        try:
            url = requests.get('http://www.cpubenchmark.net/cpu.php?cpu={}+{}'.format(GUI.brand.get(), GUI.model.get()))
            site = url.text
            soup = BeautifulSoup(site, 'html.parser')
            info = soup.find(class_='right-desc')
            info.prettify()
            return info.text

        except AttributeError:
            return 'No CPU found. Sorry!'

    # Show output of info() in new window
    def Result(event = None):
        result = tk.messagebox.showinfo('Search Results',info())

    entry.bind('<Return>',Result)
    
    
    # Call new window on button click
    button = tk.Button(root, text='GO!!!', command=lambda: Result(), bg ='white')
    button.place(relx=.43, rely=.8)

    root.mainloop()


GUI()



