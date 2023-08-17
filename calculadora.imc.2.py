from tkinter import * 

cor1= '#ff8533'#cor do fundo Janela
cor2= '#262626'#cor da fonte Principal(Letra)
cor3= '#a6a6a6'#cor do fundo Principal (Fundo)
cor4='#000099'#cor do fundo segundaria(letra)
cor5='#001a00'#cor do fundo terceiro plano(Letra)
cor6='#737373'#cor do fundo Segundario (Fundo)
cor7='#cccccc'#cor do fundo terceiro plano(Fundo)

janela= Tk ()
janela.title("janela de começo")
janela.geometry ('400x250')
janela.config(bg=cor1)
janela.resizable (width=True,height=True)


  
  
def text_imc ():

    peso=float(entry_peso_2.get())
    altura=float(entry_altura_2.get())
    calculo_imc = peso/altura**2
    
    IMC=calculo_imc
   
    if IMC <= 18.5:
      label_imc_1['text']="Baixo peso"
    elif 18.5 < IMC <=24.9:
       label_imc_1['text']="Peso normal"
    elif 24.9 < IMC <=29.9:
      label_imc_1['text']="Sobrepeso" 
    elif 29.9 < IMC <=34.9:
        label_imc_1['text']="Obsidade Grau 1" 
    elif 34.9< IMC <=39.9:
       label_imc_1['text']="Obsidade Grau 2" 
    else: 
       label_imc_1['text']="Obsidade mórbida" 

      
      
  

#titulo---------------------------------------------------------------------------------------------------
label_titulo_1= Label(janela, width=25,height=1,text='Calculadora de IMC',font='arial 11 ',fg=cor2,bg=cor1,)
label_titulo_1.grid(row=0,column=1,pady=2,padx=2,sticky=NSEW)
 


#Identificação das Entradas------------------------------------------------------------------------------
label_peso_1= Label(janela, width=6,height=3,text='Peso:',font='arial 10 ',fg=cor4,bg=cor1,)
label_peso_1.grid(row=1,column=0,pady=2,padx=2,sticky=NSEW)

label_altura_1= Label(janela, width=6,height=3,text='Altura:',font='arial 10 ',fg=cor4, bg=cor1,)
label_altura_1.grid(row=2,column=0,pady=2,padx=2,sticky=NSEW)



#Calculo de IMC-----------------------------------------------------------------------------------------------
label_imc_1= Label(janela, width=6,height=2,text='',font='arial 12 ',fg=cor5, bg=cor1)
label_imc_1.grid(row=3,column=1,pady=2,padx=0,sticky=NSEW)

label_imc_2= Label(janela, width=6,height=3,text='',font='arial 12 ',fg=cor5,bg=cor1)
label_imc_2.grid(row=3,column=2,pady=2,padx=2,sticky=NSEW)



#Entradas para o usuario--------------------------------------------------------------------------------------
entry_peso_2= Entry(janela, width=16,font='arial 10 ',fg=cor5,)
entry_peso_2.grid(row=1,column=1,pady=2,padx=0)

entry_altura_2= Entry(janela, width=16,font='arial 10 ',fg=cor5,)
entry_altura_2.grid(row=2,column=1,pady=2,padx=0)

#Botão---------------------------------------------------------------------------------------------------------
botao_1= Button (janela,command=text_imc, width=6,height=2,text='Calcular',font='arial 10 ', relief='raised',fg=cor2, bg=cor6)
botao_1.grid(row=3,column=0,pady=2,padx=0)






janela.mainloop ()