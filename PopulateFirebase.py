import wx
import pandas as pd
import requests
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

# u need to have admin credentials, download the JSON then just add it to this path
cred = credentials.Certificate(os.path.join("D:","/admin-key.json"))

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://croitorie-ioana-vue.firebaseio.com/'   ### the database url u can find it in Realtime Database 
})



Reference=''
Elements=0
valueelm = list()
nameelm= list()
name = list()
value = list()






class MyFrame(wx.Frame): 

    


 

    def __init__(self):
        super().__init__(parent=None, title='Populate Firebase Database',size=(750,200),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        global panel 
        panel = wx.Panel(self)
        w = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)
        h = wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)
        self.SetPosition(wx.Point(w/3.5,h/20))
      

        self.sommation = None

        #### GUI def

        self.AdressFormat=wx.StaticText(panel , pos=(75,50), label='Enter the reference')
        self.GetReference = wx.TextCtrl(panel, pos=(50, 75), size=(350,25))
        self.AdressFormat=wx.StaticText(panel , pos=(445,80), label='Nr of Elm:')
        self.NrElm =  wx.TextCtrl(panel, pos=(500, 75), size=(50,25))
        self.BeginPopulate = wx.Button(panel, label='Begin to Populate', pos=(575, 75))
        self.BeginPopulate.Bind(wx.EVT_BUTTON,self.onclick)

        
        
        self.TitleOfAPP=wx.StaticText(panel,pos=(220,10), label='POPULATE FIREBASE DATABASE',size=(300,30) )
        font=wx.Font(20,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.TitleOfAPP.SetFont(font)
       
      
 
        #### Elements that appear after u press 'Begin to Populate'
       
        self.UplBtn = wx.Button(panel , label='Upload to Database', pos=(550,850))
        self.UplBtn.Bind(wx.EVT_BUTTON, self.onClickUpload)

        self.Show()


            


    def onClickUpload(self,event):
        
        Reference = (str(self.GetReference.GetValue())) 
        Elements = (str(self.NrElm.GetValue()))          
        for elm in range(int(Elements)):
            name.append(str(nameelm[elm].GetValue()))
            value.append(str(valueelm[elm].GetValue()))
            
        
        print(name)
        print(value)

        ref = db.reference(Reference) 

        for elm in range(int(Elements)):
           
           ref.update({ name[elm] : value[elm]})




    
    def onclick(self,event):
        Reference = (str(self.GetReference.GetValue()))    
        Elements = (str(self.NrElm.GetValue()))
        posytext= 200
        posystatic= 205
        
        if Reference!='' and Elements!=0:
            self.SetSize(750,1000)
            
            
            for elm in range(int(Elements)):
                valueelm.append("Value"+str(elm))
                nameelm.append("Elm"+str(elm))

                statictextn="Elm nr "+str(elm)+" :"
                nameelm[elm] = wx.TextCtrl(panel, pos=(100, posytext), size=(250,25))
                nametext=wx.StaticText(panel , pos=(40,posystatic), label=statictextn )
                valueelm[elm] = wx.TextCtrl(panel, pos=(430, posytext), size=(250,25))
                valuetext=wx.StaticText(panel , pos=(380,posystatic), label="Value :" )
                posytext+=50
                posystatic+=50
        
        
   

if __name__ == '__main__': # funcția main 
    
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


