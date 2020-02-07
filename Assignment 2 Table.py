def table(_from , _to):
    for i in range(_from,_to+1):
      print("\n")
      for x in range(1,10):
        print("\t")
        print(str(x) + " * " + str(i) + " = " + str(x*i))

table(5,10)

