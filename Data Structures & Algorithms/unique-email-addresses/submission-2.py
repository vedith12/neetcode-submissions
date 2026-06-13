class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            curr = ""
            i = 0
            while i < len(email):
                if email[i] != '@' and email[i].isalnum():
                    curr += email[i]
                elif email[i] == '+':
                    while email[i] != '@':
                        i += 1
                if email[i] == '@':
                    curr += email[i:-1]
                    break
                i += 1
            ans.add(curr)
        print(ans)
        return len(ans)