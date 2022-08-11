


class Number:

    def two_digit(self,num):
        if len(str(num)) == 1:
            num = "0"+str(num)
        return num