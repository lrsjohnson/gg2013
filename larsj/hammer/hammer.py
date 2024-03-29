import math

in_file = "B-small-attempt0.in"
out_file = "puzzle.out"
fin = open(in_file,"r")
fout = open(out_file,"w")

first_line = fin.readline()

for (i, line) in enumerate(fin):
    parts = line.split(" ")
    v = int(parts[0])
    d = int(parts[1])
    print "v",v,"d",d

    try:
        ans = math.asin(d*9.8/float(v*v))/2*180/(math.pi)
        fout.write("Case #"+str(i+1)+": "+str(ans)+"\n")
    except:
        fout.write("Case #"+str(i+1)+": Impossible\n")

fin.close()
fout.close()
