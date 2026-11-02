# Agents as a review panel

A teaching demonstration of a multi-agent AI workflow. Five specialist agents, each defined in a short Markdown file, review a fictional research data management plan (DMP). Separate agents then write the panel's report, critique the panel's work and challenge its findings. A plain script checks that every claim in the report traces back to a recorded finding.

The demo asks one question: does a team of specialist agents review a plan better than a single generalist agent, and where does it go wrong? It is designed to make the known failure modes of agent teams visible and measurable: invented claims, conformity, findings lost in summary, and giving way under pushback.

> **Status:** teaching material. The study, institution and people in the plan are fictional, and no real personal data is used. This is not a tool for reviewing real data management plans, and nothing here is legal advice.

## Contents

- [How it works](#how-it-works)
- [Repository layout](#repository-layout)
- [Requirements](#requirements)
- [Running the session](#running-the-session)
- [The reading pack](#the-reading-pack)
- [Safety and data](#safety-and-data)
- [Adapting the demo](#adapting-the-demo)
- [Background](#background)
- [AI assistance](#ai-assistance)
- [Licence](#licence)

## How it works

The main Claude Code session acts as the **chair**. It follows the brief in [`CHAIR.md`](CHAIR.md), invokes each agent in turn, saves every output unchanged and writes no findings of its own.

### The panel

| Agent | Role | Tools |
|---|---|---|
| `data-steward` | Metadata, repositories, licensing, retention, costs | Read, Grep, Glob |
| `ig-officer` | UK GDPR, DPIA, identifiability, data sharing, transfers | Read, Grep, Glob |
| `bioinformatician` | Experimental design, data volumes, compute, pipelines | Read, Grep, Glob |
| `ethics-reviewer` | Approvals, consent scope, genetic findings, capacity | Read, Grep, Glob |
| `tre-officer` | Secure research environment, data in and out | Read, Grep, Glob |
| `generalist` | Baseline: one agent covering every specialist's checklist | Read, Grep, Glob |
| `report-writer` | Writes the report from the findings register alone | Read |
| `critic` | Checks the panel's evidence, the report and conformity | Read, Grep, Glob |
| `applicant` | Challenges chosen findings in the rebuttal round | Read |

The generalist uses exactly the five specialists' checklists combined, so any difference between it and the panel comes from dividing the work, not from better instructions.

### Ground rules

- **Read-only.** No agent can edit files, run code or browse the web.
- **Reading pack only.** Agents may cite only the plan, the samplesheet and the documents in `reading-pack/`.
- **Evidence required.** Every finding either quotes a pack document (30 words at most, with its section) or shows its working from the plan's own text. Findings without evidence are discarded.
- **Structured output.** Specialists return findings as JSON, which the chair saves to a shared register, so every later step can be checked.
- **Reasons to change.** In the discussion and rebuttal rounds, a finding may change only in the light of new evidence, not because others agree, disagree or push back.

### Stages

| Stage | What happens | What it shows |
|---|---|---|
| 0. Pre-flight | The chair checks the files and reports which stages have already run | |
| 1. Baseline | The generalist reviews the plan alone | Breadth against depth |
| 2. Independent review | The five specialists review in parallel, each in its own context | Coverage, referrals between remits, evidence quality |
| 3. Discussion | Each specialist reads everyone's findings and keeps, revises, withdraws or adds | Conformity |
| 4. Write-up | The report writer drafts the report from the register, citing finding IDs | Loss and distortion in summary |
| 5. Trace check | `tools/check_trace.py` compares report and register in both directions | Invented or dropped findings |
| 6. Critic | The critic checks quotes, reasoning, the report and changes made in discussion | What a second agent catches |
| 7. Rebuttal | The applicant challenges chosen findings; specialists uphold, revise or withdraw | Holding ground under pushback |
| 8. Close | The chair writes a summary of counts from the saved files | Scoring, done by the facilitator |

The chair pauses after each stage until the facilitator types `continue`.

## Repository layout

```
.
├── CHAIR.md                 Brief for the main session, which runs the stages
├── .claude/agents/          The nine agent definitions
├── study/
│   ├── dmp.md               The fictional data management plan under review
│   └── samplesheet.csv      Its RNA-seq samplesheet
├── reading-pack/            The only documents agents may cite (see below)
├── register/                Findings written by the chair during a run
├── report/                  Report, baseline and summaries written during a run
└── tools/
    └── check_trace.py       Two-way traceability check (Python standard library only)
```

`register/` and `report/` are empty in a fresh copy and are filled during a run.

## Requirements

- [Claude Code](https://code.claude.com/docs), either the command-line tool or Claude Code on the web. Cloud sessions run in an isolated sandbox and are the recommended way to run the demo.
- A plan with Claude Code access. A full run invokes up to nine agents, so allow enough usage for a rehearsal and the live session.
- Python 3 for the trace check, which uses only the standard library.

Claude Code reads agent definitions from `.claude/agents/` at the repository root. Check that the nine files are there before starting.

## Running the session

Open the repository in Claude Code and send:

```text
Read CHAIR.md and run the session.
```

To run the baseline and independent review ahead of time, for example before an audience arrives:

```text
Read CHAIR.md and run stages 0 to 2, then stop.
```

Later, sending `Read CHAIR.md and run the session.` again resumes at the next stage that has not run.

| Command | Effect |
|---|---|
| `continue` | Run the next stage |
| `rerun N` | Run stage N again, overwriting its files, and report which later files are now out of date |
| `skip to N` | Start stage N, if the files from earlier stages exist |
| `stop` | End the session |

The trace check can also be run by hand:

```bash
python3 tools/check_trace.py register/round2.json report/report.md
```

It exits with status 1 when it finds a problem. That is expected behaviour, not a failure of the script.

## The reading pack

Files 01 to 10 in `reading-pack/` are digests of public UK guidance: HRA, ICO, DSIT, UKRI, MRC, MRC and Wellcome, EMBL-EBI, FGED and the FAIR principles. They are written in the preparer's own words, not copied. Each names and links its source and says which section it summarises. They were checked against their sources on 29 October 2026, and guidance changes, so check the originals before relying on any point outside this exercise.

Files 11 and 12 are the policies of the fictional University of Northbridge: an information classification policy and a secure research environment user guide.

## Safety and data

- The study is fictional, and the repository contains no real personal data. Do not add any.
- Reviewing agents are limited to reading and searching files; none can edit, execute or fetch.
- Run the demo in a sandboxed environment, such as a Claude Code cloud session, rather than on a machine holding sensitive data.
- Keep secrets out of the repository.

Facilitator materials (the answer key, scoring grid and speaker notes) are deliberately kept **outside** this repository. Agents can read any file in the repository they run in, so an answer key placed here would contaminate every run.

## Adapting the demo

- **Change a role:** edit its file in `.claude/agents/`. Each file holds the agent's remit, checklist, evidence rule and output format.
- **Change the case:** replace `study/` and the reading pack. The process in `CHAIR.md` does not depend on the subject matter.
- **Use another tool:** the prompts, the chair's brief, the register format and the trace check are tool-neutral. The agent file headers are Claude Code's format; other tools that support Markdown-defined subagents, such as GitHub Copilot, Gemini CLI, Cursor and OpenCode, need the folder, field names and tool names adapting. Check that read-only restrictions are enforced in the target tool before running it.

## Background

The panel design draws on the Virtual Lab, in which an AI principal investigator led a team of AI scientist agents through research meetings (Swanson et al., *Nature*, 2025, [doi:10.1038/s41586-025-09442-9](https://doi.org/10.1038/s41586-025-09442-9)). The authors reported that their agents tended to be too agreeable with each other. This demo tests for that and related failures directly.

For the research integrity context of AI use in research, see the UK Research Integrity Office's guidance, [*Embracing AI with integrity*](https://ukrio.org/ukrio-resources/embracing-ai-with-integrity/) (2025).

## AI assistance

The agent definitions, chair's brief, documents and code in this repository were drafted with the help of Claude (Anthropic) and reviewed by the author, who is responsible for the content.

## Licence

[Licence to be confirmed.]

---

Maintained by Nick Owen, Centre for Advanced Research Computing, UCL.
