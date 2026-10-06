# Prompt and output standard

Status: v0.1, 2026-09-25. Adapted from the Research Desk [workflow-standard.md](../../../Research%20Desk/kit/workflow-standard.md) for standalone use.

## The one difference from the Research Desk standard

The Research Desk standard puts rules in a system prompt and keeps workflows lean. These prompts run standalone, with no system prompt, so **the rules travel inside every prompt**. To stop six copies drifting apart, the shared blocks are written once in `src/` and stitched into each prompt by `build.mjs`. Edit `src/`, never `prompts/`.

Later, when this becomes a Research Desk kit, the shared blocks lift out into the project instruction and the workflow bodies stay as they are.

## Anatomy of a prompt

Every prompt has the same ten sections, in this order. Sections marked *shared* are identical in every prompt.

| # | Section | What it holds |
|---|---|---|
| 0 | Header | ID, name, the question it answers, where it runs in the series, what it needs, what it returns |
| 1 | Purpose | Two or three sentences, including what it is not |
| 2 | Rules | *Shared.* Scope, pack-only, code for numbers, marks, benign first, "not disclosed" is a claim, framework, no gap-filling |
| 3 | Inputs | The pack files this step reads, and what to do when one is missing |
| 4 | Method | Ordered steps. Each is one move, names its comparison, and says what to look for. Framework-specific instructions sit inside the step they change |
| 5 | Judgment notes | What an experienced forensic analyst knows about this step that a junior does not |
| 6 | Output | Fixed sections, each with one line on what a good version contains |
| 7 | Ledger format | *Shared* (F2 to F5). Columns, ID scheme, reading priority, when a computed item becomes a row |
| 8 | Closing sections | *Shared.* Looked for and not found; could not run; code; verification line |
| 9 | Self-check | Pass or fail checks the assistant runs on its own output before returning it |

Test cases and the changelog do not go in the prompt. They live in [TESTS.md](TESTS.md).

## The shared output structure

Every run returns the same skeleton, so outputs from different steps, companies and platforms line up.

1. **Header line.** Company, framework, currency and units, periods covered, step ID, run date.
2. **Summary.** Counts and the highest-priority items, one line each. No conclusions.
3. **Computation or delta tables.** Periods across the columns, oldest to newest. Items down the rows. A formula column.
4. **Ledger rows.** Markdown table plus the same rows as CSV, to save as `ledger-F#.csv`.
5. **Closing sections.** Looked for and not found; could not run; code; verification line; the final line "Candidates for review, not findings."

F1 returns a context sheet instead of a ledger. F6 returns the report.

## The ledger row

The unit every step produces and every later step consumes. Defined once in `src/_ledger.md`.

| Column | Content |
|---|---|
| ID | `F2-A1-03`: step, checklist row, sequence |
| Item | Checklist row and short name |
| Period | Fiscal quarter or year |
| Evidence | Computed value with its comparison, or the sentence as filed |
| Locator | Pack file and location |
| Benign reading | Written first |
| Adverse reading | Written second |
| Context | The context-sheet event that bears on it, or "none" |
| Resolving disclosure | The note or rule that would settle it, and whether it is in the pack |
| Priority | P1 to P4, reading priority by strength of evidence, not severity |
| Verdict | Blank. The analyst fills it |

## Marks

The Research Desk kit's marks, with pack locators instead of numbered web sources, plus one addition for absences:

| Mark | Meaning |
|---|---|
| `[P3, location]` | Copied from pack file P3 |
| `[calc]` | Computed in code; formula in the table, code in the Code section |
| `[inf: P2, P5]` | Inference, naming its inputs |
| `[not found: where searched]` | Searched for and absent |
| `[unverified]` | Could not trace |

## Length

Measured by `build.mjs`; the current table is in [README.md](README.md). The shared blocks add about 1,200 words to F2 to F5 and about 750 to F1 and F6, which carry the rules and their own closing. Workflow bodies run from about 800 words (F6) to about 2,700 (F3, which carries the screens and the IFRS cash-flow adjustments). Whole prompts run from about 1,400 to 3,900 words, or 9,000 to 24,000 characters. That is long for a chat message and untested on both platforms; it is the first thing the test log records.

The length is deliberate. Everything a system prompt would normally hold is inside each prompt, and the method content is the value. When the prompts become a Research Desk kit, the shared blocks move to the project instruction and each prompt drops by about a third.

## Naming

Prompts are `F1` to `F6` (F for forensic) so they never collide with the Research Desk's `W` workflows. The manual's Chapter 12 uses the same IDs.
