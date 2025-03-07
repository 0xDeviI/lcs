class Solution(object):
    num_labels = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
        7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 
        12: "Twelve", 13: "Thirteen", 14: "Fourteen",
        15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
        18: "Eighteen", 19: "Nineteen", 20: "Twenty",
        30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
        70: "Seventy", 80: "Eighty", 90: "Ninety",
        100: "Hundred", 1000: "Thousand", 10**6: "Million", 10**9: "Billion"
    }

    def split_number_to_n(self, num: int, n: int):
        num_str = str(num)[::-1]
        return [num_str[i : i + n][::-1] for i in range(0, len(num_str), n)][::-1]
    
    def print_number_section(self, num_section: str):
        if len(num_section) == 1:
            return self.num_labels[int(num_section)]
        elif len(num_section) == 2:
            value = int(num_section)
            if value == 0:
                return ""
            elif value <= 20:
                return self.num_labels[value]
            else:
                tens = int(num_section[0]) * 10
                ones = int(num_section[1])
                tens_str = self.num_labels[tens]
                if ones == 0:
                    return tens_str
                else:
                    ones_str = self.num_labels[ones]
                    return f"{tens_str} {ones_str}"
        else:  # len == 3
            value = int(num_section)
            if value == 0:
                return ""
            hundreds = int(num_section[0])
            rest = num_section[1:]
            if hundreds == 0:
                return self.print_number_section(rest)
            else:
                hundreds_str = self.num_labels[hundreds] + " Hundred"
                rest_str = self.print_number_section(rest)
                if rest_str:
                    return f"{hundreds_str} {rest_str}"
                else:
                    return hundreds_str
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return self.num_labels[0]
        
        large_scale_numbers = {
            2: self.num_labels[1000],
            3: self.num_labels[10**6],
            4: self.num_labels[10**9],
        }

        splited_number = self.split_number_to_n(num, 3)
        result = ""
        scale_counter = len(splited_number)
        for num_section in splited_number:
            section_value = int(num_section)
            if section_value == 0:
                scale_counter -= 1
                continue
            processed = self.print_number_section(num_section)
            if scale_counter > 1:
                result += f"{processed} {large_scale_numbers[scale_counter]} "
            else:
                result += f"{processed} "
            scale_counter -= 1
        return result.strip()