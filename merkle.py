import hashlib
def h(value: bytes) -> bytes: return hashlib.sha256(value).digest()
def leaf(account, amount): return h(f"{account}:{amount}".encode())
def root(leaves):
    layer = leaves[:]
    while len(layer) > 1: layer = [h(layer[i] + layer[i+1]) for i in range(0, len(layer), 2)]
    return layer[0]
def verify(item, proof, expected, index):
    node = item
    for sibling in proof: node = h(node + sibling) if index % 2 == 0 else h(sibling + node); index //= 2
    return node == expected
if __name__ == "__main__":
    leaves = [leaf("alice", 10), leaf("bob", 20), leaf("carol", 30), leaf("dave", 40)]
    bob_proof = [leaves[0], h(leaves[2] + leaves[3])]
    print("root:", root(leaves).hex(), "bob valid:", verify(leaves[1], bob_proof, root(leaves), 1))
