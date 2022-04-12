import math
from timeit import default_timer as timer


def f1(n):
    s=0
    for j in range(1, n):
      s=s+1/j
    return s

def f2(n):
    s=0
    for j in range(1, n):
      for k in range(1, n):
        s=s+k/j
    return s

def f3(n):
    s=0
    for j in range(1, n):
      for k in range(j, n):
        s=s+k/j
    return s   
        
def f4(n):
    s=0
    for j in range(1, n):
      k=2
      while k<=n:
        s=s+k/j
        k=k*2
    return s           

def f5(n):
    s=0
    k=2
    while k<=n:
       s=s+1/k
       k=k*2
    return s   

nn = [2000, 4000, 8000, 16000, 32000]

for n in nn:  
  start = timer()
  f5(n)
  stop = timer()
  Tn=stop-start
  Fn=100*n
  print(n, Tn, Fn/Tn)

# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n

##f1: n
##2000 0.00011870000162161887 16849199.432830837
##4000 0.00022529999841935933 17754105.761486292
##8000 0.0005583000020124018 14329213.632749176
##16000 0.0009210999996867031 17370535.235525064
##32000 0.0018640000198502094 17167381.791429117

##f2: n*n
##2000 0.22896929999114946 17469590.90216293
##4000 1.0187810999923386 15705042.035153894
##8000 3.819655100000091 16755439.515991503
##16000 15.367220800020732 16658835.278767819
##32000 61.85315760000958 16555339.12467294

##f3: n*n
##2000 0.11991149999084882 33357934.812801644
##4000 0.5582194000016898 28662565.292341266
##8000 2.048995199991623 31234821.828895282
##16000 8.211590100021567 31175447.98044993
##32000 30.777742499980377 33270796.258063857

##f4: n*math.log(n,2)
##2000 0.001701500004855916 12889549.51909116
##4000 0.004499299975577742 10637907.54082859
##8000 0.009761000022990629 10626603.22026272
##16000 0.0218524000083562 10225538.085937781
##32000 0.04301250001299195 11134091.18197113

##f5: math.log(n,2)
##2000 4.8999791033566e-06 2237924.7040360374
##4000 2.9999937396496534e-06 3988603.0849049306
##8000 3.6999990697950125e-06 3504266.9038780103
##16000 2.900022082030773e-06 4815751.014862062
##32000 3.3999967854470015e-06 4401705.421816897
