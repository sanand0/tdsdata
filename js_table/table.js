import { default as seedrandom } from "https://cdn.jsdelivr.net/npm/seedrandom/+esm";

export function generate(seed, rows, cols) {
  const random = seedrandom(seed);
  return Array.from({ length: rows }, () => Array.from({ length: cols }, () => Math.round(random() * 1000)));
}
