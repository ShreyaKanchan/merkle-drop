# MerkleDrop

> A Merkle-tree allocation toolkit showing how large off-chain allowlists can be verified against one on-chain root.

![MerkleDrop](assets/logo.svg)

Merkle tree and proof verification demo for efficient allowlists and token distributions.

```bash
python3 merkle.py
```

## Why Merkle proofs?

An issuer can publish one root on-chain while keeping the full allocation list off-chain. A claimant supplies the leaf and sibling hashes needed to reconstruct the root, reducing on-chain storage and verification cost.

The example uses sorted, fixed-width pairs for clarity. A production drop should domain-separate leaves, prevent duplicate claims, define allocation encoding precisely, and use a vetted contract implementation.
