import unittest
from merkle import leaf, root, verify, h

class MerkleTests(unittest.TestCase):
    def test_valid_and_invalid_proofs(self):
        leaves = [leaf("alice", 10), leaf("bob", 20), leaf("carol", 30), leaf("dave", 40)]
        tree_root = root(leaves)
        proof = [leaves[0], h(leaves[2] + leaves[3])]
        self.assertTrue(verify(leaves[1], proof, tree_root, 1))
        self.assertFalse(verify(leaf("bob", 21), proof, tree_root, 1))

if __name__ == "__main__": unittest.main()
