# Architecture notes

The tree builder is off-chain; the verifier only needs a leaf, sibling path, index, and expected root. This mirrors the storage-saving property of Merkle-based distribution systems.
