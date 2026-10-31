class Solution(object):

  def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    # Handle the special overflow edge case
    INT_MAX = 2147483647  # 2^31 - 1
    INT_MIN = -2147483648  # -2^31

    if dividend == INT_MIN and divisor == -1:
      return INT_MAX

    # Determine the sign of the result
    negative = (dividend < 0) ^ (divisor < 0)

    # Work with positive absolute values to simplify bit shifting
    abs_dividend = -dividend if dividend < 0 else dividend
    abs_divisor = -divisor if divisor < 0 else divisor

    quotient = 0

    # Subtract shifted divisors from the dividend
    while abs_dividend >= abs_divisor:
      temp_divisor, multiple = abs_divisor, 1
      while abs_dividend >= (temp_divisor << 1):
        temp_divisor <<= 1
        multiple <<= 1

      abs_dividend -= temp_divisor
      quotient += multiple

    return -quotient if negative else quotient