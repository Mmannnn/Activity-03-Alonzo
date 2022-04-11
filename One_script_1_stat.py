
class SCalc():
    def Hp(base,Iv,Ev,lvl):
        health=(2*base+Iv)
        health=(health+(Ev/4))
        health = (health*lvl)/100+lvl+10
        return health
    def Atk(base1,Iv1,Ev1,lvl1,Nature):
        attk=(2*base1+Iv1)
        attk=(attk+(Ev1/4))
        attk= (attk*lvl1)/100+5*Nature
        return attk
    def Dep(base1,Iv1,Ev1,lvl1,Nature):
        attk=(2*base1+Iv1)
        attk=(attk+(Ev1/4))
        attk= (attk*lvl1)/100+5*Nature
        return attk
    def Spatk(base1,Iv1,Ev1,lvl1,Nature):
        attk=(2*base1+Iv1)
        attk=(attk+(Ev1/4))
        attk= (attk*lvl1)/100+5*Nature
        return attk
    def Spd(base1,Iv1,Ev1,lvl1,Nature):
        attk=(2*base1+Iv1)
        attk=(attk+(Ev1/4))
        attk= (attk*lvl1)/100+5*Nature
        return attk
    def Speed(base1,Iv1,Ev1,lvl1,Nature):
        attk=(2*base1+Iv1)
        attk=(attk+(Ev1/4))
        attk= (attk*lvl1)/100+5*Nature
        return attk

