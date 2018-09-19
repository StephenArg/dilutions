nine_five_percent = 100   #<---- lowest amount of 95% ethanol to use
max_nine_five_percent = 2000 # <----- max amount of 95% ethanol to use
final_dilution_percent = 2 #<---- set final dilution amount here. Be sure to use integer value for percentage w/out % sign """
print("(ml of 95% ethanol, ml of distilled water)")

while nine_five_percent < max_nine_five_percent:
    total_volume = (nine_five_percent*95)/ final_dilution_percent
    water = total_volume - nine_five_percent
    if nine_five_percent % 20 == 0 or nine_five_percent % 50 == 0:
        if water % 20 == 0 or water % 50 == 0:
            print("(", nine_five_percent,",", water, ")")
            nine_five_percent += 10
        else:
            nine_five_percent += 10
    else:
        nine_five_percent += 10


"""Designed to factor in easily measurable dilution amounts of 95% ethanol and water to get 50% ethanol solution. Results 
are printed showing ethanol amount first, followed by water amount. Can be readily tweaked to find any dilution you want.
Just change the umber where the arrow points to """
