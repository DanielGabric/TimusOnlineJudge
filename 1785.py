def t(n):
    if n >= 1 and n < 5:
        print "few"
    elif n >= 5 and n < 10:
        print "several"
    elif n >= 10 and n<20:
        print "pack"
    elif n >= 20 and n < 50:
        print "lots"
    elif n>=50 and n <100:
        print "horde"
    elif n >= 100 and n < 250:
        print "throng"
    elif n>=250 and n < 500:
        print "swarm"
    elif n >=500 and n < 1000:
        print "zounds"
    else:
        print "legion"
t(input())