p1=20
p2=5
p3=30
if((p1>p2)&(p1>p3)):
    print("p1 is oldest")
elif((p2>p1)&(p2>p3)):
    print("p2 is oldest")
elif((p3>p1)&(p3>p2)):
    print("p3 is oldest")
else:
    print("")

if((p1<p2)&(p1<p3)):
    print("p1 is youngest")
elif((p2<p1)&(p2<p3)):
    print("p2 is yougnest")
elif((p3<p1)&(p3<p2)):
    print("p3 is yongest")
else:
        print(" ")