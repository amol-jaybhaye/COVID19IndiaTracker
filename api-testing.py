from tkinter import *
import requests
import json
from tkinter import messagebox

top = Tk()

top.title("Covid-19 Data")
top.geometry("650x400")

#Getting data from api 
response_API = requests.get('https://api.covid19india.org/data.json')
data = response_API.text
type_json = json.loads(data)

# printing a list of states
Lb1 = Listbox(top, width=45, height=23)

for i in range(38):
     Lb1.insert(i, str(i)+ ") " + type_json['statewise'][i]['state'])

Lb1.place(x=0, y=0)

L1 = Label(top, text="Enter State Code")
L1.place(x=400, y=25)
E1 = Entry(top, )
E1.place(x=400, y=50)

def msg():
     En = E1.get()
     try:
          En = int(En)
     except ValueError:
          messagebox.showerror("error", "Please enter valid code")
     else:
          if En in range(38):
               messagebox.showinfo(
                    "covid info",  type_json['statewise'][En]['state'] + "\n" +
                     "active : " + type_json['statewise'][En]['active'] +  "\n"
                     "confirmed : " + type_json['statewise'][En]['confirmed'] + "\n" +
                     "deaths : " + type_json['statewise'][En]['deaths'] + "\n" +
                     "recovered : " + type_json['statewise'][En]['recovered'])
          else:
               messagebox.showerror("error", "only 0 to 38 code numbers are available!")

B1 = Button(top, text="submit", command=msg, padx=40, bg="green")
B1.place(x=400, y=75)

top.mainloop()