class Solution(object):
    def toHex(self, num):
        if num == -1:
            return "ffffffff"
        if num == 0:
            return "0"
        result = ""
        if num < 0:
            num = 4294967296 + num
        while num != 0:
            remainder = num % 16
            if remainder == 10:
                result = "a"+result
            elif remainder == 11:
                result = "b"+result 
            elif remainder == 12:
                result = "c"+result 
            elif remainder == 13:
                result = "d"+result  
            elif remainder == 14:
                result = "e"+result  
            elif remainder == 15:
                result = "f"+result 
            else:
                result =  str(remainder) + result
            num = num / 16
        return result
