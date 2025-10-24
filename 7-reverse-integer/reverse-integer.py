class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        str_x = str(x)
        rev_str_x = str_x[-1::-1]
        ans = -(int(rev_str_x[:-1])) if is_negative else int(rev_str_x)
        print(ans)
        return ans if ((ans >= -(2**31)) and (ans <= ((2**31) - 1))) else 0