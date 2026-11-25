import random


satelite=[]
R=random.randint(0,3)
for i in range(4):
    row=["⭐"]*7
    satelite.append(row)

for row in satelite:
    print(" ".join(row))

satelite_row=random.randint(0,3)
satelite_col=random.randint(0,6)

while True:

        user_choice=(int(input("What row do you choose?:")))

        user_choicecol=(int(input("What Col do you choose?:")))
        if user_choice==satelite_row:
            if user_choicecol==satelite_col:
                print("Congratulations you found the satelite!!!")
                satelite[satelite_row][satelite_col]="🛰️ "
                for row in satelite:
                    print(" ".join(row))
                break
            elif user_choicecol>satelite_col:
                print("move west")

            elif user_choicecol<satelite_col:
                print("move east")

        elif user_choice>satelite_row:
            print("move north")

        elif user_choice<satelite_row:
            print("move south")
