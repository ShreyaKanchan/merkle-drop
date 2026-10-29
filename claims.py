from dataclasses import dataclass
@dataclass
class ClaimBook:
    claimed: set
    def __init__(self): self.claimed = set()
    def claim(self, account, amount):
        key = (account, amount)
        if key in self.claimed: raise ValueError("already claimed")
        self.claimed.add(key); return key
