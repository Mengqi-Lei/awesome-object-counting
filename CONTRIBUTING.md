# Contributing

Thank you for helping improve Awesome Object Counting.

## Scope

- Work published in 2022 or earlier should be seminal or broadly recognized.
- Work from 2023 onward should come from a major conference, reputable journal,
  or verifiable arXiv release.
- Object counting must be a central task or contribution. Pure detection,
  segmentation, tracking, crowd-flow estimation, and unrelated applications are
  outside the scope.

## Adding a paper

1. Add one row to <code>data/papers.csv</code>.
2. Use one or more of the six exact category names, separated by semicolons:
   Open-vocabulary Counting; Exemplar-based Counting; MLLM-based Counting;
   Class-agnostic Counting; Class-specific Counting; Video Object Counting.
3. Link the original paper and the official code repository when available.
4. Verify the title, venue, year, category, and links against a primary source.
5. Run <code>python3 scripts/generate_readme.py</code>.

The generated paper format is:

    - **[Abbreviation]** Title. (**Venue Year**) [[Paper](URL)] [[Code](URL)]

Venue and year are bold by design. A paper may appear in multiple sections when
it genuinely spans multiple task settings.

## Datasets and leaderboards

- Record dataset scale, annotations, access, license, and verification status in
  <code>data/datasets.csv</code>.
- Do not mix leaderboard values across different prompts, training settings,
  annotations, splits, or output types.
- FSC-147 entries must preserve the <code>protocol</code> field.
- CLOC entries in the current table refer to the corrected CLOC-v1.1 test
  snapshot.

## Pull requests

Keep each pull request focused, cite primary sources, and avoid unrelated
formatting changes. The README is generated from the CSV files and should not be
edited manually for individual entries.
