in_file = "puzzle.in"
out_file = "puzzle.out"
fin = open(in_file,"r")
fout = open(out_file,"w")

first_line = fin.readline()
fout.write("First Line: "+first_line.upper())

for line in fin:
    fout.write(line)

fin.close()
fout.close()
