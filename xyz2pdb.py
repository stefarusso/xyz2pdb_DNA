#!/bin/python3
#
# arc deve avere 2 linee prima delle xyz
# 
# pdb solo ATOM lines
# 
#

filename_arc='dna.arc'
filename_pdb='modello.pdb'

filename_pdb_final=filename_arc.split(".")[0] + ".pdb"

def line_parser(filename,arc=False):
    with open(filename) as file:
        if arc:
            #arc file has 2 lines before the coordinates
            N_ATOMS=file.readline().split()[0]
            comment = file.readline()
            lines = [line.split() for line in file]
        else:
            return [line for line in file]
    return lines


arc_lines=line_parser(filename_arc,arc=True)
pdb_lines=line_parser(filename_pdb)
print("ALL FILES LOADED")


with open(filename_pdb_final,"w") as f_output: 
    count=0
    for arc_line,pdb_line in zip(arc_lines,pdb_lines):
        atom_line=arc_line[0]
        atom_arc=arc_line[1]
        arc_x,arc_y,arc_z=float(arc_line[2]),float(arc_line[3]),float(arc_line[4])
        pre_string = pdb_line[0:30]
        atom_pbd= pdb_line[77]
        post_string = pdb_line[54:]
        if arc_line[1] == pdb_line[77]:
            string = pre_string
            string += "{:>8.3f}".format(arc_x)
            string += "{:>8.3f}".format(arc_y)
            string += "{:>8.3f}".format(arc_z) + '\n'
#            string += post_string
#            print(string)
            f_output.write(string)
            count += 1
            if count % 10 == 0:
                print("Line : " + str(count))
        else:
            print("ORDER INCORRECT:")
            print("line :" + atom_line + "   arc:" + atom_arc + "   pdb:" + atom_pdb )

print("FILE: " + filename_pdb_final + "  COMPLETED") 
