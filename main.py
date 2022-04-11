import One_script_1_stat as stat
import Two_script_2_ev as ev


def main(): 
     
    print ("Choose an Option:\n")
    user=int(input("1 Stat\n" "2 Ev\n"))
    if user==1:
        base=int(input("Base: "))
        Iv=int(input("IV: "))
        if Iv<0 or Iv>31:
            print("Value is out of range :(")
            main()
        
        Ev=int(input("EV: "))
        if Ev<0 or Ev> 255:
            print ("Value is out of range :(")
            main()
        lvl=int(input("Level: "))
        print('\n',base,Iv,Ev,lvl,'\n')
        var = stat.SCalc.Hp(base,Iv,Ev,lvl)
        print("Pokemon's Hp stat value is: ", var, '\n\n')

    elif user==2:
        Stat=int(input("Enter Desired Increase Stat: "))
        Modifier=int(input("Enter Modifier: "))
        Lvl=int(input("Enter Level: "))  
        base=int(input("Base: "))
        Iv=int(input("IV: "))
        Ev=int(input("EV: "))
        D=(2*base+Iv)
        D=(D+(Ev/4))
        D=(D*(Lvl/100))

        print("EVs Needed is: ",ev.ECalc.Evs(Stat,Modifier,D,Lvl))
        main()
    else:
        main()
    
main()
def Os():
    #atk
    print("For Other Stat Enter following values: \n")
    base1=int(input("Base: "))
    Iv1=int(input("IV: "))
    if Iv1<0 or Iv1>31:
        print("Value is out of range :(\n\n")
        Os()    
    Ev1=int(input("EV: "))
    if Ev1<0 or Ev1> 255:
        print ("Value is out of range :(\n\n")
        Os()
    lvl1=int(input("Level: "))
    print("Choose Nature: ")
    Nature=int(input(("""0 Hardy 1 Lonely 2 Brave""" """3 Adamant 4 Naughty 5 Bold""" """6 Docile 7 Relaxed  8 Impish\n"""
    """9 Lax 10 Timid 11 Hasty""" """12 Serious 13 Jolly 14 Naive""" """15 Modest 16 Mild  17 Quiet\n"""
    """18 Bashful 19 Rash 20 Calm""" """21 Gentle 22 Sassy 23 Careful""" "24 Quirky\n")))
    if Nature==1:
        Nature=1.1
    print('\n',base1,Iv1,Ev1,lvl1,Nature)
    var = stat.SCalc.Atk(base1,Iv1,Ev1,lvl1,Nature)
    print("Attack is: ",var,'\n')

    # def
    base1=int(input("Base: "))
    Iv1=int(input("IV: "))
    if Iv1<0 or Iv1>31:
        print("Value is out of range :(\n\n")
        Os()    
    Ev1=int(input("EV: "))
    if Ev1<0 or Ev1> 255:
        print ("Value is out of range :(\n\n")
        Os()
    lvl1=int(input("Level: "))
    print("Choose Nature: ")
    Nature=int(input(("""0 Hardy 1 Lonely 2 Brave""" """3 Adamant 4 Naughty 5 Bold""" """6 Docile 7 Relaxed  8 Impish\n"""
    """9 Lax 10 Timid 11 Hasty""" """12 Serious 13 Jolly 14 Naive""" """15 Modest 16 Mild  17 Quiet\n"""
    """18 Bashful 19 Rash 20 Calm""" """21 Gentle 22 Sassy 23 Careful""" "24 Quirky\n")))
    if Nature==1:
        Nature=1.1
    print('\n',base1,Iv1,Ev1,lvl1,Nature)
    var = stat.SCalc.Dep(base1,Iv1,Ev1,lvl1,Nature)
    print("Defense is: ",var,'\n')


     # spatk
    base1=int(input("Base: "))
    Iv1=int(input("IV: "))
    if Iv1<0 or Iv1>31:
        print("Value is out of range :(\n\n")
        Os()    
    Ev1=int(input("EV: "))
    if Ev1<0 or Ev1> 255:
        print ("Value is out of range :(\n\n")
        Os()
    lvl1=int(input("Level: "))
    print("Choose Nature: ")
    Nature=int(input(("""0 Hardy 1 Lonely 2 Brave""" """3 Adamant 4 Naughty 5 Bold""" """6 Docile 7 Relaxed  8 Impish\n"""
    """9 Lax 10 Timid 11 Hasty""" """12 Serious 13 Jolly 14 Naive""" """15 Modest 16 Mild  17 Quiet\n"""
    """18 Bashful 19 Rash 20 Calm""" """21 Gentle 22 Sassy 23 Careful""" "24 Quirky\n")))
    if Nature==1:
        Nature=1.1
    print('\n',base1,Iv1,Ev1,lvl1,Nature)
    var = stat.SCalc.Spatk(base1,Iv1,Ev1,lvl1,Nature)
    print("Special Attack is: ",var,'\n')

    # spD
    base1=int(input("Base: "))
    Iv1=int(input("IV: "))
    if Iv1<0 or Iv1>31:
        print("Value is out of range :(\n\n")
        Os()    
    Ev1=int(input("EV: "))
    if Ev1<0 or Ev1> 255:
        print ("Value is out of range :(\n\n")
        Os()
    lvl1=int(input("Level: "))
    print("Choose Nature: ")
    Nature=int(input(("""0 Hardy 1 Lonely 2 Brave""" """3 Adamant 4 Naughty 5 Bold""" """6 Docile 7 Relaxed  8 Impish\n"""
    """9 Lax 10 Timid 11 Hasty""" """12 Serious 13 Jolly 14 Naive""" """15 Modest 16 Mild  17 Quiet\n"""
    """18 Bashful 19 Rash 20 Calm""" """21 Gentle 22 Sassy 23 Careful""" "24 Quirky\n")))
    if Nature==1:
        Nature=1.1
    print('\n',base1,Iv1,Ev1,lvl1,Nature)
    var = stat.SCalc.Spd(base1,Iv1,Ev1,lvl1,Nature)
    print("Special Defense is: ",var,'\n')

     # speed
    base1=int(input("Base: "))
    Iv1=int(input("IV: "))
    if Iv1<0 or Iv1>31:
        print("Value is out of range :(\n\n")
        Os()    
    Ev1=int(input("EV: "))
    if Ev1<0 or Ev1> 255:
        print ("Value is out of range :(\n\n")
        Os()
    lvl1=int(input("Level: "))
    print("Choose Nature: ")
    Nature=int(input(("""0 Hardy 1 Lonely 2 Brave""" """3 Adamant 4 Naughty 5 Bold""" """6 Docile 7 Relaxed  8 Impish\n"""
    """9 Lax 10 Timid 11 Hasty""" """12 Serious 13 Jolly 14 Naive""" """15 Modest 16 Mild  17 Quiet\n"""
    """18 Bashful 19 Rash 20 Calm""" """21 Gentle 22 Sassy 23 Careful""" "24 Quirky\n")))
    if Nature==1:
        Nature=1.1
    print('\n',base1,Iv1,Ev1,lvl1,Nature)
    var = stat.SCalc.Speed(base1,Iv1,Ev1,lvl1,Nature)
    print("Speed is: ",var,'\n')

Os()

     

