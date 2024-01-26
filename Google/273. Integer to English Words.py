class Solution:
    # len(key) = 31
    key = [1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    text = ["Billion", "Million", "Thousand", "Hundred", "Ninety", "Eighty", "Seventy", "Sixty", "Fifty", "Forty", "Thirty", "Twenty", "Nineteen", "Eighteen", "Seventeen", "Sixteen", "Fifteen", "Fourteen", "Thirteen", "Twelve", "Eleven", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]

    def numberToWords(self, num: int) -> str:
        i = 0
        res = []
        
        if not num:
            return "Zero"
        
        # use recursive
        while num:
            k = num // self.key[i]
            
            if k == 0:
                i += 1
                continue
            
            #  234, 000, k = 234 thousand
            # need to call the numberToWords(234) -> Two Hundred Thirty Four
            if k > 20:
                x = str(self.numberToWords(k) + " ")
                res.append(x)
            
            # num=> 234, need to put two in front of Hundred
            # num=> 1,234,567 need to put one in front of Million
            elif num >= 100:
                x = str(self.text[31 - k] + " ")
                res.append(x)
            
            # num = 1,234,567. i = 1, k = 1, adding the Million
            # num %= 1,000,000 next num = 234,567
            res.append(str(self.text[i] + " "))
            num %= self.key[i]
            i += 1

        # transform the list[str] into a string
        res = ''.join(res)
        
        # remove the tail's ' ' whitespace
        res = res[:-1]
        return res


  
