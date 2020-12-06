d={1:[111,"Adveya", 50000],
2:[222,"Archie",50000],
3:[333,"Avi", 50000],
4:[444,"Souhardya",50000],
5:[555,"Souvik",50000],
6:[444,"Pratik",50000]}

print("{:<8} {:<10} {:<15} {:<10}".format("S.no.","ID","Name", "Salary"))

print("~"*100)

for k, v in d.items():
    id, name, salary=v
    print("{:<8} {:<10} {:<15} {:<10}".format(k, id, name, salary))
    print("-"*100)

print("~"*100)