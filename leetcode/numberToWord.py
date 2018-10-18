class NumWord(object):
    """docstring for Solution"""

    def numToWord(self, number):
        result = ""
        numWords = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        while(number > 0):
        if(number > 1000000):
            millions = numWords[number % 1000000]
            result += millions + " million "
            number = number / 1000000
        elif(number > 100000):
            thousands = number % 1000
            while(thousands > 0):
                if(thousands > 100):
                    thousands1 = thousands // 100
                    result += numWords[thousands1] + "hundred"
                    thousands = thousands % 100
                elif(thousands < 20 and thousands > 0):
                    result += numWords[thousands] + "hundred"
            number = number / 1000

            number = number / 1000

        print(numWords[number - number % 1000000] + numWords[number - number % 10] + numWords[number % 10].lower())

        return str(number)


obj1 = NumWord()
print(obj1.numToWord(1234))
