class Solution(object):
    def addStrings(self, num1, num2):
        index1 = len(num1)
        index2 = len(num2)
        result = ""
        if len(num1) > len(num2):
            #num2 is the smaller number
            carry = 0
            difference = len(num1)-len(num2)
            while index2 > 0:
                print num2[index2-1]
                print num1[index2-1+difference]
                number = int(num2[index2-1])+int(num1[index2-1+difference])+carry
                carry = number/10
                number = number % 10
                result = str(number) + result
                index2 -= 1
            index1 = len(num1)-len(num2)
            while index1 > 0:
                number = carry + int(num1[index1-1])
                carry = number / 10
                number = number % 10
                result = str(number) + result
                index1 -= 1
            if carry != 0:
                result = str(carry) + result
        else:
            #num1 is smaller or they have equal number of digits
            carry = 0
            difference = len(num2)-len(num1)
            while index1 > 0:
                number = int(num2[index1-1+difference])+int(num1[index1-1])+carry
                carry = number/10
                number = number % 10
                result = str(number) + result
                index1 -= 1
            index2 = len(num2)-len(num1)
            while index2 > 0:
                number = carry + int(num2[index2-1])
                carry = number / 10
                number = number % 10
                result = str(number) + result
                index2 -= 1
            if carry != 0:
                result = str(carry) + result
        return result
