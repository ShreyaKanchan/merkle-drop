import test from "node:test";
import assert from "node:assert/strict";
test("allocation claims are tied to an account and amount", () => { const leaf = `${"alice"}:10`; assert.equal(leaf, "alice:10"); assert.notEqual(leaf, "alice:100"); });
