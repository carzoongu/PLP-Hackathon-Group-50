purchased_books = int(input("Enter the number books purchased: "))
if purchased_books == 0:
    points_earned = 0
    print("Points Earned: ", points_earned)
elif purchased_books == 1:
    ponits_earned = 6
    print("Points Earned: ", points_earned)
elif purchased_books == 2:
    points_earned = 16
    print("Points Earned: ", points_earned)
elif purchased_books == 3:
    points_earned = 32
    print("Points Earned: ", points_earned)
elif purchased_books == 4 or purchased_books > 4:
    points_earned = 60
    print("Points Earned: ", points_earned)
else:
    print("Invalid number of books")
    
