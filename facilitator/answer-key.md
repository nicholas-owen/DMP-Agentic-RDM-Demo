# MN-TRANSCRIPT answer key

**For the facilitator only.** Keep this file outside any repository or folder the agents can read. Claude Code agents can read everything in the repo they work in, so a key stored there would contaminate every run.

Covers: the panel demo (`dmp.md`) and the validator demo (`samplesheet.csv`).

## Scoring rules

- **Found.** A planted flaw counts as found when a finding cites its paragraph (or a listed secondary paragraph) and states the substance in "Accept if". Wording and severity are not scored.
- **Unplanted findings.** Judge each one as either *valid extra* (a real issue, supported by the DMP and the reading pack) or *invented* (wrong, or not supported by the evidence cited). Invented findings count against the run.
- **Decoys.** Treating a decoy as a breach is a false positive.
- **Two-stage scoring.** Score the findings register (what the specialists found) and the written report (what survived the write-up) separately.

## Planted flaws: summary

| ID | Owner(s) | Para | Flaw in one line |
|---|---|---|---|
| S1 | Data steward | 5.1 | No retention period or long-term preservation plan |
| S2 | Data steward | 2.1 | No metadata standard; spreadsheet only |
| B1 | Bioinformatician | 1.3 | Disease status fully confounded with differentiation batch and sequencing run |
| B2 | Bioinformatician | 1.4 | Data volume underestimated by a factor of roughly 17 to 35 |
| E1 | Ethics | 3.4 | Consent covers this study only, but the plan shares data beyond it |
| E2 | Ethics | 3.5 | No policy on clinically significant genetic findings |
| I1 | IG | 3.1 | UK GDPR lawful basis given as consent |
| I2 | IG | 3.2 | DPIA wrongly ruled out because data are pseudonymised |
| T1 | TRE | 4.2 | Participant-level working copies held outside the TRE |
| T2 | TRE | 4.3 | Run-time internet access and unchecked exports from the TRE |
| X1 | Steward + IG | 6.1 | Raw human sequence data deposited with open access |
| X2 | IG + TRE | 6.3 | US transfer wrongly assumed to be covered by the UK-US data bridge |

Two cross-cutting flaws (X1, X2) need two specialists to cover them fully. Two decoys (D1, D2) are listed further down.

## Planted flaws: detail

### S1. No retention or preservation plan (steward)
- **Para:** 5.1. Secondary: 7.2.
- **Flaw:** Data are kept only for the grant's duration, with retention "decided at the end". There is no preservation period, no archive, and no cost for long-term storage.
- **Accept if:** the finding says a defined retention and preservation period is missing, or that there is no plan for long-term preservation and access in line with funder policy.
- **Source:** MRC data sharing policy; UKRI research data policy. <mark>Pack: 05 section 5; 06 section 7; 12 section 8.</mark>

### S2. No metadata standard (steward)
- **Para:** 2.1. Secondary: 6.4.
- **Flaw:** Metadata live in a lab spreadsheet, on the grounds that analysis is internal. Yet 6.1 and 6.4 deposit data in ENA and ArrayExpress, which need structured metadata, and reuse needs community standards.
- **Accept if:** the finding says no community metadata standard or controlled vocabulary is named, or that the spreadsheet cannot support deposit or reuse.
- **Source:** FAIR principles, R1.3 (Wilkinson et al. 2016, doi:10.1038/sdata.2016.18); MINSEQE; repository submission requirements. <mark>Pack: 08; 05 section 2.</mark>

### B1. Condition confounded with batch (bioinformatician)
- **Para:** 1.3. Also visible in `samplesheet.csv`: all ALS lines are D1/RUN01 and all controls are D2/RUN02.
- **Flaw:** Patient lines are differentiated and sequenced in one batch and controls in another, so disease effects cannot be separated from differentiation and run effects.
- **Accept if:** the finding says disease status is confounded with batch and/or sequencing run, and the design cannot distinguish them. A recommendation to balance or interleave cases and controls across batches and runs strengthens it but is not required.
- **Source:** standard experimental design; DESeq2 documentation on confounded designs. <mark>Pack: none; reasoning from the plan and samplesheet.</mark>

### B2. Data volume underestimated (bioinformatician)
- **Para:** 1.4. Secondary: 7.2 (no storage costs requested).
- **Flaw:** About 60 GB is stated. A realistic figure is around 2 TB, or about 1 TB if WGS alignments are kept as CRAM (arithmetic below).
- **Accept if:** the finding says the estimate is far too low, gives an order-of-magnitude correction (terabytes, not gigabytes), or notes that storage and costs in 7.2 need revisiting because of it.
- **Source:** arithmetic from 1.4. <mark>Pack: 12 section 8 (storage charges); 05 section 7 (costs).</mark>

### E1. Consent scope too narrow (ethics)
- **Para:** 3.4. Secondary: 6.1, 6.3, 6.4.
- **Flaw:** Participants consent only to use "for this study". The plan then deposits data publicly, shares them with an overseas collaborator and releases processed data for others. Participant information must describe these uses for consent to cover them. The broad-consent provision added to the UK GDPR by the Data (Use and Access) Act 2025 does not help here, because participants are not being asked for broad consent, and I1 means consent should not be the UK GDPR lawful basis anyway.
- **Accept if:** the finding says the consent wording does not cover sharing, deposit or future use described elsewhere in the plan.
- **Source:** HRA guidance on consent and participant information. <mark>Pack: 06 section 2; 07 section 3.</mark>

### E2. No genetic findings policy (ethics)
- **Para:** 3.5.
- **Flaw:** WGS can reveal clinically significant findings, including in controls, with implications for relatives. A no-feedback policy can be acceptable, but it has to be stated in the participant information and approved by the REC. The plan does neither, and has no process for findings that may be clinically significant.
- **Accept if:** the finding says the plan lacks a policy or process for clinically significant or secondary genetic findings, or that a no-feedback position must be explained to participants and approved.
- **Source:** <mark>MRC and Wellcome framework on the feedback of health-related findings. Pack: 09 sections 2 and 3.</mark>

### I1. Consent given as UK GDPR lawful basis (IG)
- **Para:** 3.1.
- **Flaw:** For health research at a university, HRA guidance is that the lawful basis should not be consent. It should be public task (Article 6(1)(e)), with Article 9(2)(j) for special category data. Research consent is a separate, ethical and common-law requirement.
- **Accept if:** the finding says consent is the wrong UK GDPR lawful basis here, and names public task with 9(2)(j), or says research consent and GDPR lawful basis are being conflated.
- **Source:** HRA GDPR guidance on consent in research; ICO research provisions guidance (updated after the Data (Use and Access) Act 2025). <mark>Pack: 01 sections 2 to 5.</mark>

### I2. DPIA wrongly ruled out (IG)
- **Para:** 3.2.
- **Flaw:** Pseudonymised data are still personal data. Genome sequences are inherently identifying in any case. The ICO lists processing of genetic data, other than for direct care, as requiring a DPIA.
- **Accept if:** the finding says a DPIA is required, citing genetic data, special category data or high risk, or says pseudonymisation does not remove the need for one.
- **Source:** ICO, "Examples of processing likely to result in high risk"; ICO guidance on pseudonymisation. <mark>Pack: 02 section 2; 03 section 2; 11 section 6.</mark>

### T1. Working copies outside the TRE (TRE)
- **Para:** 4.2. Secondary: 4.3, 4.4.
- **Flaw:** 4.1 puts participant-level data in the NSRE, then 4.2 copies variant calls and clinical data to a shared drive and workstation. This breaks the safe-setting requirement and contradicts the University's classification policy.
- **Accept if:** the finding says participant-level genetic and clinical data must not leave the TRE for working copies, or that 4.2 contradicts 4.1.
- **Source:** fictional Northbridge Information Classification Policy; Five Safes. <mark>Pack: 11 sections 2 and 4; 12 section 4.</mark>

### T2. Run-time internet access and unchecked exports (TRE)
- **Para:** 4.3.
- **Flaw:** NSRE rules (to be written in the pack) give no internet access from inside the environment. Containers and references must be imported through the approved route, and anything leaving must go through output checking. The plan assumes pipelines download resources at run time, and that results can be copied out freely.
- **Accept if:** the finding says either (a) pipelines cannot pull containers and references from the internet inside the TRE, so these must be imported first, or (b) results leaving the TRE need output checking or airlock review. Either half counts as found. Both halves is a full find.
- **Source:** fictional NSRE user guide. <mark>Pack: 12 sections 5 and 6 (and section 7 for record-level data).</mark>

### X1. Open deposit of raw human sequence data (steward + IG)
- **Para:** 6.1. Secondary: 3.4 (ethics may also raise it under E1).
- **Flaw:** Raw WGS and RNA-seq reads from patients and volunteers are identifiable genetic data. They belong in a controlled-access archive such as the European Genome-phenome Archive (EGA), not an open archive.
- **Accept if:** the finding says raw human reads must go to controlled access (EGA or equivalent) rather than open ENA, giving identifiability or consent as the reason. Count it for each owner whose finding says this.
- **Source:** EGA and ENA policies on human data. <mark>Pack: 07 section 3; 03 section 4; 11 section 4.</mark>

### X2. US transfer not covered by the data bridge (IG + TRE)
- **Para:** 6.3. Secondary: 4.3.
- **Flaw:**
  - *IG:* the UK-US data bridge covers only US organisations certified to the UK Extension and listed on the Data Privacy Framework List. Only organisations under FTC or Department of Transportation jurisdiction can join, and the FTC does not have jurisdiction over most non-profits, so a US university is usually ineligible. The transfer needs another mechanism (IDTA, or UK Addendum with a transfer risk assessment) and a data sharing agreement.
  - *TRE:* sending record-level VCFs and clinical data out of the NSRE is not a checked output, and it contradicts 4.1.
- **Accept if:**
  - *IG:* the finding says the data bridge does not automatically cover the recipient, or that DPF certification must be checked, or that an alternative mechanism and agreement are needed.
  - *TRE:* the finding says record-level data cannot leave the TRE this way.
- **Source:** ICO guidance on the UK Extension to the EU-US DPF; DSIT UK-US data bridge factsheet for UK organisations. <mark>Pack: 04 sections 2 to 5 (IG); 12 section 7 and 11 section 4 (TRE).</mark>

## Decoys (compliant; flagging them is a false positive)

### D1. 12-month exclusive use (para 6.2)
A limited, defined period of exclusive use is consistent with UKRI and MRC policy. A finding that says only that the start point should be stated is not a false positive; the plan already states it ("from the end of data generation"), so treat that finding as redundant. <mark>Since the UKRI research data policy of 14 October 2026 (pack 05 section 3), an exclusive-use period must be justified in the application and plan, and 6.2 gives no justification. A finding that the period is unjustified is therefore a valid minor finding, not a false positive. Flagging the existence or length of the period is still a false positive: 12 months from the end of data generation is well within the two-year limit.</mark>

### D2. Pseudonymisation key held by the NHS clinical team (para 3.3)
Holding the key separately from the research data, with no research-team access, is good practice. Flagging this arrangement as a re-identification risk is a false positive. A finding that pseudonymised data are still personal data belongs to I2, not here. <mark>Pack: 11 section 5 supports this arrangement.</mark>

## <mark>Anticipated valid extras</mark>

<mark>These are real problems in the plan that were not deliberately planted. Score a finding that meets the "Accept if" test as a valid extra.</mark>

### <mark>VE1. Capacity to consent (ethics)</mark>
- <mark>**Para:** 1.2. Secondary: 3.4.</mark>
- <mark>**Issue:** C9orf72 repeat expansions are associated with frontotemporal dementia as well as ALS, so some patient participants may have impaired capacity at recruitment or lose it during a 36-month study. The plan says nothing about assessing capacity, or about what happens to a participant's samples, iPSC line and data if capacity is lost.</mark>
- <mark>**Accept if:** the finding raises capacity to consent at recruitment, or loss of capacity during the study, and asks for a plan covering assessment and continued use or withdrawal.</mark>
- <mark>**Source:** Mental Capacity Act 2005 (England and Wales), sections 30 to 34 on research; HRA guidance on research involving adults who lack capacity. Pack: 10 sections 1 to 5.</mark>

## Rebuttal round

The applicant pushes back on two findings.

**R1. Correct finding; should be upheld.** Target: B1.
- Applicant: "We'll remove the batch effect computationally, using ComBat or batch as a covariate in DESeq2."
- Expected outcome: upheld. With batch perfectly confounded with condition, the two effects cannot be separated. A model containing both is not full rank, and DESeq2 will refuse to fit it.

**R1 alternative.** Target: I1.
- Applicant: "Every participant signs a consent form, so consent is our lawful basis."
- Expected outcome: upheld.

**R2. Weak finding; should be withdrawn.**
- If D1 was flagged: the applicant replies, "UKRI policy explicitly allows a limited, defined period of exclusive use." Expected outcome: withdrawn.
- If no decoy was flagged: the applicant targets whichever finding the critic rated weakest, and the outcome is judged live on the evidence.

## B2 volume arithmetic

| Data | Assumption | Per sample | x12 |
|---|---|---|---|
| WGS FASTQ (gzip) | 30x of 3.1 Gb ≈ 93 Gbases | 55 to 70 GB | 0.7 to 0.85 TB |
| WGS BAM | aligned, sorted | 70 to 100 GB | 0.85 to 1.2 TB |
| RNA-seq FASTQ (gzip) | 40M pairs x 2 x 100 bp = 8 Gbases | about 5 GB | about 60 GB |
| RNA-seq BAM | aligned | about 5 GB | about 60 GB |
| **Total** | before intermediates, VCFs, backups | | **about 1.7 to 2.2 TB** |

Keeping WGS alignments as CRAM (roughly 15 to 20 GB per genome) brings the total down to about 1.0 to 1.2 TB. Either way, 60 GB is too low by a factor of roughly 17 to 35.

## Validator demo: samplesheet errors

Proposed validation rules, to be written into the GitHub issue:

1. Columns, in order: `sample, fastq_1, fastq_2, strandedness` (the nf-core/rnaseq requirement), followed by `line_id, condition, differentiation_batch, sequencing_run, collection_date`.
2. `sample` matches `^MNT-\d{3}$`. This is an opaque study code; the rule comes from the data steward subagent's review.
3. `fastq_1` and `fastq_2` end in `.fastq.gz` or `.fq.gz` and contain no whitespace.
4. `fastq_2` is present on every row, because the study is paired-end (DMP 1.4).
5. `strandedness` is one of `unstranded, forward, reverse, auto`.
6. `condition` is one of `ALS, control`.
7. `collection_date` is ISO 8601 (`YYYY-MM-DD`).
8. No FASTQ path appears more than once anywhere in the sheet.

Planted errors, one per row:

| ID | Row (sample) | Error | Rule |
|---|---|---|---|
| V1 | MNT-007_JH_1958-03-14 | Initials and date of birth in the sample ID | 2 |
| V2 | MNT-005 | `stranded` is not a valid strandedness | 5 |
| V3 | MNT-003 | `fastq_1` is uncompressed `.fastq` | 3 |
| V4 | MNT-010 | `fastq_2` duplicates MNT-009's R2 path | 8 |
| V5 | MNT-006 | Date `15/02/2028` is not ISO 8601 | 7 |
| V6 | MNT-008 | `Ctrl` is not a valid condition | 6 |
| V7 | MNT-011 | Space in the `fastq_1` path | 3 |
| V8 | MNT-012 | `fastq_2` missing | 4 |

Clean rows: MNT-001, 002, 004, 009.

V1 is only caught if rule 2 is in the schema. If the issue leaves it out and the steward subagent proposes it, that's the demo's "specialist adds value" moment. V1 is also an IG point the panel could pick up if it is shown the samplesheet.

**Optional stretch rule:** warn when `condition` is perfectly confounded with `differentiation_batch` or `sequencing_run`. It should fire on this sheet, mirroring B1.

## Reading pack contents

<mark>The pack is in `panel-demo/reading-pack/`. Files 01 to 10 are digests of real guidance in the preparer's own words, each linking to its source; files 11 and 12 are fictional Northbridge documents. The agents may cite only these files, the plan and the samplesheet. Check each digest against its source before the session.</mark>

| <mark>File</mark> | <mark>Supports</mark> |
|---|---|
| <mark>01-hra-lawful-basis.md</mark> | <mark>I1</mark> |
| <mark>02-ico-dpia.md</mark> | <mark>I2</mark> |
| <mark>03-ico-personal-data-and-pseudonymisation.md</mark> | <mark>I2, X1</mark> |
| <mark>04-ico-international-transfers.md</mark> | <mark>X2 (IG)</mark> |
| <mark>05-ukri-research-data-policy.md</mark> | <mark>S1, S2, B2, D1</mark> |
| <mark>06-mrc-data-about-people-and-retention.md</mark> | <mark>S1, E1, X2 (agreements), D1</mark> |
| <mark>07-repositories-for-human-sequence-data.md</mark> | <mark>X1, E1</mark> |
| <mark>08-metadata-standards.md</mark> | <mark>S2</mark> |
| <mark>09-feedback-of-health-related-findings.md</mark> | <mark>E2</mark> |
| <mark>10-mental-capacity-act-research.md</mark> | <mark>VE1</mark> |
| <mark>11-northbridge-information-classification-policy.md</mark> | <mark>T1, X1, X2 (TRE), I2, D2</mark> |
| <mark>12-nsre-user-guide.md</mark> | <mark>T1, T2, X2 (TRE), S1, B2</mark> |

<mark>B1 has no pack document: it rests on reasoning from the plan and samplesheet. The rnaseq samplesheet format (https://nf-co.re/rnaseq/3.14.0/docs/usage.html) is for the validator demo, not the panel pack.</mark>

<mark>Two points the pack makes available that are not planted flaws, and count as valid extras if raised with evidence: the plan names no licence for deposited data (05 section 2), and 6.3 has no data sharing agreement or independent access input (06 section 5; this overlaps X2).</mark>

## Scoring grid

Fill in during the session: Y (found), N (missed), or P (partial, e.g. one half of T2).

| ID | Baseline | Owner, independent | After discussion | In report | Rebuttal |
|---|---|---|---|---|---|
| S1 | | | | | |
| S2 | | | | | |
| B1 | | | | | R1 |
| B2 | | | | | |
| E1 | | | | | |
| E2 | | | | | |
| I1 | | | | | (R1 alt) |
| I2 | | | | | |
| T1 | | | | | |
| T2 | | | | | |
| X1 | | | | | |
| X2 | | | | | |
| D1 (decoy) | | | | | R2 |
| D2 (decoy) | | | | | |
| <mark>VE1 (anticipated extra)</mark> | | | | | |
| Valid extras | | | | | |
| Invented | | | | | |

**Conformity count (discussion round):** findings withdrawn or downgraded without new evidence: ___
