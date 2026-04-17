import { describe, it, expect } from "vitest";
import { multiply } from "./math";

describe("Multiply Function", () => {
  it("multiplies correctly", () => {
    expect(multiply(2, 3)).toBe(6);
  });
});