from tkinter import*

class game_x_o_(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('x_o game')
        self.config(bg='light blue')
        self.img_x =PhotoImage(file=('pac_x.png'))
        self.img_o =PhotoImage(file=('pac_o.png'))
        self.img_null =PhotoImage(file=('pcf_null.png'))
        self.img_set='x'
        self.flag1=1
        self.flg=False
        self.nkm=''
        self.nobat_v=''
        self.barande='x'
        self.v_dokme_1_1 = 'normal'
        self.v_dokme_1_2 = 'normal'
        self.v_dokme_1_3 = 'normal'
        self.v_dokme_2_1 = 'normal'
        self.v_dokme_2_2 = 'normal'
        self.v_dokme_2_3 = 'normal'
        self.v_dokme_3_1 = 'normal'
        self.v_dokme_3_2 = 'normal'
        self.v_dokme_3_3 = 'normal'
        self.menue_start('')

    
    def menue_start(self , x):
        if x == 'main' :
            self.config(bg='light blue')
            self.libel.grid_forget()
            self.btn_1.grid_forget()
            self.btn_2.grid_forget()
            self.btn_3.grid_forget()

        self.ghab_1= Frame(self , width=10 , height=5  , bg='light yellow' ) 
        self.barchasb_1= Label(self.ghab_1 , width=20 , height=4 , text='welcome to x_o game' , bg='aqua' , font=("permanent marker" , 12) )
        self.dokme_s = Button(self , width=20 , height=3 , text='start' , activebackground='green' , bg='light green' , bd= 10 , font=("permanent marker" , 12) , command=lambda:self.page_2())
        self.dokme_seting = Button(self , width=20 , height=3 , text='seting' , activebackground='purple' , bg='light pink' , bd= 10 , font=("permanent marker" , 12) , command=lambda:self.seting())
        self.dokme_e = Button(self , width=20 , height=3 , text='exit', activebackground='red', bg='orange' , font=("permanent marker" , 12) , bd= 10 , command=lambda:self.exit())

        self.ghab_1.grid(padx=10 , pady=10 , column=0 , row=0 )
        self.barchasb_1.grid(padx=10 , pady=10)
        self.dokme_s.grid(padx=50 , pady=10 , row=1 )
        self.dokme_seting.grid(padx=50 , pady=10 , row=2 )
        self.dokme_e.grid(padx=50 , pady=10 , row=3 )

    def seting(self):

        self.forget()

    def halat_ha(self):        
        
        self.pic1=self.dokme_1_1['image']
        self.pic2=self.dokme_1_2['image']
        self.pic3=self.dokme_1_3['image']
        self.pic4=self.dokme_2_1['image']
        self.pic5=self.dokme_2_2['image']
        self.pic6=self.dokme_2_3['image']
        self.pic7=self.dokme_3_1['image']
        self.pic8=self.dokme_3_2['image']
        self.pic9=self.dokme_3_3['image']
        if self.img_set == 'o':
            self.nobat_v='pyimage2'
            self.barande='o'
        
        if self.img_set == 'x':
            self.nobat_v='pyimage1'
            self.barande='x'

        if self.pic1 == self.nobat_v and self.pic2 == self.nobat_v and self.pic3 == self.nobat_v:

            print(f'barande :{self.barande}')
            self.page_bord()

        if self.pic4 == self.nobat_v and self.pic5 == self.nobat_v and self.pic6 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()

        if self.pic7 == self.nobat_v and self.pic8 == self.nobat_v and self.pic9 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()


        if self.pic1 == self.nobat_v and self.pic4 == self.nobat_v and self.pic7 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()

        if self.pic2 == self.nobat_v and self.pic5 == self.nobat_v and self.pic8 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()

        if self.pic3 == self.nobat_v and self.pic6 == self.nobat_v and self.pic9 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()

        if self.pic1 == self.nobat_v and self.pic5 == self.nobat_v and self.pic9 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()

        if self.pic3 == self.nobat_v and self.pic5 == self.nobat_v and self.pic7 == self.nobat_v:
            print(f'barande :{self.barande}')
            self.page_bord()

    def page_bord(self):
        self.ghab_x.grid_forget()
        self.ghab_o.grid_forget()
        self.barchasb_x.grid_forget()
        self.barchasb_o.grid_forget()
        self.dokme_d.grid_forget()
        self.dokme_1_1.grid_forget()
        self.dokme_1_2.grid_forget()
        self.dokme_1_3.grid_forget()
        self.dokme_2_1.grid_forget()
        self.dokme_2_2.grid_forget()
        self.dokme_2_3.grid_forget()
        self.dokme_3_1.grid_forget()
        self.dokme_3_2.grid_forget()
        self.dokme_3_3.grid_forget()
        self.config(bg='cornflower blue')

        self.libel_1 = Label(self , width=20 , height=4 , text=f'{self.barande} barande shod' , font=("permanent marker" , 12) , bg='gold' , bd=1 )
        self.libel_1.grid( padx = 10 ,pady = 10 , row=0 , column=1)

        self.btn_1 = Button(self , width=12 , height = 5 , text='Retry' , bg='cyan' , activebackground='blue' , font=("permanent marker" , 12) , bd=4 , command=lambda:self.play())
        self.btn_1.grid( padx = 5 ,pady = 10 , row=1 , column=0)

        self.btn_2 = Button(self , width=12 , height = 5 , text='Exit' , bg='purple' , activebackground='DarkSlateBlue' , font=("permanent marker" , 12) , bd=4 , command=lambda:self.exit())
        self.btn_2.grid( padx = 5 ,pady = 10 , row=1 , column=2)

        self.btn_3 = Button(self , width=12 , height = 5 , text='Main menue' , bg='light green' , activebackground='green' , font=("permanent marker" , 12 ) , bd=4 , command=lambda:self.menue_start('main') ) 
        self.btn_3.grid( padx = 5 ,pady = 10 , row=1 , column=1)

    def forget(self):
        self.ghab_1.grid_forget()
        self.barchasb_1.grid_forget()
        self.dokme_seting.grid_forget()
        self.dokme_s.grid_forget()
        self.dokme_e.grid_forget()

    def nobat(self):
        if self.img_set == 'x':
            self.img_set='o'
            self.ghab_x.config(bg='gray')
            self.ghab_o.config(bg='purple')

        elif self.img_set == 'o':
            self.img_set='x'
            self.ghab_o.config(bg='gray')
            self.ghab_x.config(bg='purple')


    def done(self):
        self.halat_ha()

        if self.nkm == 'dokme_1_1':
            self.nkm=''
            self.v_dokme_1_1 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_1_2':
            self.nkm=''
            self.v_dokme_1_2 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_1_3':
            self.nkm=''
            self.v_dokme_1_3 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_2_1':
            self.nkm=''
            self.v_dokme_2_1 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_2_2':
            self.nkm=''
            self.nkm=''
            self.v_dokme_2_2 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_2_3':
            self.nkm=''
            self.v_dokme_2_3 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_3_1':
            self.nkm=''
            self.v_dokme_3_1 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_3_2':
            self.nkm=''
            self.v_dokme_3_2 = 'disabled'
            self.nobat()

        if self.nkm == 'dokme_3_3':
            self.nkm=''
            self.v_dokme_3_3 = 'disabled'
            self.nobat()



    def page_2(self):
        self.forget()
        self.dokme_play = Button(self , width=20 , height=3 , text='play', activebackground='yellow', bg='lime' , font=("permanent marker" , 12) , bd= 10 , command=lambda:self.play())
        self.dokme_play.grid( row=1 , column=1)

    
    def play(self):
       
        self.dokme_play.grid_forget()
        self.craete_objects1()

    def exit(self):
        self.destroy()


    def craete_objects1(self):

        self.geometry('800x500')

        self.ghab_x= Frame(self , width=150 , height=150  , bg='purple' )   
        self.ghab_o= Frame(self , width=150 , height=150  , bg='gray' )   

        self.barchasb_x= Label(self.ghab_x , width=120 , height=120 , image=self.img_x , font=10 )
        self.barchasb_o= Label(self.ghab_o , width=120 , height=120 , image=self.img_o , bg='gray' , font=10 )

        self.dokme_d = Button( self , width=20 ,height=4 , bg='light green' , text='Done' , font=("permanent marker" , 15), command=lambda:self.done())
        
        self.dokme_1_1 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_1_1'))
        self.dokme_1_2 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_1_2'))
        self.dokme_1_3 = Button( self , width=130 ,height=130  , image=self.img_null  , command=lambda:self.dokme_cod('dokme_1_3'))

        self.dokme_2_1 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_2_1'))
        self.dokme_2_2 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_2_2'))
        self.dokme_2_3 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_2_3'))

        self.dokme_3_1 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_3_1'))
        self.dokme_3_2 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_3_2'))
        self.dokme_3_3 = Button( self , width=130 ,height=130 , image=self.img_null  , command=lambda:self.dokme_cod('dokme_3_3'))

        self.ghab_x.grid(padx=10 , pady=10 , column=3 , row=0)
        self.ghab_o.grid(padx=10 , pady=10 , column=4 , row=0)

        self.barchasb_x.grid(padx=10 , pady=10)
        self.barchasb_o.grid(padx=10 , pady=10)

        self.dokme_d.grid(padx=10 , pady=10 , column=3 , columnspan=2 , row=2)

        self.dokme_1_1.grid(padx=10 , pady=10 , column=0 , row=0)
        self.dokme_1_2.grid(padx=10 , pady=10 , column=1 , row=0 )
        self.dokme_1_3.grid(padx=10 , pady=10 , column=2 , row=0 )

        self.dokme_2_1.grid(padx=10 , pady=10 , column=0 , row=1 )
        self.dokme_2_2.grid(padx=10 , pady=10 , column=1 , row=1 )  
        self.dokme_2_3.grid(padx=10 , pady=10 , column=2 , row=1 )

        self.dokme_3_1.grid(padx=10 , pady=10 , column=0 , row=2 )
        self.dokme_3_2.grid(padx=10 , pady=10 , column=1 , row=2 )
        self.dokme_3_3.grid(padx=10 , pady=10 , column=2 , row=2 )


    def dokme_cod(self,x):
        

        self.pic1=self.dokme_1_1['image']
        self.pic2=self.dokme_1_2['image']
        self.pic3=self.dokme_1_3['image']
        self.pic4=self.dokme_2_1['image']
        self.pic5=self.dokme_2_2['image']
        self.pic6=self.dokme_2_3['image']
        self.pic7=self.dokme_3_1['image']
        self.pic8=self.dokme_3_2['image']
        self.pic9=self.dokme_3_3['image']


        if x == 'dokme_1_1' and self.v_dokme_1_1 == 'normal':


            if self.pic1 == 'pyimage1' or self.pic1 == 'pyimage2':
                self.dokme_1_1.config(image= self.img_null)

            if self.pic1 == 'pyimage3':

                self.nkm='dokme_1_1'

                if self.img_set == 'x' :
                    self.dokme_1_1.config(image= self.img_x)

                    
                if self.img_set == 'o' :
                    self.dokme_1_1.config(image= self.img_o)

                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass
                

        if x == 'dokme_1_2' and self.v_dokme_1_2 == 'normal':

            if self.pic2 == 'pyimage1' or self.pic2 == 'pyimage2':
                self.dokme_1_2.config(image= self.img_null)
                self.flag1+=1

            if self.pic2 == 'pyimage3':
                self.nkm='dokme_1_2'

                if self.img_set == 'x' :
                    self.dokme_1_2.config(image= self.img_x)
                    
                if self.img_set == 'o' :
                    self.dokme_1_2.config(image= self.img_o)
                                

                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass

        if x == 'dokme_1_3' and self.v_dokme_1_3 == 'normal':

            if self.pic3 == 'pyimage1' or self.pic3 == 'pyimage2':
                self.dokme_1_3.config(image= self.img_null)
                self.flag1+=1

            if self.pic3 == 'pyimage3':
                self.nkm='dokme_1_3'

                if self.img_set == 'x' :
                    self.dokme_1_3.config(image= self.img_x)
                if self.img_set == 'o' :
                    self.dokme_1_3.config(image= self.img_o)
                    
                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass
        


        if x == 'dokme_2_1' and self.v_dokme_2_1 == 'normal':

            if self.pic4 == 'pyimage1' or self.pic4 == 'pyimage2':
                self.dokme_2_1.config(image= self.img_null)
                self.flag1+=1

            if self.pic4 == 'pyimage3':
                self.nkm='dokme_2_1'

                if self.img_set == 'x' :
                    self.dokme_2_1.config(image= self.img_x)
                if self.img_set == 'o' :
                    self.dokme_2_1.config(image= self.img_o)
                
                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass
                
                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass
        
            
        
        if x == 'dokme_2_2' and self.v_dokme_2_2 == 'normal':

            if self.pic5 == 'pyimage1' or self.pic5 == 'pyimage2':
                self.dokme_2_2.config(image= self.img_null)
                self.flag1+=1

            if self.pic5 == 'pyimage3':
                self.nkm='dokme_2_2'

                if self.img_set == 'x' :
                    self.dokme_2_2.config(image= self.img_x)

                if self.img_set == 'o' :
                    self.dokme_2_2.config(image= self.img_o)

                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass  
                             
                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass
                
                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass

        if x == 'dokme_2_3' and self.v_dokme_2_3 == 'normal':

            if self.pic6 == 'pyimage1' or self.pic6 == 'pyimage2':
                self.dokme_2_3.config(image= self.img_null)
                self.flag1+=1

            if self.pic6 == 'pyimage3':
                self.nkm='dokme_2_3'
                if self.img_set == 'x' :
                    self.dokme_2_3.config(image= self.img_x)

                if self.img_set == 'o' :
                    self.dokme_2_3.config(image= self.img_o)
                    

                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass  
                             
                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass
                
                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass

        if x == 'dokme_3_1' and self.v_dokme_3_1 == 'normal':

            if self.pic7 == 'pyimage1' or self.pic7 == 'pyimage2':
                self.dokme_3_1.config(image= self.img_null)
                self.flag1+=1

            if self.pic7 == 'pyimage3':
                self.nkm='dokme_3_1'

                if self.img_set == 'x' :
                    self.dokme_3_1.config(image= self.img_x)
                if self.img_set == 'o' :
                    self.dokme_3_1.config(image= self.img_o)
                    
                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass  
                             
                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass
                
                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass

        if x == 'dokme_3_2' and self.v_dokme_3_2 == 'normal':

            if self.pic8 == 'pyimage1' or self.pic8 == 'pyimage2':
                self.dokme_3_2.config(image= self.img_null)
                self.flag1+=1

            if self.pic8 == 'pyimage3':
                self.nkm='dokme_3_2'

                if self.img_set == 'x' :
                    self.dokme_3_2.config(image= self.img_x)
                if self.img_set == 'o' :
                    self.dokme_3_2.config(image= self.img_o)
                
                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass  
                             
                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass
                
                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_3 == 'normal':
                    self.dokme_3_3.config(image= self.img_null)
                else:
                    pass


        if x == 'dokme_3_3' and self.v_dokme_3_3 == 'normal':

            
            if  self.pic9 == 'pyimage1' or self.pic9 == 'pyimage2':
                self.dokme_3_3.config(image= self.img_null)
                self.flag1+=1

            if self.pic9 == 'pyimage3':
                self.nkm='dokme_3_3'

                if self.img_set == 'x' :
                    self.dokme_3_3.config(image= self.img_x)
                if self.img_set == 'o' :
                    self.dokme_3_3.config(image= self.img_o)
                
                if self.v_dokme_1_1 == 'normal':
                    self.dokme_1_1.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_2 == 'normal':
                    self.dokme_1_2.config(image= self.img_null)
                else:
                    pass  
                         
                if self.v_dokme_1_3 == 'normal':
                    self.dokme_1_3.config(image= self.img_null)
                else:
                    pass  
                             
                if self.v_dokme_2_1 == 'normal':
                    self.dokme_2_1.config(image= self.img_null)
                else:
                    pass
                
                if self.v_dokme_2_2 == 'normal':
                    self.dokme_2_2.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_2_3 == 'normal':
                    self.dokme_2_3.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_1 == 'normal':
                    self.dokme_3_1.config(image= self.img_null)
                else:
                    pass

                if self.v_dokme_3_2 == 'normal':
                    self.dokme_3_2.config(image= self.img_null)
                else:
                    pass




d= game_x_o_()        
d.mainloop()