class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n
        while True:
            binary = self.decimal_to_binary(x)
            if '0' not in binary:
                return x
            x += 1

    def decimal_to_binary(self, num):
        if num == 0:
            return "0"

        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        return binary