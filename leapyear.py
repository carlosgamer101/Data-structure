def is_leap()->bool:
    #DISPLAY
    if(year % 4) == 0:
        #IF ITS DIVISIBLE BY 4 AND ALSO 100 DO THE TEST
        if(year % 100) ==0:
           #IF ITS DIVISIBLE BY 4 100 AND 400 DO THIS TEST
            if (year % 400) ==0:
                leap_year = True

            else:
                leap_year = False

        else:
            leap_year = True

    else:
        leap_year = False

