# meta
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        left_parenthese_idxes_stack = []
        be_poped = []

        for i in range(len(s)):
            if s[i] == '(':
                left_parenthese_idxes_stack.append(i)
            
            if s[i] == ')':
                if not left_parenthese_idxes_stack:
                    be_poped.append(i)
                else:
                    left_parenthese_idxes_stack.pop()

        be_poped = sorted(be_poped + left_parenthese_idxes_stack)
        for i in range(len(be_poped) - 1, -1, -1):
            del s[be_poped[i]]

        return ''.join(s)

print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print(Solution().minRemoveToMakeValid("))(("))