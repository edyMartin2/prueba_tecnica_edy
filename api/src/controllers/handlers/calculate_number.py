"""
this is the handler calculate
"""

class CalculateNumber:
    def __init__(self):
        self.numbers = set(range(1, 101))
        
    def extract(self, number):
        if not isinstance(number, int):
            return {"error": "Not is a number"}, False
        if number < 1 or number > 100:
            return {"error": "Out of range"}, False
        
        if number in self.numbers:
            self.numbers.remove(number)
            return False, {"message":"success", "NumbersInArray": list(self.numbers)} 
        
        return {"error": "Not a number here"}, False
    
    def calculate_extract(self):
        all_sum = sum(range(1, 101))
        sum_of_our_arr_of_numbers = sum(self.numbers)
        return all_sum - sum_of_our_arr_of_numbers