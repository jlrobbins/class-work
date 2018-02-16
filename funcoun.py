def count (tastydish, userlet):
    letcoun = 0
    for letter in tastydish:
        if letter == userlet:
            letcoun = letcoun + 1
    return letcoun
tastydish = input("Choose a delicious dish!: ")
userlet = input("Now choose a letter you want to count in your delicious dish's name: ")
letcoun = count(tastydish, userlet)
print("This is how many times that letter appears in your delicious dish: ",letcoun)