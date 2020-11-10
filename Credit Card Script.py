
class CreditCard():
    
    def __init__(self, numcode, cvv, expiredate):
        self.numcode = numcode
        self.expiredate = expiredate
        self.cvv = cvv

    def __str__(self):
        return "Number Code: {}  |  CVV: {}  |  Expire Date: {}".format(self.numcode, self.cvv, self.expiredate)

    def code_check(self):
        
        finalnumber = 0

        # reverse the initial string
        numberstring = self.numcode[::-1]

        for index,number in enumerate(numberstring):

            # convert the string to number
            currentnumber = int(number)

            if index % 2 != 0:
                multipliednum = currentnumber * 2
                if multipliednum >= 10:
                    sumnumb = 1 + (multipliednum % 10)
                    finalnumber = finalnumber + sumnumb
                else:
                    finalnumber = finalnumber + multipliednum

            else:
                finalnumber = finalnumber + currentnumber
        
        if finalnumber % 10 == 0:
            return True
        else:
            return False


def main():
    print("Credit Card Validity script")
    number = input("Insert the credit card number: ")
    cvv = input("Insert the credit card cvv: ")
    expiredate = input("Insert the credit card expire date: ")
    ccard = CreditCard(number, cvv, expiredate)
    if ccard.code_check():
        print("Valid Credit Card")
    else:
        print("Invalid Credit Card")

    print(ccard)

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")