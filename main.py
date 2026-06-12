def total_cal(bill_amount, tip_perc):
#define function to calculate the tip on the bill
    total= bill_amount*(1+0.01* tip_perc)
    total= round(total,2)
    print(f"Please pay ${total}")

#specify only bill_amaount
#default value of tip percent is used

total_cal(150,20)