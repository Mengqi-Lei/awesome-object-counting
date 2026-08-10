# Awesome Object Counting Data

This directory is the structured collection and verification source for the
`awesome-object-counting` repository.

## Paper scope

- Papers published in 2022 or earlier are included only when they are seminal
  or broadly recognized as representative works.
- Papers from 2023 onward are collected with high recall, but must treat visual
  object counting as a central task or contribution.
- Accepted sources are major computer vision, machine learning, and AI
  conferences; reputable journals; and verifiable arXiv preprints.
- Pure object detection, segmentation, tracking, crowd-flow estimation, or
  domain applications without a substantive counting contribution are excluded.

## Categories

- Open-vocabulary Counting
- Exemplar-based Counting
- MLLM-based Counting
- Class-agnostic Counting
- Class-specific Counting
- Video Object Counting

Multiple categories are separated with semicolons.

## Status

- `candidate`: the resource exists, but at least one core field such as size,
  annotations, release availability, or license is not yet confirmed
- `verified`: the recorded metadata and listed links have been checked against
  an original paper, author project page, official repository, or official host
- `published`: already added to the public GitHub README

For leaderboard rows, `verified` additionally means that the reported value was
located in the cited table or official result artifact. It does not make results
from different prompts, annotations, training data, or output types comparable.

## Files

- `papers.csv`: paper metadata used to prepare the public paper list
- `datasets.csv`: datasets and benchmark metadata, ordered by year and name
- `leaderboard_fsc147.csv`: FSC-147 results with protocol and source fields
- `leaderboard_cloc.csv`: CLOC results stored per metric and split/domain
- `tutorials.csv`: surveys, tutorials, talks, and technical resources

## Leaderboard protocol rules

- FSC-147 results must be grouped by the `protocol` column. In particular,
  three-shot, text-only, multimodal, reference-less, one-shot, detection-output,
  training-free, and corrected-annotation results are not one global ranking.
- `leaderboard_cloc.csv` records the corrected CLOC-v1.1 test snapshot. The
  original CLOC paper table is a different annotation version and must not be
  mixed into the same ranking.
- CLOC currently has no public submission server or dynamically maintained
  leaderboard; the CSV cites the official static result artifact.
