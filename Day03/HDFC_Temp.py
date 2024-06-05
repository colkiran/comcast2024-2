
import HDFC
def withDraw_temp(self):
    print(f"Your withdraw of Rs.2000 for the day is completed.....")

# replace the address of withDraw with withDraw_temp
HDFC.Account.withDraw = withDraw_temp

acc01 = HDFC.Account()
acc01.withDraw()

