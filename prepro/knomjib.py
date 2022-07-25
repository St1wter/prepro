"""knomjeeb"""
def main():
    "''AYOAYOAYO"
    var_m = int(input())
    var_w = int(input())
    var_1 = int(input())
    var_2 = int(input())
    var_3 = int(input())
    if var_w > var_m:
        print("Now you have %d left." %var_m)
        print("You don’t have enough money!")
    else:
        #wqwwqw 
        sage = (var_m - var_w) % 3
        if sage == 0:
            snack1 = 10
        elif sage == 1:
            snack1 = 15
        elif sage == 2:
            snack1 = 20
        snack11 = snack1 * var_1
        var_ll = (var_m - var_w) - snack11
        #snack2
        sage2 = (var_ll %3)
        if sage2 == 0:
            snack2 = 12
        elif sage2 == 1:
            snack2 = 15
        elif sage2 == 3:
            snack2 = 18
        snack22 = snack2 * var_2
        var_lll = var_ll - snack22
        #snack3
        sage3 = (var_lll %3)
        if sage3 == 0:
            snack3 = 5
        elif sage2 == 1:
            snack3 = 7
        elif sage2 == 3:
            snack3 = 9
        snack33 = snack3 * var_3
        var_all = var_lll - snack33
        #print
        print("Now you have %d  left." %var_all)
        print("Here’s your order!")
        print("Water: %d " %var_w)
        print("Snack number 1: %d baht" %snack11)
        print("Snack number 1: %d baht" %snack22)
        print("Snack number 1: %d baht" %snack33)
main()
