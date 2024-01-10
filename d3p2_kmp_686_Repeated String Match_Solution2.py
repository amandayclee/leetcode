class Solution:
   def repeatedStringMatch(self, a: str, b: str) -> int:
       # Concatenate a to ensure it is at least as long as b
       repeat_count = -(-len(b) // len(a))  # Ceiling division
       repeated_a = a * repeat_count

       # Extend the repeated string by one more a to handle partial overlaps
       repeated_a += a

       # KMP search in the extended repeated string
       lps = self.compute_lps_array(b)
       i = j = 0  # indexes for repeated_a[] and b[]

       while i < len(repeated_a) and j < len(b):
           if repeated_a[i] == b[j]:
               i += 1
               j += 1

           if j == len(b):
               # Found b in repeated_a, return the minimum number of repeats
               return repeat_count if i <= len(a) * repeat_count else repeat_count + 1

           # Mismatch after j matches
           elif i < len(repeated_a) and repeated_a[i] != b[j]:
               if j != 0:
                   j = lps[j - 1]
               else:
                   i += 1

       return -1  # b is not a substring of any repeat of a
  
   def compute_lps_array(self, pattern):
       """ Compute the longest prefix-suffix (LPS) array. """
       length = 0  # length of the previous longest prefix suffix
       lps = [0] * len(pattern)
       i = 1

       while i < len(pattern):
           if pattern[i] == pattern[length]:
               length += 1
               lps[i] = length
               i += 1
           else:
               if length != 0:
                   length = lps[length - 1]
               else:
                   lps[i] = 0
                   i += 1
       return lps

