in_file = "puzzle.in"
out_file = "puzzle.out"
fin = open(in_file,"r")
fout = open(out_file,"w")

n_testcase = int(fin.readline())

def get_ans(elts):
    a = elts
    count = 0
    for i in range(len(elts)):
        v = a[i]
        h = i
        while (h > 0 and v < a[h -1]):
            a[h] = a[h-1]
            h = h -1
        if h != i:
            count+=1
        a[h] = v
    return count

for testcasenum in range(n_testcase):
    n_elts = int(fin.readline())
    elts = []
    for eltnum in range(n_elts):
        elts.append(fin.readline())

    ans = get_ans(elts)
    fout.write("Case #"+str(testcasenum+1)+": "+str(ans)+"\n")

