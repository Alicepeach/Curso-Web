def patron(numero):
      for i in range(numero):
        for j in range(i+1):
          if (i % 2 == 0):
            print('*', end = '')
          else:
            print('>', end = '')
        print()
    
      for i in range(numero-1,0,-1):
        for j in range(i):
          if (i+1) % 2 == 0:
            print('*', end = '')
          else:
            print('>', end = '')
        print()