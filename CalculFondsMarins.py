from MainVitalité import VerifyVita
import time
from Macro1 import MacroReset
import re
from Macro1 import * 
from ScreenFondsMarins import screenValuesFondsMarins

def UpStats():
  def getValue(doc):
    f=open(doc, "r") 
    content = f.read()
    content = re.sub("[^0-9]","", content)
    if content == '' :
      content = 0
      return int(content)
    else :
      return int(content)

  def getValue2(doc) :
    f=open(doc , "r") 
    content = f.read()
    if(content == 'A Esquive PM\n\x0c'):
        X == 0
    else : 
        X == 1


    if content == 'A Esquive PM\n\x0c' :
      content = 4
      return int(content)
    if content == '1 Esquive PM\n\x0c' :
      content = 1
      return int(content)
    if content == '2 Esquive PM\n\x0c' :
      content = 2
      return int(content)
    if content == '3 Esquive PM\n\x0c' :
      content = 3
      return int(content)
    if content == 'Esquive PM\n\x0c' :
      content = 0
    if content == '5 Esquive PM\n\x0c' :
      content = 5
      return int(content)
    if content == '\x0c' :
      content = 0
      return int(content)
    else :
      return int(content)
  A1 = 239
  B1 = 55
  C1 = 40
  D1 = 2
  E1 = 0
  F1 = 10
  G1 = 9
  H1 = 6
  I1 = 3

  X = 2
  J = getValue("data9.txt")

  A = getValue("data0.txt")
  B = getValue("data1.txt")
  C = getValue("data2.txt")
  D = getValue("data3.txt")
  E = getValue("data4.txt")
  F = getValue("data5.txt")
  G = getValue("data6.txt")
  H = getValue("data7.txt")
  I = getValue2("data8.txt")
  if X == 0:
      I == 4
  else : 
    if X == 1 :
        I =getValue("data8.txt")
  print (A, B, C, D, E, G, H , I ,J)
  
  if not (I > 1) and (A < 251 and B < 61): 
      selectRune(1070,680) # Esquiv
      return False
  else: 
    if not E > E1 and (A < 251 and B < 61) :
        selectRune(1009,520) #Po
        return False
    else : 
        if not H > 6 and ( A < 251 and B < 61):
            selectRune(1070,640) #PaTac
            return False
        else : 
            if not C > 30 and (A < 251 and B < 61) :
                selectRune(1120,440) #RaSa
                return False
            else : 
                if not B > 39 and (A < 251) :
                    selectRune(1120,400) #RaCha
                    return False
                else : 
                    if not F > 7 and (A < 251 and B < 61) :
                        selectRune(1070,560) #PaDoEau
                        return False
                    else : 
                        if not G > 6 and  (A < 251 and B < 61) :
                            selectRune(1008,600) #RePerFeu
                            return False
                        else : 
                            if not D > 1 and (A < 251 and B < 61) :
                                selectRune(1008,480) #Crit
                                return False
                            else : 
                                if not A > 184 and (B < 61) :
                                    selectRune(1120,360) #RaVi
                                    return False
                                else : 
                                    #Fin étape 1
                                    if not I > I1 and (A < 251 and B < 61) :
                                        if I <6 :
                                            selectRune(1008,680) #EsquivPme
                                        if I > 5 : 
                                            selectRune(1015, 1030)
                                        return False
                                    else : 
                                        if not H > H1 and (A < 251 and B < 61) : 
                                            if H < 11 :
                                                selectRune(1008,640) #Tac
                                            if H > 10 :
                                                selectRune(1015, 1030)
                                            return False
                                        else : 
                                            if not C > C1 and (A < 251 and B < 61) : 
                                                selectRune(1070,440) #PaSa
                                                return False
                                            else : 
                                                if not (B > B1 and B < 61) and (A < 251):
                                                    if B < 52 : 
                                                        selectRune(1120,400) #RaCha
                                                    if (B > 51 and B < 56) :
                                                        selectRune(1070,400) #PaCha
                                                    if B > 60 : 
                                                        selectRune(1015, 1030)
                                                    return False
                                                else : 
                                                    if not F > F1 and (A < 251 and B  < 61):
                                                        if F == 8 :
                                                            selectRune(1070,560)  #PaDoEau
                                                        if F > 8 : 
                                                            selectRune(1008,560) #DoEau
                                                        return False
                                                    else : 
                                                        if not G > G1 and (A < 251 and B < 61) :
                                                            if G < 11 :
                                                                selectRune(1008,600) #RePerFeu
                                                            if G > 10 :
                                                                selectRune(1015, 1030)
                                                            return False 
                                                        else : 
                                                            if not D > D1 and (A < 251 and B < 61) :
                                                                selectRune(1008,480) #Crit
                                                                return False
                                                            else : 
                                                                if not (A > A1 and A < 251) and (B < 61) : 
                                                                    if (A > 184 and A < 190) or  (A > 205 and A < 240):
                                                                        selectRune(1070,360) #PaVi
                                                                    if (A > 189 and A < 206) :
                                                                        selectRune(1120,360) #RaVi
                                                                    if (A > 250) :
                                                                        selectRune(1015,1030)
                                                                    return False
                                                                else : 
                                                                    
                                                        
                    
  
                                                                    if (A > A1 and A < 251) and (B > B1 and B < 61) and (C > C1 and C < 51) and (D > D1) and (E > E1 ) and (F > F1) and (G > G1 and G < 11) and (H > H1 and H < 11)  and (I > I1 and I < 6): 
                                                                        if J != 0: 
                                                                            selectRune(1187, 1030) 
                                                                            screenValuesFondsMarins()
                                                                            J = getValue("data9.txt")
                                                                            print(J)
                                                                            time.sleep(0.1)
                                                                            if J != 0 : 
                                                                                OtherD()
                                                                        else:
                                                                            selectRune(1147, 1030) 
                                                                            time.sleep(0.1)
                                                                            MacroReset()
                                                                            screenValuesFondsMarins()
                                                                            time.sleep(0.3)
                                                                            J = getValue("data9.txt")
                                                                            time.sleep(0.1)
                                                                            if  J != 0 : 
                                                                                OtherD()
                                                                            else : 
                                                                                return False
                                                                            time.sleep(0.1)
                                                                            print(A, B, C, D, E, F, G, H, I, J)