class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # 1. Handle the one specific overflow edge case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # 2. Determine if the final answer should be negative
        is_negative = (dividend < 0) != (divisor < 0)

        # 3. Work with absolute values to make the logic simpler
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # 4. Subtract multiples of the divisor using bit-shifting
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            
            # Keep doubling the temp_divisor until the next doubling is larger than the dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            # Subtract the large chunk we just found from the dividend
            dividend -= temp_divisor
            # Add the multiple to our final quotient
            quotient += multiple

        # 5. Apply the correct sign to the quotient
        if is_negative:
            quotient = -quotient
            
        return quotient