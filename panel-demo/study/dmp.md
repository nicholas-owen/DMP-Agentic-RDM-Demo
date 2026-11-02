# Data Management Plan: MN-TRANSCRIPT

> **Fictional study prepared for training.** The institution, NHS trust, collaborators, people and study are invented. The funder and the laws and guidance referred to are real. Review this plan as if it were a real submission.

| | |
|---|---|
| **Project title** | MN-TRANSCRIPT: transcriptomic signatures of C9orf72 ALS in iPSC-derived motor neurons |
| **Lead applicant** | Dr Rowan Hale, Department of Neuroscience, University of Northbridge |
| **Funder** | Medical Research Council (MRC) |
| **Sponsor** | University of Northbridge |
| **NHS site** | Northbridge Teaching Hospitals NHS Foundation Trust |
| **Duration** | 36 months, from 1 February 2027 |

**Summary.** We will compare gene expression in motor neurons derived from induced pluripotent stem cells (iPSCs) of people with ALS carrying a C9orf72 repeat expansion and of healthy controls, and relate expression differences to clinical features of disease. Whole-genome sequencing will confirm genotypes and support future analyses.

## 1 Data collection

**1.1 Data types.** We will generate (a) whole-genome sequencing (WGS) of blood-derived DNA from all participants; (b) bulk RNA-seq of iPSC-derived motor neurons; and (c) clinical data extracted from NHS records by the clinical team: ALSFRS-R scores, age at onset, site of onset, date of diagnosis and survival status.

**1.2 Participants and samples.** We will recruit six people with ALS carrying a C9orf72 hexanucleotide repeat expansion from the Northbridge MND clinic, and six unrelated healthy volunteers. Each participant will provide a blood sample and a skin biopsy. Fibroblasts from the biopsy will be reprogrammed to iPSCs, giving one iPSC line per participant.

**1.3 Experimental design.** Each iPSC line will be differentiated into motor neurons and harvested at day 30 for RNA extraction. For practical reasons, differentiations will be run in two batches: the six patient lines in batch 1 (February 2028) and the six control lines in batch 2 (April 2028). Each batch will be sequenced on its own sequencing run as soon as it is complete.

**1.4 Volumes and formats.** WGS will be performed at 30x mean coverage. RNA-seq libraries will be stranded, paired-end 2 x 100 bp, at 40 million read pairs per sample. Data will be held as FASTQ, BAM and VCF files and as gene-level count tables. We estimate the total data volume at approximately 60 GB.

**1.5 Software.** RNA-seq data will be processed with nf-core/rnaseq and WGS data with nf-core/sarek, each at a pinned release recorded in the project repository, using the GRCh38 reference with GENCODE annotation. Differential expression will be analysed in R with DESeq2.

## 2 Documentation and metadata

**2.1 Sample information.** Sample information (line identifiers, differentiation dates, RNA quality and library details) will be recorded in a laboratory spreadsheet maintained by the postdoctoral researcher. A formal metadata standard is not needed because the data will be analysed within the group.

**2.2 Code.** Analysis code will be kept in a version-controlled repository on the University's GitLab, with a README describing how to reproduce each analysis.

## 3 Ethics and legal compliance

**3.1 Lawful basis.** The lawful basis for processing personal data under the UK GDPR will be consent (Article 6(1)(a)), with explicit consent (Article 9(2)(a)) for the special category health and genetic data.

**3.2 Data protection impact assessment.** A DPIA is not required for this project because all data will be pseudonymised before they reach the research team.

**3.3 Pseudonymisation.** Participants will be assigned study codes (MNT-001 to MNT-012) by the clinical team at the NHS site. The key linking codes to identities will be held only by the clinical team, on NHS systems, separately from the research data. The research team will not have access to it.

**3.4 Consent.** Participants will give written informed consent to take part in the MN-TRANSCRIPT study and to the use of their samples and data for this study.

**3.5 Genetic findings.** WGS data will be analysed for research purposes only, and participants will not be informed of any findings.

**3.6 Approvals.** NHS Research Ethics Committee and HRA approval will be obtained through IRAS before recruitment begins.

## 4 Storage and backup

**4.1 Primary storage.** All participant-level data (WGS, RNA-seq and clinical data) will be stored in the Northbridge Secure Research Environment (NSRE), the University's trusted research environment.

**4.2 Working copies.** To allow interactive analysis, working copies of the RNA-seq count tables, variant calls and clinical data will be kept on the research group's shared drive and analysis workstation.

**4.3 Analysis workflow.** Pipelines will be run in the NSRE. They will retrieve reference genomes and software containers from public repositories at run time. Results files will be copied out of the NSRE to the group's workstation and to collaborators as needed.

**4.4 Backup.** The NSRE is backed up nightly by IT Services. The group shared drive is backed up weekly.

## 5 Selection and preservation

**5.1 Retention.** Data will be kept in the NSRE for the duration of the grant. Decisions on long-term retention will be made at the end of the project.

**5.2 Code.** Analysis code will remain in the GitLab repository.

## 6 Data sharing

**6.1 Raw data.** Raw sequencing reads (WGS and RNA-seq FASTQ files) will be deposited in the European Nucleotide Archive (ENA) with open access when the main results are published.

**6.2 Exclusive use.** Processed data will be held for a 12-month period of exclusive use by the research team from the end of data generation, after which they will be released as described in 6.4.

**6.3 Collaboration.** Pseudonymised WGS variant calls (VCF files) and clinical data will be shared with collaborators at Calder University, Ohio, USA, for joint analysis of C9orf72 modifier variants. This transfer is covered by the UK-US data bridge.

**6.4 Processed data.** Gene-level count tables and the sample information spreadsheet will be deposited in ArrayExpress (BioStudies) at the end of the exclusive use period.

## 7 Responsibilities and resources

**7.1 Responsibilities.** The PI is responsible for data management. The postdoctoral researcher will maintain the sample spreadsheet and run the analyses. The clinical team at the NHS site will manage recruitment, consent and the pseudonymisation key.

**7.2 Costs.** Storage will be provided from the group's existing allocation. No additional data management or storage costs are requested.
