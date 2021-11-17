import argparse
import math

parser=argparse.ArgumentParser()

parser.add_argument('--type')

parser.add_argument('--interest',type=float)

parser.add_argument('--periods',type=int )

parser.add_argument('--principal',type=float)

parser.add_argument('--payment',type=float)

args=parser.parse_args()

inputs= [args.type, args.interest, args.periods , args.principal, args.payment]


if args.type not in ("diff" ,"annuity"):
      print("Incorrect parameters.")

elif args.type=="diff" and args.payment is not None:
       print("Incorrect parameters.")

elif args.interest == None:
      print("Incorrect parameters.")


elif len(inputs)<4:
      print("Incorrect parameters.")


elif args.type=="diff":
    P=args.principal
    n=args.periods
    i=args.interest
    i=i*(1/1200)
    if (args.interest < 0 or  args.principal < 0 or args.periods < 0):
        print("Incorrect parameters.")

    Total_payment=0
    for m in range(1, n+1):
       Dm=(P/n) + i*(P-(P*(m-1))/n)
       print(f'Month {m} : payment is {math.ceil(Dm)}')
       Total_payment+=math.ceil(Dm)
       
    overpayment= Total_payment-P
    print(f'overpayment={overpayment}')

elif args.type=="annuity":
       if args.principal==None:
           A=args.payment
           n=args.periods
           i=args.interest
           i=i*(1/1200)
           if (args.interest < 0 or  args.periods < 0 or args.payment <0 ):
                print("Incorrect parameters.")

           P=A/((i*math.pow(1+i,n))/(math.pow(1+i,n)-1))
           print(f'Your loan principal = {P}!')
           A=math.ceil(P*i*(math.pow(1+i,n))/(math.pow(1+i,n)-1))
           Total_payment=(A)*(n)
           Overpayment=Total_payment -P
           print(f'Overpayment={Overpayment}')
         
       elif args.periods==None:
             P=args.principal
             A=args.payment
             i=args.interest
             i=(i)*(1/1200)

             n=math.ceil( math.log( A/(A-i*P),1+i) )
             Y=n//12
             M=n%12
             if Y==0:
                 print(f'It will take {M} months to repay this loan')
             elif M==0:
                  print(f'It will take {Y} years to repay this loan')
             elif Y!=0 and M!=0:
                  print(f'It will take {Y} years and {M} months to repay this loan!')
             Total_payment=A*n
             Overpayment=Total_payment -P
             print(f'Overpayment={Overpayment}')      

       elif args.payment==None:
             P=args.principal
             n=args.periods
             i=args.interest
             i=i*(1/1200)

             A=math.ceil(P*i*(math.pow(1+i,n))/(math.pow(1+i,n)-1))
             print(f'Your annuity payment ={A}!')
             Total_payment=A*n
             Overpayment=Total_payment -P
             print(f'Overpayment={Overpayment}')
