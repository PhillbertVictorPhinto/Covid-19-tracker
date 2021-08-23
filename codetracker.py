import requests
import bs4
import tkinter as tk

def getdata(url):

    data = requests.get(url)
    return data


def coviddata():

    url ="https://www.worldometers.info/coronavirus/"

    html_data =getdata(url)
    bs =bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll('div',id="maincounter-wrap")
    all_data=''

    for block in info_div:
        text=block.find("h1",class_=None).get_text()
        count = block.find("span",class_=None).get_text()
        all_data= all_data + text +" "+count + "\n"

    return all_data

def getcountry_data():
    name = textfield.get()

    url="https://www.worldometers.info/coronavirus/country/"+name


    html_data = getdata(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll('div', id="maincounter-wrap")
    all_data = ''

    for i in range(3):
        text = info_div[i].find("h1", class_=None).get_text()

        count = info_div[i].find("span", class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"

    mainlabel['text'] = all_data


def reload():
    new_data = coviddata()
    mainlabel['text'] =new_data

coviddata()

root=tk.Tk()

root.geometry("900x700")

root.title("Covid Tracking System")

f=("poppins",25,"bold")

banner=tk.PhotoImage(file='corono_fevicon.png')

bannerlabel = tk.Label(root,image=banner)

bannerlabel.pack()

textfield=tk.Entry(root, width=50)
textfield.pack()

mainlabel=tk.Label(root, text=coviddata(),font=f)
mainlabel.pack()



gbtn = tk.Button(root,text="Get data",font=f,relief='solid',command=getcountry_data)
gbtn.pack()

rbtn = tk.Button(root,text="Reload",font=f,relief='solid',command=reload)
rbtn.pack()

root.mainloop()
