
import sys
import tkinter as tk
import tkinter.ttk as ttk
import interface_support
from tkinter.constants import DISABLED

sys.path.insert(1,"../donnees")
import bagOfWord
import sql
import modele
import donnees
from donnees import question



def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    interface_support.set_Tk_var()
    top = Toplevel1 (root)
    interface_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    interface_support.set_Tk_var()
    top = Toplevel1 (w)
    interface_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def buttonAdd(self):
        CQ=donnees.question(self.id_entry.get(),self.tdd_cb.get(),self.tq_cb.get(),self.sn_entry.get(),self.question_text.get("1.0",'end-1c'),self.anwser_cb.get(),None,0)
        foo = []
        foo = self.newquestion_cb["values"] 
        if(foo!='' and self.question_text.get("1.0",'end-1c') not in foo):
            for k in foo:
                laq=donnees.findQ(self.newquestion_cb.get())
                modele.update_pertinance_rejete(CQ,laq)
                print("b")
        
        self.question_list.insert(0,self.question_text.get("1.0",'end-1c'))
        self.id_entry['state']='normal'
        self.id_entry.delete(0, 'end')
        self.id_entry.insert(0,cmp+1)
        self.id_entry['state']=DISABLED
        self.sn_entry.delete(0, 'end')
        self.question_text.delete("1.0",'end-1c')
        self.tdd_cb.delete(0, 'end')
        self.tq_cb.delete(0, 'end')
        self.add_btn['state']=DISABLED
        self.find_btn['state']=DISABLED
        self.newquestion_cb.set('')
        self.anwser_cb.current(0)
        self.tdd_cb.current(0)
        self.tq_cb.current(0)
        foo = []
        self.newquestion_cb["values"] = foo
        self.newquestion_cb.set('')
        self.replace_btn['state']= DISABLED
        self.next_btn['state']= DISABLED

    def onselect(self,event):
        print("e")
        self.use_btn['state']='active'

    def buttonUse(self):
        laq=donnees.findQ(self.waiting_list.get(self.waiting_list.curselection()))
        self.question_text.insert("1.0",laq.text)
        self.sn_entry.insert(0, laq.shortName)
        self.tdd_cb.set(laq.typeOfDD)
        self.tq_cb.set(laq.categorie)
        self.anwser_cb.set(laq.typeOfAnswer)
        self.newquestion_cb.set('')
        self.waiting_list.delete(self.waiting_list.curselection())
        self.use_btn['state']=DISABLED


    def buttonFind(self):
        CQ=donnees.question(self.id_entry.get(),self.tdd_cb.get(),self.tq_cb.get(),self.sn_entry.get(),self.question_text.get("1.0",'end-1c'),self.anwser_cb.get(),None,0)
        LP=modele.get_liste_pertinance(CQ)
        foo = []
        for k in range(4):
            foo.append(LP[k][0].text)
        self.newquestion_cb["values"] = foo

    def buttonReplace(self):
        foo = []
        foo = self.newquestion_cb["values"] 
        CQ=donnees.question(self.id_entry.get(),self.tdd_cb.get(),self.tq_cb.get(),self.sn_entry.get(),self.question_text.get("1.0",'end-1c'),self.anwser_cb.get(),None,0)
        for k in foo:
            laq=donnees.findQ(self.newquestion_cb.get())
            if k == self.newquestion_cb.get():
                modele.update_pertinance_choisi(CQ,laq)
                print("a")
            else:
                modele.update_pertinance_rejete(CQ,laq)
                print("b")
        self.id_entry['state']='normal'
        self.id_entry.delete(0, 'end')
        self.id_entry.insert(0,cmp+1)
        self.id_entry['state']=DISABLED
        self.sn_entry.delete(0, 'end')
        self.question_text.delete("1.0",'end-1c')
        self.question_text.insert("1.0",self.newquestion_cb.get())
        laq=donnees.findQ(self.newquestion_cb.get())
        self.sn_entry.insert(0, laq.shortName)
        self.tdd_cb.set(laq.typeOfDD)
        self.tq_cb.set(laq.categorie)
        self.anwser_cb.set(laq.typeOfAnswer)
        foo = []
        self.newquestion_cb["values"] = foo
        self.newquestion_cb.set('')
        self.replace_btn['state']= DISABLED
        self.next_btn['state']= DISABLED

    def buttonAddAsNext(self):
        foo = []
        foo = self.newquestion_cb["values"] 
        CQ=donnees.question(self.id_entry.get(),self.tdd_cb.get(),self.tq_cb.get(),self.sn_entry.get(),self.question_text.get("1.0",'end-1c'),self.anwser_cb.get(),None,0)
        for k in foo:
            laq=donnees.findQ(self.newquestion_cb.get())
            if k == self.newquestion_cb.get():
                modele.update_pertinance_waiting_list(laq)
        self.waiting_list.insert(0,self.newquestion_cb.get())
        self.id_entry['state']='normal'
        self.id_entry.delete(0, 'end')
        self.id_entry.insert(0,cmp+1)
        self.id_entry['state']=DISABLED
        self.sn_entry.delete(0, 'end')
        self.question_text.delete("1.0",'end-1c')
        foo = []
        self.newquestion_cb["values"] = foo
        self.newquestion_cb.set('')
        self.replace_btn['state']= DISABLED
        self.next_btn['state']= DISABLED


    def callback(self,event):

        if (self.sn_entry.get()!='' and self.question_text.get("1.0",'end-1c')!=''  ):
            self.add_btn['state']='active'
            self.find_btn['state']='active'
        else:
            self.add_btn['state']=DISABLED
            self.find_btn['state']=DISABLED


        if (len(self.newquestion_cb.get()) != 0):
            self.replace_btn['state']= 'active'
            self.next_btn['state']= 'active'
        else:
            self.replace_btn['state']= DISABLED
            self.next_btn['state']= DISABLED




    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("936x588+515+244")
        top.minsize(1080, 720)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Good Questions")
        top.configure(background="#d9d9d9")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.280, rely=0.085, relheight=0.689
                , relwidth=0.4)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Questions''')
        self.Labelframe1.configure(background="#d9d9d9")

        self.id_entry = tk.Entry(self.Labelframe1)
        self.id_entry.place(relx=0.091, rely=0.222, height=20, relwidth=0.153
                , bordermode='ignore')
        self.id_entry.configure(background="white")
        self.id_entry.configure(disabledforeground="#a3a3a3")
        self.id_entry.configure(font="TkFixedFont")
        self.id_entry.configure(foreground="#000000")
        self.id_entry.configure(insertbackground="black")
        global cmp
        cmp=1
        self.id_entry.insert(0,cmp);
        self.id_entry['state']=DISABLED

        self.tq_cb = ttk.Combobox(self.Labelframe1,state="readonly")
        self.tq_cb.place(relx=0.091, rely=0.42, height=20, relwidth=0.207
                , bordermode='ignore')
        self.tq_cb.configure(textvariable=interface_support.combobox4)
        self.tq_cb["values"]=['AML/KYC','Asset Management','BCP/DRP','Compliance','Custody','Distribution','Employee','Fund Administration','General Information','Generic/Technical','Governance, Risk and Compliance','Internal audit and control','IT & Business Continuity','Know Your Counterparty','Licence/Authorisation/Regulator','Management  & Ownership','MIFID II','Outsourcing','Policy & Procedure','Regulatory','Regulatory Status','Risk','Tax Information','Transfer Agent']
        self.tq_cb.current(0)
        self.tq_cb.configure(takefocus="")
        self.tq_cb.configure(cursor="fleur")

        self.tdd_cb = ttk.Combobox(self.Labelframe1,state="readonly")
        self.tdd_cb.place(relx=0.364, rely=0.222, height=20, relwidth=0.262
                , bordermode='ignore')
        self.tdd_cb.configure(textvariable=interface_support.combobox3)
        self.tdd_cb["values"]=['Common','Depositary Bank','Distribution','Fund Administration','Investment Management','Transfer Agent']
        self.tdd_cb.current(0)
        self.tdd_cb.configure(takefocus="")
        self.tdd_cb.configure(cursor="fleur")

        self.sn_entry = tk.Entry(self.Labelframe1)
        self.sn_entry.place(relx=0.364, rely=0.42, height=20, relwidth=0.553
                , bordermode='ignore')
        self.sn_entry.configure(background="white")
        self.sn_entry.configure(disabledforeground="#a3a3a3")
        self.sn_entry.configure(font="TkFixedFont")
        self.sn_entry.configure(foreground="#000000")
        self.sn_entry.configure(insertbackground="black")
        self.sn_entry.bind('<KeyRelease>',self.callback)


        self.question_text = tk.Text(self.Labelframe1)
        self.question_text.place(relx=0.091, rely=0.593, relheight=0.281
                   , relwidth=0.825, bordermode='ignore')
        self.question_text.configure(background="white")
        self.question_text.configure(font="TkTextFont")
        self.question_text.configure(foreground="black")
        self.question_text.configure(highlightbackground="#d9d9d9")
        self.question_text.configure(highlightcolor="black")
        self.question_text.configure(insertbackground="black")
        self.question_text.configure(selectbackground="#c4c4c4")
        self.question_text.configure(selectforeground="black")
        self.question_text.configure(wrap="word")
        self.question_text.bind('<KeyRelease>', self.callback)

        self.Label1 = tk.Label(self.Labelframe1)
        self.Label1.place(relx=0.091, rely=0.148, height=21, width=58
                , bordermode='ignore')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Unique ID''')


        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.364, rely=0.148, height=21, width=124
                , bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Type of Due Dulligence''')

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.091, rely=0.346, height=21, width=94
                , bordermode='ignore')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Type of question''')

        self.Label4 = tk.Label(self.Labelframe1)
        self.Label4.place(relx=0.364, rely=0.346, height=21, width=67
                , bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Short name''')

        self.anwser_cb = ttk.Combobox(self.Labelframe1,state="readonly")
        self.anwser_cb.place(relx=0.673, rely=0.222, relheight=0.052
                , relwidth=0.242, bordermode='ignore')
        self.anwser_cb.configure(textvariable=interface_support.combobox)
        self.anwser_cb["values"]=['Boolean','Rich Text','Attachment','GPS Position','Radio Button','Rich Text with Attachment']
        self.anwser_cb.current(0)
        self.anwser_cb.configure(takefocus="")
        self.anwser_cb.configure(cursor="fleur")

        self.newquestion_cb = ttk.Combobox(top,state="readonly")
        self.newquestion_cb.place(relx=0.203, rely=0.867, relheight=0.036
                , relwidth=0.601)
        self.newquestion_cb.configure(textvariable=interface_support.combobox2)
        self.newquestion_cb.configure(takefocus="")
        self.newquestion_cb.bind("<<ComboboxSelected>>",self.callback)
        self.Label5 = tk.Label(self.Labelframe1)
        self.Label5.place(relx=0.655, rely=0.148, height=21, width=94
                , bordermode='ignore')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Type of anwser''')

        self.Label6 = tk.Label(self.Labelframe1)
        self.Label6.place(relx=0.091, rely=0.519, height=21, width=74
                , bordermode='ignore')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Question text''')

        self.add_btn = tk.Button(self.Labelframe1,command=self.buttonAdd)
        self.add_btn.place(relx=0.436, rely=0.914, height=24, width=82
                , bordermode='ignore')
        self.add_btn.configure(activebackground="#ececec")
        self.add_btn.configure(activeforeground="#000000")
        self.add_btn.configure(background="#d9d9d9")
        self.add_btn.configure(disabledforeground="#a3a3a3")
        self.add_btn.configure(foreground="#000000")
        self.add_btn.configure(highlightbackground="#d9d9d9")
        self.add_btn.configure(highlightcolor="black")
        self.add_btn.configure(pady="0")
        self.add_btn.configure(text='''Add question''')
        self.add_btn['state']=DISABLED



        self.find_btn = tk.Button(self.Labelframe1,command=self.buttonFind)
        self.find_btn.place(relx=0.800, rely=0.914, height=24, width=82
                , bordermode='ignore')
        self.find_btn.configure(activebackground="#ececec")
        self.find_btn.configure(activeforeground="#000000")
        self.find_btn.configure(background="#d9d9d9")
        self.find_btn.configure(disabledforeground="#a3a3a3")
        self.find_btn.configure(foreground="#000000")
        self.find_btn.configure(highlightbackground="#d9d9d9")
        self.find_btn.configure(highlightcolor="black")
        self.find_btn.configure(pady="0")
        self.find_btn.configure(text='''Find''')
        self.find_btn['state']=DISABLED

        self.waiting_list = tk.Listbox(top)
        self.waiting_list.place(relx=0.015, rely=0.153, relheight=0.531
                , relwidth=0.25)
        self.waiting_list.configure(background="white")
        self.waiting_list.configure(disabledforeground="#a3a3a3")
        self.waiting_list.configure(font="TkFixedFont")
        self.waiting_list.configure(foreground="#000000")
        self.waiting_list.bind('<<ListboxSelect>>', self.onselect)

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.110, rely=0.102, height=21, width=108)
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Waiting List''')

        self.question_list = tk.Listbox(top)
        self.question_list.place(relx=0.700, rely=0.153, relheight=0.531
                , relwidth=0.28)
        self.question_list.configure(background="white")
        self.question_list.configure(disabledforeground="#a3a3a3")
        self.question_list.configure(font="TkFixedFont")
        self.question_list.configure(foreground="#000000")

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.825, rely=0.102, height=21, width=114)
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Questions List''')


        self.replace_btn = tk.Button(top,command=self.buttonReplace)
        self.replace_btn.place(relx=0.30, rely=0.799, height=24, width=93)
        self.replace_btn.configure(activebackground="#ececec")
        self.replace_btn.configure(activeforeground="#000000")
        self.replace_btn.configure(background="#d9d9d9")
        self.replace_btn.configure(disabledforeground="#a3a3a3")
        self.replace_btn.configure(foreground="#000000")
        self.replace_btn.configure(highlightbackground="#d9d9d9")
        self.replace_btn.configure(highlightcolor="black")
        self.replace_btn.configure(pady="0")
        self.replace_btn.configure(text='''Replace current''')
        self.replace_btn['state'] = DISABLED

        self.next_btn = tk.Button(top,command=self.buttonAddAsNext)
        self.next_btn.place(relx=0.459, rely=0.799, height=24, width=110)
        self.next_btn.configure(activebackground="#ececec")
        self.next_btn.configure(activeforeground="#000000")
        self.next_btn.configure(background="#d9d9d9")
        self.next_btn.configure(disabledforeground="#a3a3a3")
        self.next_btn.configure(foreground="#000000")
        self.next_btn.configure(highlightbackground="#d9d9d9")
        self.next_btn.configure(highlightcolor="black")
        self.next_btn.configure(pady="0")
        self.next_btn.configure(text='''Add to waiting list''')
        self.next_btn['state'] = DISABLED

        self.nosuggest_btn = tk.Button(top)
        self.nosuggest_btn.place(relx=0.610, rely=0.799, height=24, width=123)
        self.nosuggest_btn.configure(activebackground="#ececec")
        self.nosuggest_btn.configure(activeforeground="#000000")
        self.nosuggest_btn.configure(background="#d9d9d9")
        self.nosuggest_btn.configure(disabledforeground="#a3a3a3")
        self.nosuggest_btn.configure(foreground="#000000")
        self.nosuggest_btn.configure(highlightbackground="#d9d9d9")
        self.nosuggest_btn.configure(highlightcolor="black")
        self.nosuggest_btn.configure(pady="0")
        self.nosuggest_btn.configure(text='''Do not suggest again''')

        self.use_btn = tk.Button(top,command=self.buttonUse)
        self.use_btn.place(relx=0.120, rely=0.700, height=24, width=90)
        self.use_btn.configure(activebackground="#ececec")
        self.use_btn.configure(activeforeground="#000000")
        self.use_btn.configure(background="#d9d9d9")
        self.use_btn.configure(disabledforeground="#a3a3a3")
        self.use_btn.configure(foreground="#000000")
        self.use_btn.configure(highlightbackground="#d9d9d9")
        self.use_btn.configure(highlightcolor="black")
        self.use_btn.configure(pady="0")
        self.use_btn.configure(text='''Use''')
        self.use_btn['state']=DISABLED


if __name__ == '__main__':
    vp_start_gui()
    conn=sql.getConnection()
