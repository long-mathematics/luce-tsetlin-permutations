# Mechanical extraction record: regular-profile microscopic cycles

Date: 11 October 2026.

## Scope

This record covers only the mechanical extraction of the regular positive-profile
microscopic-cycle and sparse-entry theory from the frozen 139-page manuscript.
It is not a mathematical proof audit, novelty review, or formal verification.

## Frozen source

- source: `archive/6178a99/papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex`;
- pinned repository commit: `6178a99a8f2ee7b6416edd026e7780b9b8fa9fa0`;
- source SHA-256: `c6d6a4607a2db9c8a5f69e2ec256c33619083fcc81ab467e9b939673fb3a5028`.

The active source is `papers/regular-profile-cycles/regular-profile-cycles.tex` with SHA-256 `7c4bbf5a78a7e78bb13a9b0ce63061dc8301d8fd61ff89880415277f66c79f7a` before PDF
generation.

## Extracted material

The extraction contains three byte-preserved blocks:

1. exponential-race and Gumbel threshold input, archived lines
   224--336;
2. Bernoulli concentration and the uniform tilted lattice local limit theorem,
   archived lines 353--531;
3. the complete regular positive-profile section, archived lines
   865--2198.

The third block contains the separated bulk local estimate, endpoint and
collision domination, target-crowding estimates, factorial-moment summation,
long-trace universality, diagonal-band laws, sparse-entry laws, thin-graph
corollaries, deterministic-permutation overlaps, and the transverse-curve
corollary.

## Completeness checks

- all 27 theorem-like environments in the selected blocks are
  present;
- all 33 labels and all 21 distinct reference targets are
  present;
- every cited key has its original bibliography entry;
- the three active mathematical blocks compare byte-for-byte with the frozen
  source;
- no active manuscript is imported as a proof dependency;
- no statement from the macroscopic, mesoscopic, order, or total-cycle papers
  is used.

The detailed old-label/new-label map is
`papers/regular-profile-cycles/EXTRACTION_MAP.md`.

## Status boundary

The extraction does not assess the correctness or optimality of the separated
local estimate, endpoint/collision envelopes, improper trace limits, factorial
moment argument, total-variation conclusion for fixed cycle vectors, sparse
entry theorem, or overlap laws. It does not alter a hypothesis, equality,
limit, topology, or proof step. A separate adversarial audit is required
before promotion from working mechanical extraction.
