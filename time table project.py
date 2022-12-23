from tkinter import *
from tkinter import messagebox
import pyttsx3
root=Tk()
root.title("TIME TABLE GENERATOR")

engine=pyttsx3.init()

def table():
    return



#inputting values



#weekly time table function                                               
def weekly():
    
    messagebox.showinfo("WEEKLY TIME TABLE","WEEKLY TIME TABLE")
   
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("WEEKLY TIME TABLE")
    engine.runAndWait()
    


#class
def classs():
    messagebox.showinfo("CLASS","CLASS")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("CLASS")
    engine.runAndWait()
    

#period 1
def I():
    messagebox.showinfo("I","I")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("FIRST PERIOD")
    engine.runAndWait()
    


#period 2
def II():
    messagebox.showinfo("II","II")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("SECOND PERIOD")
    engine.runAndWait()
        

#period 3
def III():
    messagebox.showinfo("III","III")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("THIRD PERIOD")
    engine.runAndWait()
        

#period 4
def IV():
    messagebox.showinfo("IV","IV")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("FOURTH PERIOD")
    engine.runAndWait()
        

#period 5
def V():
    messagebox.showinfo("V","V")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("FIFTH PERIOD")
    engine.runAndWait()
        

#period 5
def VI():
    messagebox.showinfo("VI","VI")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("SIXTH PERIOD")
    engine.runAndWait()



#XII A        
def  xiia():
    messagebox.showinfo("XII A","CLASS 'XII'- A")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("CLASS TWELVE A")
    engine.runAndWait()
        

# XII B
def xiib():
    
    messagebox.showinfo("XII B","CLASS 'XII'- B")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("CLASS TWELVE B")
    engine.runAndWait()
        

#XII C
def xiic():
    messagebox.showinfo("XII C","CLASS 'XII'- C")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("CLASS TWELVE C")
    engine.runAndWait()
        

#XII D
def xiid():
    messagebox.showinfo("XII D","CLASS 'XII'- D")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("CLASS TWELVE D ")
    engine.runAndWait()
        
#XII E
def xiie():
    messagebox.showinfo("XII E","CLASS 'XII'- E")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("CLASS TWELVE E")
    engine.runAndWait()
        
#PHYSICS OF 12 A
def phyA():
    messagebox.showinfo("PHYSICS","MS RUCHI KAPOOR\n7:30 a.m. to 8:30 a.m.\nYour classteacher code is 9187")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS RUCHI KAPOOR\n YOUR CLASS TIME IS FROM 7:30 a.m. to 8:30 a.m.\nYour classteacher code is 9187")
    engine.runAndWait()
        

#MATHS OF 12 A
def mathsA():
    messagebox.showinfo("MATHS","MS PURNIMA PANDEY\n8:45 a.m. to 9:45 a.m.\nYour classteacher code is 1956")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 8:45 a.m. to 9:45 a.m.\nYour classteacher code is 1956")
    engine.runAndWait()
        

#CS PE  OF 12 A
def cspeA():
    messagebox.showinfo("COMPUTER SCIENCE/P.E","MS PRIYA KOLTE\n10:00 a.m. to 11:00 a.m.\nYour classteacher code is 0101\nNEGI SIR\n10:00 a.m. to 11:00 a.m.\n Your classteaher code is 1234")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 10:00 a.m. to 11:00 a.m.\nYour classteacher code is 0101\n MISTER NEGI SIR\n YOUR CLASS TIME IS FROM 10:00 a.m. to 11:00 a.m.\n Your classteaher code is 1234")
    engine.runAndWait()
        



def breaks():
    messagebox.showinfo("B","BREAK")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("BREAK")
    engine.runAndWait()
        

#ENGLISH OF 12 A
def engA():
    messagebox.showinfo("ENGLISH","MS RUPALI GOSWAMI\n11:15 a.m to 12:15 p.m.\nYour classteacher code is 5679")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS RUPALI GOSWAMI\n YOUR CLASS TIME IS FROM 11:15 a.m to 12:15 p.m.\nYour classteacher code is 5679")
    engine.runAndWait()
        


#CHEMISTRY OF 12 A
def chemA():
    messagebox.showinfo("CHEMISTRY","MS MANI SRIVASTAVA\n12:30 p.m. to 1:30 p.m.\nYour classteacher code is 0012")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS MANI SRIVASTAVA\n YOUR CLASS TIME IS FROM 12:30 p.m. to 1:30 p.m.\nYour classteacher code is 0012")
    engine.runAndWait()
        


#ENGLISH OF 12 B
def engB():
   messagebox.showinfo("ENGLISH","MS RUPALI GOSWAMI\n7:30 a.m. to 8:30 a.m.\nYour classteacher code is 2215")
   engine=pyttsx3.init()
   voices=engine.getProperty('voices')
   engine.setProperty('voice',voices[1].id)
   engine.say("MISS RUPALI GOSWAMI\n YOUR CLASS TIME IS FROM  7:30 a.m. to 8:30 a.m.\nYour classteacher code is 2215")
   engine.runAndWait()

      
#CHEMISTRY OF 12 B
def chemB():
    messagebox.showinfo("CHEMISTRY","MS DEEPIKA SINGHAL\n8:45 a.m. to 9:45 a.m.\nYour classteacher code is 1220")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS DEEPIKA SINGHAL\n YOUR CLASS TIME IS FROM 8:45 a.m. to 9:45 a.m.\nYour classteacher code is 1220")
    engine.runAndWait()


        
#CS PE OF 12 B
def cspeB():
    
    messagebox.showinfo("COMPUTER SCIENCE/P.E","MS PRIYA KOLTE\n10:00 a.m. to 11:00 a.m.\nYour classteacher code is 0101\nNEGI SIR\n10:00 a.m. to 11:00 a.m.\n Your classteaher code is 1234")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 10:00 a.m. to 11:00 a.m.\nYour classteacher code is 0101\n MISTER NEGI SIR\n YOUR CLASS TIME IS FROM 10:00 a.m. to 11:00 a.m.\n Your classteaher code is 1234")
    engine.runAndWait()
        


def break1():
    messagebox.showinfo("R","BREAK")
    engine=pyttsx3.init()
    engine.say("BREAK")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.runAndWait()
        

#MATHS OF 12 B
def mathsB():
                                
    messagebox.showinfo("MATHS","MS PURNIMA PANDEY\n11:15 a.m. to 12:15 p.m.\nYour classteacher code is 2280")
    engine=pyttsx3.init()
    engine.say("MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 11:15 a.m. to 12:15 p.m.\nYour classteacher code is 2280")
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.runAndWait()
    

#PHYSICS OF 12 B
def phyB():
     messagebox.showinfo("PHYSICS","MS ANAGHA TAGARE\n12:30 p.m. to 1:30 p.m.\nYour classteacher code is 1974")
     engine=pyttsx3.init()
     engine.say("MISS ANAGHA TAGARE\nYOUR CLASS TIME IS FROM 12:30 p.m. to 1:30 p.m.\nYour classteacher code is 1974")
     voices=engine.getProperty('voices')
     engine.setProperty('voice',voices[1].id)
     engine.runAndWait()
    
# MATHS,BIO OF 12 C
def mathsbio():
    messagebox.showinfo("MATHS/BIOLOGY","MISS PURNIMA PANDEY\n7:30 a.m. to 8:30 a.m.\nYour classteacher code is 4132\n MISS SANGEETA NINGULE\n 7:30 a.m. to 8:30 a.m.\n YOUR CLASS TEACHER CODE IS 9821")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 7:30 a.m. to 8:30 a.m.\nYour classteacher code is 4132\n MISS SANGEETA NINGULE\n 7:30 a.m. to 8:30 a.m.\n YOUR CLASS TEACHER CODE IS 9821")
    engine.runAndWait()


#PHYSICS OF 12 C
def phyC():
    messagebox.showinfo("PHYSICS","MISS RUCHI KAPOOR\n YOUR CLASS TIME IS FROM 8:45 a.m. TO 9:45 a.m.\n Your class teacher code is 6654")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS RUCHI KAPOOR\n YOUR CLASS TIME IS FROM 8:45 a.m. TO 9:45 a.m.\n Your class teacher code is 6654")
    engine.runAndWait()


#ENGLISH OF 12 C
def engC():

       messagebox.showinfo("ENGLISH","MS ANANYA DEY\n10:00 a.m. to 11:00 a.m.\nYour classteacher code is 8764")
       engine=pyttsx3.init()
       voices=engine.getProperty('voices')
       engine.setProperty('voice',voices[1].id)
       engine.say("MISS ANANYA DEY \n YOUR CLASS TIME IS FROM 10:00  a.m. to 11:00 a.m.\nYour classteacher code is 8764")
       engine.runAndWait()                  


           
def break2():
    messagebox.showinfo("E","BREAK")
    engine=pyttsx3.init()
    engine.say("BREAK")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.runAndWait()


#CHEMISTRY OF 12 C
def chemC():
    messagebox.showinfo("CHEMISTRY","MS DEEPIKA SINGHAL\n 11:00 a.m. to 12:15 p.m.\nYour classteacher code is 0178")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS DEEPIKA SINGHAL\n YOUR CLASS TIME IS FROM 11:00 a.m. to 12:15 p.m.\nYour classteacher code is 0178")
    engine.runAndWait()


#CS PE ECO OF 12 C
def cspeecoC():
    messagebox.showinfo("C.S/P.E/ECO","MS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 1265\nMISTER NEGI SIR \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\n Your classteacher code is 3575\n MISS SONIA \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 4590")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 1265\nMISTER NEGI SIR \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\n Your classteacher code is 3575\n MISS SONIA \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 4590")
    engine.runAndWait()


#ENGLISH OF 12 D
def engD():
    messagebox.showinfo("ENGLISH","MISS SRIEKALA NAIR\n YOUR CLASS TIME IS FROM 7:30 A.M. TO 8:30 A.M\n Your classteacher code is 9402")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SRIEKALA NAIR\n YOUR CLASS TIME IS FROM 7:30 A.M. TO 8:30 A.M\n Your classteacher code is 9402")
    engine.runAndWait()
 

#BUSINESS STUDIES OF 12 D
def bstD():
    messagebox.showinfo("BUSINESS STUDIES","MISS SUCHITRA KAMAT\n YOUR CLASS TIME IS FROM 8:45 A.M. TO 9:45 A.M.\nYour clssteacher code is 8943")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SUCHITRA KAMAT\n YOUR CLASS TIME IS FROM 8:45 A.M. TO 9:45 A.M.\nYour clssteacher code is 8943")
    engine.runAndWait()


#MATHS,CS,PE OF 12 D
def mathscspe():
    messagebox.showinfo("MATHS/COMPUTER SCIENCE/P.E.","MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 1345\nMISS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 3578\nMISTER NEGI SIR\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 8932")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 1345\nMISS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 3578\nMISTER NEGI SIR\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 8932")
    engine.runAndWait()



def break3():
    messagebox.showinfo("A","BREAK")
    engine=pyttsx3.init()
    engine.say("BREAK")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("BREAK")
    engine.runAndWait()


#ACOUNTS OF 12 D
def accountsD():
    messagebox.showinfo("ACCOUNTANCY","MISS SARIKA GALGALI\n YOUR CLASS TIME IS FROM 11:15 A.M. TO 12:15 P.M.\n Your classteacher code is 7779")       
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SARIKA GALGALI\n YOUR CLASS TIME IS FROM 11:15 A.M. TO 12:15 P.M.\n Your classteacher code is 7779")
    engine.runAndWait()


#ECONOMICS OF 12 D
def ecoD():
    messagebox.showinfo("ECONOMICS","MISS SONIA \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 4590")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SONIA \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 4590")
    engine.runAndWait()


#ENGLISH OF 12 E
def engE():
    messagebox.showinfo("ENGLISH","MISS ANANYA DEY\n YOUR CLASS TIME IS FROM 7:30 A.M. TO 8:30 A.M\n Your classteacher code is 9402")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS ANANYA DEY\n YOUR CLASS TIME IS FROM 7:30 A.M. TO 8:30 A.M\n Your classteacher code is 9402")
    engine.runAndWait()


#BUSINESS SUTDIES 12 E
def bstE():
    messagebox.showinfo("BUSINESS STUDIES","MISS SUCHITRA KAMAT\n YOUR CLASS TIME IS FROM 8:45 A.M. TO 9:45 A.M.\nYour clssteacher code is 8943")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SUCHITRA KAMAT\n YOUR CLASS TIME IS FROM 8:45 A.M. TO 9:45 A.M.\nYour clssteacher code is 8943")


#MATHS CS PE OF 12 E
def mathscspeE():
    messagebox.showinfo("MATHS/COMPUTER SCIENCE/P.E.","MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 1345\nMISS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 3578\nMISTER NEGI SIR\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 8932")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS PURNIMA PANDEY\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 1345\nMISS PRIYA KOLTE\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 3578\nMISTER NEGI SIR\n YOUR CLASS TIME IS FROM 10:00 A.M. TO 11 A.M.\n Your classteacher code is 8932")
    engine.runAndWait()

def break4():
    messagebox.showinfo("K","BREAK")
    engine=pyttsx3.init()
    engine.say("BREAK")
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("BREAK")
    engine.runAndWait()


#ACCOUNTS OF 12 E
def accountsE():
    messagebox.showinfo("ACCOUNTANCY","MISS SARIKA GALGALI\n YOUR CLASS TIME IS FROM 11:15 A.M. TO 12:15 P.M.\n Your classteacher code is 7779")       
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SARIKA GALGALI\n YOUR CLASS TIME IS FROM 11:15 A.M. TO 12:15 P.M.\n Your classteacher code is 7779")
    engine.runAndWait()


#ECONOMICS OF 12 E
def ecoE():
    messagebox.showinfo("ECONOMICS","MISS SONIA \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 4590")
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("MISS SONIA \n YOUR CLASS TIME IS FROM 12:30 P.M. TO 1:30 P.M.\nYour classteacher code is 4590")
    engine.runAndWait()





button_1=Button(root,text="CLASS",padx=50,pady=20,font='verdana 9 bold',command=classs,bg="indigo",fg="orange")
#CLASS 12 SECTIONS
button_2=Button(root,text="XII A",padx=50,pady=20,font='verdana 9 bold',command=xiia,bg="indigo",fg="orange")
button_4=Button(root,text="XII B",padx=50,pady=20,font='verdana 9 bold',command=xiib,bg="indigo", fg="orange" )
button_5=Button(root,text="XII C",padx=50,pady=20,font='verdana 9 bold',command=xiic,bg="indigo" ,fg="orange" )
button_6=Button(root,text="XII D",padx=50,pady=20,font='verdana 9 bold',command=xiid,bg="indigo",fg="orange" )
button_7=Button(root,text="XII E",padx=50,pady=20,font='verdana 9 bold',command=xiie,bg="indigo",fg="orange" )
#no.of periods
button_8=Button(root,text="I",padx=75,pady=20,font='verdana 9 bold',command=I, bg="orange", fg="indigo")
button_9=Button(root,text="II",padx=105,pady=20,font='verdana 9 bold',command=II, bg="indigo",fg="orange")
button_10=Button(root,text="III",padx=125,pady=20,font='verdana 9 bold',command=III,bg="orange",fg="indigo")
button_11=Button(root,text="IV",padx=50,pady=20,font='verdana 9 bold',command=IV, bg="indigo",fg="orange")
button_12=Button(root,text="V",padx=75,pady=20,font='verdana 9 bold',command=V,bg="orange",fg="indigo" )
button_13=Button(root,text="VI",padx=80,pady=20,font='verdana 9 bold',command=VI,bg="indigo",fg="orange" )
#SCIENCE A SECTION
button_14=Button(root,text="PHYSICS",padx=50,pady=20,font='verdana 9 bold',command=phyA, bg="orange",fg="indigo" )
button_15=Button(root,text="CHEMISTRY",padx=50,pady=20,font='verdana 9 bold',command=chemA,bg="indigo",fg="orange" )
button_16=Button(root,text="MATHS",padx=90,pady=20,font='verdana 9 bold',command=mathsA,bg="indigo",fg="orange" )
button_17=Button(root,text="COMPUTER SCIENCE/P.E.",padx=50,pady=15,font='verdana 9 bold',command=cspeA,bg="orange",fg="indigo" )
button_18=Button(root,text="ENGLISH",padx=50,pady=20,font='verdana 9 bold',command=engA,bg="orange",fg="indigo" )
#SCIENCE B SECTION
button_19=Button(root,text="PHYSICS",padx=60,pady=20,font='verdana 9 bold',command=phyB,bg="indigo",fg="orange" )
button_20=Button(root,text="CHEMISTRY",padx=75,pady=20,font='verdana 9 bold',command=chemB,bg="indigo",fg="orange" )
button_21=Button(root,text="MATHS",padx=55,pady=20,font='verdana 9 bold',command=mathsB,bg="orange", fg="indigo")
button_22=Button(root,text="COMPUTER SCIENCE/P.E.",padx=50,pady=20,font='verdana 9 bold',command=cspeB,bg="orange",fg="indigo")
button_23=Button(root,text="ENGLISH",padx=50,pady=20,font='verdana 9 bold',command=engB,bg="orange",fg="indigo" )
#SCIENCE C SECTION
button_24=Button(root,text="PHYSICS",padx=85,pady=20,font='verdana 9 bold',command=phyC,bg="indigo",fg="orange" )
button_25=Button(root,text="CHEMISRTY",padx=40,pady=20,font='verdana 9 bold',command=chemC,bg="orange",fg="indigo" )
button_26=Button(root,text="MATHS/BIOLOGY",padx=20,pady=20,font='verdana 9 bold',command=mathsbio,bg="orange", fg="indigo")
button_27=Button(root,text="C.S/P.E/ECO",padx=45,pady=20,font='verdana 9 bold',command=cspeecoC,bg="indigo",fg="orange" )
button_28=Button(root,text="ENGLISH",padx=105,pady=20,font='verdana 9 bold',command=engC,bg="orange",fg="indigo" )
#COMMERCE D SECTION
button_29=Button(root,text="BUSINESS STUDIES",padx=50,pady=20,font='verdana 9 bold',command=bstD,bg="indigo",fg="orange")
button_30=Button(root,text="ECONOMICS",padx=50,pady=20,font='verdana 9 bold',command=ecoD,bg="indigo",fg="orange" )
button_31=Button(root,text="ACCOUNTANCY",padx=30,pady=20,font='verdana 9 bold',command=accountsD,bg="orange",fg="indigo" )
button_32=Button(root,text="ENGLISH",padx=50,pady=20,font='verdana 9 bold',command=engD,bg="orange",fg="indigo" )
button_33=Button(root,text="MATHS/COMPUTER SCIENCE/P.E.",padx=25,pady=20,font='verdana 9 bold',command=mathscspe,bg="orange",fg="indigo")
#COMMERCE E SECTION
button_34=Button(root,text="BUSINESS STUDIES",padx=50,pady=20,font='verdana 9 bold',command=bstE,bg="indigo", fg="orange" )
button_35=Button(root,text="ECONOMICS",padx=50,pady=20,font='verdana 9 bold',command=ecoE,bg="indigo",fg="orange" )
button_36=Button(root,text="ACCOUNTANCY",padx=30,pady=20,font='verdana 9 bold',command=accountsE,bg="orange",fg="indigo" )
button_37=Button(root,text="ENGLISH",padx=50,pady=20,font='verdana 9 bold',command=engE,bg="orange",fg="indigo" )
button_38=Button(root,text="MATHS/COMPUTER SCIENCE/P.E.",padx=25,pady=20,font='verdana 9 bold',command=mathscspeE,bg="orange",fg="indigo") 
#break
button_39=Button(root,text="B",padx=50,pady=20,font='verdana 9 bold',command=breaks,bg="indigo",fg="orange" )
button_40=Button(root,text="R",padx=50,pady=20,font='verdana 9 bold',command=break1,bg="indigo",fg="orange")
button_41=Button(root,text="E",padx=50,pady=20,font='verdana 9 bold',command=breaks,bg="indigo",fg="orange" )
button_42=Button(root,text="A",padx=50,pady=20,font='verdana 9 bold',command=break1,bg="indigo", fg="orange")
button_43=Button(root,text="K",padx=50,pady=20,font='verdana 9 bold',command=break1,bg="indigo", fg="orange")
button_44=Button(root, text="WEEKLY TIMETABLE",padx=100,pady=20,font='verdana 9 bold',command=weekly)



#buttons grids
button_44.grid(row=1,column=3,ipadx=10)
#row2's
button_1.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_10.grid(row=2,column=3)
button_11.grid(row=2,column=4)
button_12.grid(row=2,column=5)
button_13.grid(row=2,column=6)


#row3's
button_2.grid(row=3,column=0)
button_14.grid(row=3,column=1)
button_16.grid(row=3,column=2)
button_17.grid(row=3,column=3)
button_39.grid(row=3,column=4)
button_18.grid(row=3,column=5)
button_15.grid(row=3,column=6)


#row4's
button_4.grid(row=4,column=0)
button_23.grid(row=4,column=1)
button_20.grid(row=4,column=2)
button_22.grid(row=4,column=3)
button_40.grid(row=4,column=4)
button_21.grid(row=4,column=5)
button_19.grid(row=4,column=6)


#row5's
button_5.grid(row=5,column=0)
button_26.grid(row=5,column=1)
button_24.grid(row=5,column=2)
button_28.grid(row=5,column=3)
button_41.grid(row=5,column=4)
button_25.grid(row=5,column=5)
button_27.grid(row=5,column=6)


#row6's
button_6.grid(row=6,column=0)
button_32.grid(row=6,column=1)
button_29.grid(row=6,column=2)
button_33.grid(row=6,column=3)
button_42.grid(row=6,column=4)
button_31.grid(row=6,column=5)
button_30.grid(row=6,column=6)


#row7's
button_7.grid(row=7,column=0)
button_37.grid(row=7,column=1)
button_34.grid(row=7,column=2)
button_38.grid(row=7,column=3)
button_43.grid(row=7,column=4)
button_36.grid(row=7,column=5)
button_35.grid(row=7,column=6)


root.mainloop()








