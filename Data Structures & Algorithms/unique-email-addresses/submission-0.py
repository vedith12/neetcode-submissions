class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        for email in emails:
            local, domain = email.split("@")
            if "." in local:
                local = local.replace(".", "")
            if "+" in local:
                local = local.split("+")[0]
            hashset.add((local, domain))
        return len(hashset)