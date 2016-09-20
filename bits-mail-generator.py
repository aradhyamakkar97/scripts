fo = open("shit.txt","w")

for year in range(2014,2017):
    for i in range(1,1000):

        if len(str(i)) == 1:
            adv_i = '00'+str(i)
        elif len(str(i)) == 2:
            adv_i = '0'+str(i)
        else:
            adv_i = str(i)



        fo.write('f'+str(year)+adv_i+'@pilani.bits-pilani.ac.in;')
