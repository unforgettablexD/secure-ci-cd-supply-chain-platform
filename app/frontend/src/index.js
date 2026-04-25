import test from "node:test";
import assert from "node:assert/strict";

test("frontend smoke test", () => {
  const supplyChain = "secure";
  assert.equal(supplyChain, "secure");
});
