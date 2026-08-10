#!/usr/bin/env python3
"""Generate the public README from the curated CSV files."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

CATEGORY_ORDER = [
    "Open-vocabulary Counting",
    "Exemplar-based Counting",
    "MLLM-based Counting",
    "Class-agnostic Counting",
    "Class-specific Counting",
    "Video Object Counting",
]

PROTOCOL_ORDER = [
    "standard_3shot_trained",
    "text_only_standard_gt",
    "multimodal_standard_gt",
    "reference_less_no_user_prompt",
    "one_shot_trained",
    "one_shot_detection",
    "detection_output_strict",
    "detection_reference_less",
    "training_free_3shot",
    "modified_split_or_corrected_gt",
]

PROTOCOL_LABELS = {
    "standard_3shot_trained": "Standard 3-shot exemplar-based counting",
    "text_only_standard_gt": "Text-only counting with standard FSC-147 annotations",
    "multimodal_standard_gt": "Multimodal prompting with standard FSC-147 annotations",
    "reference_less_no_user_prompt": "Reference-less counting without a user prompt",
    "one_shot_trained": "One-shot exemplar-based counting",
    "one_shot_detection": "One-shot counting with detection-based evaluation",
    "detection_output_strict": "Detection-output counting under the strict protocol",
    "detection_reference_less": "Reference-less detection-output counting",
    "training_free_3shot": "Training-free counting with 3 exemplars",
    "modified_split_or_corrected_gt": "Modified splits or corrected annotations",
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def clean(value: str) -> str:
    return " ".join((value or "").split()).replace("|", "\\|")


def year_value(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def number_value(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return float("inf")


def paper_entry(row: dict[str, str]) -> str:
    title = clean(row["title"])
    punctuation = "" if title.endswith((".", "?", "!")) else "."
    links = [f"[[Paper]({row['paper_url']})]"]
    if row.get("code_url"):
        links.append(f"[[Code]({row['code_url']})]")
    return (
        f"- **[{clean(row['abbreviation'])}]** {title}{punctuation} "
        f"(**{clean(row['venue'])} {clean(row['year'])}**) {' '.join(links)}"
    )


def dataset_links(row: dict[str, str]) -> str:
    candidates = [
        ("Paper", row.get("paper_url", "")),
        ("Project", row.get("homepage_url", "")),
        ("Download", row.get("download_url", "")),
    ]
    links: list[str] = []
    seen: set[str] = set()
    for label, url in candidates:
        if url and url not in seen:
            links.append(f"[[{label}]({url})]")
            seen.add(url)
    return " ".join(links) if links else "—"


def fsc_table(rows: list[dict[str, str]]) -> list[str]:
    ordered = sorted(rows, key=lambda row: (number_value(row["mae"]), clean(row["method"])))
    output = [
        "| Method | Venue | Prompt | Split | MAE ↓ | RMSE ↓ | Source |",
        "|---|---|---|---|---:|---:|---|",
    ]
    for row in ordered:
        source = f"[Source]({row['source_url']})"
        output.append(
            "| {method} | **{venue} {year}** | {prompt} | {split} | {mae} | {rmse} | {source} |".format(
                method=clean(row["method"]),
                venue=clean(row["venue"]),
                year=clean(row["year"]),
                prompt=clean(row["prompt"]),
                split=clean(row["split"]),
                mae=clean(row["mae"]) or "—",
                rmse=clean(row["rmse"]) or "—",
                source=source,
            )
        )
    return output


def generate() -> str:
    papers = read_csv("papers.csv")
    datasets = read_csv("datasets.csv")
    fsc_rows = read_csv("leaderboard_fsc147.csv")
    cloc_rows = read_csv("leaderboard_cloc.csv")
    tutorials = read_csv("tutorials.csv")
    verified_dates = [
        row.get("verified_on", "")
        for rows in (papers, datasets, fsc_rows, cloc_rows, tutorials)
        for row in rows
        if row.get("verified_on")
    ]
    last_verified = max(verified_dates) if verified_dates else "unknown"

    lines = [
        "# Awesome Object Counting",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "[![License](https://img.shields.io/github/license/Mengqi-Lei/awesome-object-counting)](LICENSE)",
        "",
        "A curated collection of research on visual object counting, including papers, datasets, benchmarks, leaderboards, tutorials, and project resources.",
        "",
        "> **Collection policy.** For work published in 2022 or earlier, we retain seminal and broadly recognized papers. From 2023 onward, we aim for high recall across major conferences, reputable journals, and verifiable arXiv papers, provided that object counting is a central contribution.",
        "",
        "Metadata last verified: **" + last_verified + "**.",
        "",
        "## Contents",
        "",
        "- [What is Object Counting?](#what-is-object-counting)",
        "- [Task Taxonomy](#task-taxonomy)",
        "- [Highlights](#highlights)",
        "- [Datasets and Benchmarks](#datasets-and-benchmarks)",
        "- [Papers](#papers)",
        "  - [Open-vocabulary Counting](#open-vocabulary-counting)",
        "  - [Exemplar-based Counting](#exemplar-based-counting)",
        "  - [MLLM-based Counting](#mllm-based-counting)",
        "  - [Class-agnostic Counting](#class-agnostic-counting)",
        "  - [Class-specific Counting](#class-specific-counting)",
        "  - [Video Object Counting](#video-object-counting)",
        "- [Leaderboard](#leaderboard)",
        "  - [FSC-147](#fsc-147)",
        "  - [CLOC](#cloc)",
        "- [Tutorials and Blogs](#tutorials-and-blogs)",
        "- [Contributing](#contributing)",
        "",
        "## What is Object Counting?",
        "",
        "Object counting estimates how many instances of a target concept appear in an image or video. Depending on the setting, the target may be fixed during training, specified by visual exemplars, described in natural language, or inferred by a multimodal large language model. Methods may predict a scalar count, density map, point set, or detected instances.",
        "",
        "## Task Taxonomy",
        "",
        "The taxonomy is intentionally multi-label: a paper can appear in more than one section when it combines, for example, open-vocabulary language prompts with class-agnostic counting.",
        "",
        "1. **Open-vocabulary Counting** — specifies the target with unrestricted or open-set natural-language concepts.",
        "2. **Exemplar-based Counting** — specifies the target using boxes, points, crops, or reference images.",
        "3. **MLLM-based Counting** — studies counting through multimodal large language models, including direct answers, reasoning, grounding, or tool use.",
        "4. **Class-agnostic Counting** — counts arbitrary or previously unseen categories rather than a fixed training class.",
        "5. **Class-specific Counting** — specializes in a known semantic class or application domain, such as crowds, vehicles, cells, crops, or industrial objects.",
        "6. **Video Object Counting** — counts objects in videos while addressing temporal consistency, motion, recurrence, or tracking.",
        "",
        "## Highlights",
        "",
    ]

    highlights = sorted(
        (row for row in papers if row.get("highlight", "").lower() == "yes"),
        key=lambda row: (-year_value(row["year"]), clean(row["title"])),
    )
    lines.extend(paper_entry(row) for row in highlights)

    verified_dataset_count = sum(row.get("status") == "verified" for row in datasets)
    candidate_dataset_count = len(datasets) - verified_dataset_count
    lines.extend(
        [
            "",
            "## Datasets and Benchmarks",
            "",
            f"The catalog currently contains **{len(datasets)}** datasets and benchmarks: **{verified_dataset_count} verified** entries and **{candidate_dataset_count} candidates** whose metadata is still being completed. See [data/datasets.csv](data/datasets.csv) for task, modality, scale, annotations, access, license, status, and source fields.",
            "",
            "Candidate rows are deliberately marked below and should not be treated as fully verified releases.",
            "",
            "<details>",
            f"<summary><b>Full dataset catalog ({len(datasets)} entries)</b></summary>",
            "",
            "| Year | Dataset | Domain | Scale | Annotations | Links | Status |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for row in sorted(datasets, key=lambda item: (-year_value(item["year"]), clean(item["name"]).lower())):
        status = "Verified" if row.get("status") == "verified" else "Candidate"
        lines.append(
            "| {year} | **{name}** | {domain} | {size} | {annotations} | {links} | {status} |".format(
                year=clean(row["year"]),
                name=clean(row["name"]),
                domain=clean(row["domain"]),
                size=clean(row["size"]),
                annotations=clean(row["annotations"]),
                links=dataset_links(row),
                status=status,
            )
        )
    lines.extend(["", "</details>", "", "## Papers", ""])

    for category in CATEGORY_ORDER:
        category_rows = [
            row
            for row in papers
            if category in {item.strip() for item in row.get("categories", "").split(";")}
        ]
        lines.extend([f"### {category}", "", f"*{len(category_rows)} papers.*", ""])
        grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
        for row in category_rows:
            grouped[year_value(row["year"])].append(row)
        for year in sorted(grouped, reverse=True):
            lines.extend([f"#### {year}", ""])
            for row in sorted(grouped[year], key=lambda item: clean(item["title"]).lower()):
                lines.append(paper_entry(row))
            lines.append("")

    lines.extend(
        [
            "## Leaderboard",
            "",
            "Lower is better for MAE, RMSE, and NAE. Results are only ranked inside the same evaluation protocol; prompts, training data, annotations, splits, and output types can make numbers incomparable.",
            "",
            "### FSC-147",
            "",
            "The standard table below uses the original FSC-147 test annotations and three visual exemplars. Other protocols are separated into expandable tables. Full provenance and protocol notes are available in [data/leaderboard_fsc147.csv](data/leaderboard_fsc147.csv).",
            "",
            "#### Standard 3-shot, FSC-147-trained",
            "",
        ]
    )
    by_protocol: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in fsc_rows:
        by_protocol[row["protocol"]].append(row)
    lines.extend(fsc_table(by_protocol["standard_3shot_trained"]))
    lines.append("")
    for protocol in PROTOCOL_ORDER[1:]:
        rows = by_protocol.get(protocol, [])
        if not rows:
            continue
        lines.extend(
            [
                "<details>",
                f"<summary><b>{PROTOCOL_LABELS[protocol]} ({len(rows)} results)</b></summary>",
                "",
            ]
        )
        lines.extend(fsc_table(rows))
        lines.extend(["", "</details>", ""])

    cloc_pivot: dict[str, dict[str, str]] = {}
    cloc_meta: dict[str, dict[str, str]] = {}
    for row in cloc_rows:
        method = row["method"]
        cloc_meta.setdefault(method, row)
        cloc_pivot.setdefault(method, {})[f"{row['split_or_domain']}::{row['metric']}"] = row["value"]
    cloc_methods = sorted(
        cloc_pivot,
        key=lambda method: (number_value(cloc_pivot[method].get("Full Test::MAE", "")), method.lower()),
    )
    lines.extend(
        [
            "### CLOC",
            "",
            "This is the official static **CLOC-v1.1 corrected-test** snapshot. It must not be mixed with results reported on the original annotation version, and CLOC currently has no public submission server. Full per-domain values and provenance are in [data/leaderboard_cloc.csv](data/leaderboard_cloc.csv).",
            "",
            "| Method | Venue | MAE ↓ | RMSE ↓ | NAE ↓ | Source |",
            "|---|---|---:|---:|---:|---|",
        ]
    )
    for method in cloc_methods:
        meta = cloc_meta[method]
        values = cloc_pivot[method]
        lines.append(
            "| {method} | **{venue} {year}** | {mae} | {rmse} | {nae} | [Source]({source}) |".format(
                method=clean(method),
                venue=clean(meta["venue"]),
                year=clean(meta["year"]),
                mae=clean(values.get("Full Test::MAE", "—")),
                rmse=clean(values.get("Full Test::RMSE", "—")),
                nae=clean(values.get("Full Test::NAE", "—")),
                source=meta["source_url"],
            )
        )

    domains = [
        "General Scene",
        "Remote Sensing",
        "Histopathology",
        "Cellular Microscopy",
        "Agriculture",
        "Microbiology",
    ]
    lines.extend(
        [
            "",
            "<details>",
            "<summary><b>CLOC-v1.1 per-domain MAE</b></summary>",
            "",
            "| Method | " + " | ".join(domains) + " |",
            "|---|" + "|".join("---:" for _ in domains) + "|",
        ]
    )
    for method in cloc_methods:
        values = cloc_pivot[method]
        cells = [clean(values.get(f"{domain}::MAE", "—")) for domain in domains]
        lines.append("| " + clean(method) + " | " + " | ".join(cells) + " |")
    lines.extend(["", "</details>", "", "## Tutorials and Blogs", ""])

    tutorial_groups = [
        ("Surveys", {"survey"}),
        (
            "Project Pages and Official Guides",
            {
                "research project page",
                "official code and dataset guide",
                "research project and code",
            },
        ),
        (
            "Curated Lists and Engineering Tutorials",
            {"curated resource list", "official engineering tutorial"},
        ),
    ]
    for heading, types in tutorial_groups:
        selected = [row for row in tutorials if row["type"] in types]
        if not selected:
            continue
        lines.extend([f"### {heading}", ""])
        for row in sorted(selected, key=lambda item: (-year_value(item["year"]), clean(item["title"]))):
            lines.append(
                f"- [{clean(row['title'])}]({row['url']}) — {clean(row['author_or_organization'])}, {clean(row['year'])}."
            )
        lines.append("")

    lines.extend(
        [
            "## Contributing",
            "",
            "Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for scope, metadata, verification, and formatting requirements. Additions should update the structured CSV first and then regenerate this README.",
            "",
            "## License",
            "",
            "This repository is released under the [Apache License 2.0](LICENSE).",
            "",
        ]
    )
    return "\n".join(lines)


if __name__ == "__main__":
    (ROOT / "README.md").write_text(generate(), encoding="utf-8")
