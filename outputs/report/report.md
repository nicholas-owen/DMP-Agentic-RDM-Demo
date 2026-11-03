# Panel review of the data management plan

## Summary

The panel recorded 42 findings: 27 major and 15 minor. Where findings described the same problem they have been merged. This gives 22 major items and 14 minor items below.

Major issues affect sections 1.1, 1.2, 1.3, 1.4, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5, 4.2, 4.3, 5.1, 6.1, 6.3, 6.4, 7.1 and 7.2. Minor issues affect sections 1.2, 1.5, 2.1, 3.4, 3.5, 4.1, 5.2, 6 (general), 6.1, 6.3, 6.4 and 7.1.

## Major issues

### Section 1.1 (also 3.3, 6.3 and 7.1)

**Controller and processor roles and data sharing agreements are not set out.** The plan never says who the controller or controllers are [IG-5]. Data flow between three organisations [IG-5]:
- the NHS Trust, which extracts clinical records and holds the pseudonymisation key;
- the University, which receives and analyses the data;
- Calder University, which receives VCFs and clinical data for "joint analysis", suggesting joint or separate controllership.

No agreement is named for any of these flows [IG-5]. The plan does not say who does the sequencing, and an outside provider would be a processor needing a contract [IG-5]. Set out the role of the University (as sponsor), the NHS Trust, Calder University and any sequencing provider [IG-5]. Before any data flow, name and put in place a Trust-to-University data sharing agreement [IG-5]. Also put in place a data sharing or joint-controller agreement with Calder, approved by the Information Governance Office [IG-5]. Any outside sequencing service needs an Article 28 processor contract [IG-5].

### Section 1.2

**Replication is too low for the line-level comparison and for the clinical association.** There is one iPSC clone and one differentiation per participant [BIO-2]. Variation between lines and between differentiations therefore cannot be estimated or separated from donor genotype [BIO-2]. The aim of relating expression to clinical features rests on six patients, which cannot support a meaningful association analysis, and no power calculation is given [BIO-2]. Give a power or sample-size justification for the case-control comparison [BIO-2]. Add replicate differentiations, ideally with a second clone per donor, and model them as nested or random effects [BIO-2]. Either drop the clinical-association aim or reframe it as exploratory and descriptive, with a stated analysis approach [BIO-2].

### Section 1.3

**Disease status is completely confounded with differentiation batch, sequencing run and date.** All six ALS lines go through differentiation batch 1 and sequencing run 1 [BIO-1]. All six controls go through batch 2 and run 2, two months later [BIO-1]. The disease effect therefore cannot be separated from batch, run or time effects [BIO-1]. Batch cannot be included as a covariate, and removing it afterwards would also remove the disease signal, so the study's main comparison is defeated [BIO-1]. Redesign so that each differentiation batch holds a balanced mix of ALS and control lines, for example 3+3 per batch across at least two batches, or all 12 lines in every batch [BIO-1]. Pool and multiplex all libraries across sequencing runs or lanes, and randomise harvest order [BIO-1]. Record batch, run and harvest date so they can be modelled as covariates [BIO-1].

**Samplesheet errors would corrupt the differential expression analysis.** Several rows contradict the paired-end, two-group design [BIO-6]:
- MNT-010's second read file belongs to MNT-009;
- MNT-012 has no second read file;
- MNT-008 is labelled 'Ctrl' where the other controls are 'control';
- MNT-005 has the strandedness value 'stranded', which the pipeline does not accept.

Run as it stands, the analysis would mix reads across samples, process one sample as single-end and create a spurious third condition level in DESeq2 [BIO-6]. Correct the file paths for MNT-010 and MNT-012, and confirm whether MNT-012's second read file exists [BIO-6]. Harmonise the condition labels and set MNT-005's strandedness to 'reverse' or 'auto' [BIO-6]. Validate the samplesheet against the pipeline schema before each run [BIO-6]. Check genotype concordance between RNA and WGS data to detect sample swaps [BIO-6].

### Section 1.4

**The data volume estimate of 60 GB is out by more than an order of magnitude.** The stated assays and depths produce roughly 1.3 to 2.5 TB of retained data [BIO-3]. Pipeline scratch space while running is several times larger [BIO-3]. Storage requests, compute planning and costs built on 60 GB will be badly undersized [BIO-3]. Recalculate volumes for each data type and stage: raw FASTQ, aligned BAM or CRAM, VCF, counts and pipeline scratch [BIO-3]. State which intermediates are kept, and consider CRAM for WGS alignments [BIO-3]. Size and cost NSRE project storage and compute to match [BIO-3].

### Section 2.1

**No metadata standard is adopted.** Section 2.1 rejects a formal metadata standard because the data "will be analysed within the group" [STW-2]. That contradicts the deposit for reuse planned in sections 6.1 and 6.4 [STW-2]. Without MINSEQE-level description, controlled vocabularies and provenance, the deposited RNA-seq data cannot be properly interpreted or reused, and they do not meet UKRI's FAIR requirement [STW-2]. Adopt MINSEQE for the RNA-seq experiment, including a sample-to-data table and protocols [STW-2]. Name controlled vocabularies for disease, cell type and sex, for example ontology terms [STW-2]. Record provenance: pipeline releases, GRCh38 and GENCODE versions, and differentiation and batch information [STW-2]. Capture metadata in a structured template from the start, not in an ad hoc spreadsheet [STW-2].

**The sample information spreadsheet is Highly Confidential, but its storage location is unspecified and it is released without output checking.** The plan does not say where the spreadsheet kept by the postdoc is stored [TRE-6]. It links study codes to ALS or control status and is the input file for pipelines that run inside the NSRE, so it is Highly Confidential and belongs in the NSRE [TRE-6]. Section 6.4 then deposits it publicly with no output check [TRE-6]. State that the spreadsheet is held and maintained inside the NSRE [TRE-6]. Release any version for ArrayExpress only as a curated, de-identified table after airlock output checking [TRE-6].

### Section 3.1

**Consent is the wrong UK GDPR lawful basis.** The plan uses consent (Article 6(1)(a)) and explicit consent (Article 9(2)(a)) as the lawful basis [IG-1]. The University and the NHS Trust are public authorities, so there is an imbalance of power [IG-1]. If a participant withdraws, no lawful basis would remain to keep processing their data, even after analysis or sharing with Calder or ENA [IG-1]. This leaves the processing on an unstable footing [IG-1]. Use public task (Article 6(1)(e)) as the lawful basis and record why the research is a public task [IG-1]. Use Article 9(2)(j), with appropriate safeguards, as the special category condition [IG-1]. Keep consent to take part as the ethical and common-law requirement, and update the participant information to match [IG-1].

### Section 3.2 (also 3.3 and 6.3)

**A DPIA is mandatory, and the stated reason for not doing one is wrong.** The plan says no DPIA is needed because the data are pseudonymised [IG-2]. However, whole-genome sequences are genetic data, and processing genetic data always needs a DPIA, whether pseudonymised or not [IG-2]. The project also combines NHS clinical records with lab-generated data and sends data abroad, which are further high-risk features [IG-2]. Under Article 35, processing should not start without a DPIA [IG-2]. Replace section 3.2 with a commitment to complete the University's DPIA screening and a full DPIA [IG-2]. Both must be approved by the Data Protection Officer before recruitment or any processing begins [IG-2]. The DPIA should cover the genetic data, the combination of clinical and lab data, the US transfer and any public deposit [IG-2].

**The plan treats pseudonymised data as if they were outside data protection law.** The plan relies on pseudonymisation to skip the DPIA and to justify sharing VCFs and clinical data [IG-3]. Pseudonymised data are still personal data, and genome sequences can identify a person on their own [IG-3]. The WGS, VCF and clinical data held by the research team and by any recipient are therefore special category personal data and need the full set of controls [IG-3]. State that all participant-level WGS, RNA-seq read, variant and clinical data are special category personal data, including when they leave the NHS site and when they are shared [IG-3]. Present pseudonymisation as a safeguard, not as a reason to drop controls [IG-3].

### Section 3.3 (also 2.1 and 6.4)

**Direct identifiers in the samplesheet break the pseudonymisation.** One sample ID, 'MNT-007_JH_1958-03-14', appears to contain initials and a date of birth [IG-6]. This contradicts the plan's claim that identities are known only to the clinical team [IG-6]. The sample information spreadsheet is also due for public deposit, so this would disclose identifiable special category data, and it may be a reportable breach [IG-6]. Remove the identifier from all copies, and check every other research-team record for leaked identifiers [IG-6]. Report the incident to the Information Governance Office within 24 hours [IG-6]. Add a check to the plan that the clinical team strips all direct identifiers before handover [IG-6]. Require identifier screening of any sample information file before deposit [IG-6].

### Section 3.4

**Consent limited to "this study" does not cover collaborator sharing, deposit or future use.** Several planned uses go beyond the consent described in section 3.4 [ETH-2]:
- sharing VCFs and clinical data with Calder University (USA) for a separate modifier-variant analysis;
- deposit of count tables and sample information in ArrayExpress;
- use of WGS to "support future analyses".

None of these is described to participants [ETH-2]. Revise the participant information sheet and consent form to describe each planned use [ETH-2]:
- international sharing with named collaborators and its purpose, including access through NSRE collaborator accounts if that route is adopted;
- repository deposit and access level;
- broad consent for future research on samples and data, with optional tiered consent items where appropriate.

Make sure the REC application covers all of these uses [ETH-2].

**There is no provision for participants who lose capacity during the study.** The study runs for 36 months, clinical data keep being extracted from NHS records, and participants with C9orf72 ALS are at recognised risk of cognitive decline [ETH-4]. The plan does not say what happens if a participant loses capacity [ETH-4]. Continued research use would need approval under the Mental Capacity Act and a consultee [ETH-4]. The alternative is withdrawal, with the data destroyed or anonymised [ETH-4]. State in the plan and the participant information sheet what will happen if a participant loses capacity [ETH-4]. One option is to seek NHS REC approval under sections 30 to 33 of the Mental Capacity Act, with consultee arrangements [ETH-4]. The other is to state that the participant will be withdrawn and what happens to their samples, iPSC lines and data [ETH-4]. Also say how capacity is assessed at recruitment [ETH-4].

### Section 3.5

**The blanket no-feedback policy for WGS findings is unjustified and has no pathway for significant findings.** Section 3.5 says participants "will not be informed of any findings" but gives no reason [ETH-3]. The plan does not say the policy will be explained during consent, and it sets out no process for a clinically significant or actionable finding [ETH-3]. This matters most for the six healthy controls [ETH-3]. They will have 30x WGS and could unknowingly carry pathogenic variants, including a C9orf72 expansion [ETH-3]. Write a justified feedback policy that weighs benefit and harm [ETH-3]. State it in the participant information sheet so participants know it before consenting, and define what happens if a clinically significant finding arises [ETH-3]. If any feedback will happen, describe a resourced pathway through the NHS clinical team and genetic counselling, including what controls would be told about their C9orf72 status [ETH-3].

### Section 4.2

**Working copies of record-level data are held outside the NSRE.** Section 4.2 keeps working copies of variant calls and clinical data on the group shared drive and an analysis workstation [TRE-1]. These data are Highly Confidential and may be held only in the NSRE [TRE-1]. Interactive convenience does not justify an exception [TRE-1]. The weekly shared-drive backup in section 4.4 would add further uncontrolled copies [TRE-1]. Delete section 4.2 and state that all interactive analysis of variant calls, clinical data and pre-release count tables takes place on the NSRE virtual desktop [TRE-1]. Remove the shared drive from section 4.4 for participant-level data [TRE-1]. Only output-checked summary results may be kept on group storage [TRE-1].

### Section 4.3

**The pipelines assume internet access that the NSRE does not have.** The plan says nf-core/rnaseq and nf-core/sarek will download reference genomes and containers from public repositories at run time [BIO-4, TRE-2]. The NSRE has no internet access, so the workflow as written will fail [BIO-4, TRE-2]. Fetching at run time also undermines reproducibility, because the exact reference and container used are not fixed [BIO-4]. Configure both pipelines to run offline [BIO-4, TRE-2]. Use imported Singularity or Apptainer images and a local reference bundle, brought in through the pre-approved catalogue or an NSRE software and reference data import request [BIO-4, TRE-2]. Name the GRCh38 and GENCODE files and any R or DESeq2 packages to import [TRE-2]. Record the checksums of imported containers and references in the project repository [BIO-4]. Allow five working days for each import in the timeline [TRE-2].

**Results leave the NSRE without airlock output checking.** Section 4.3 has "results files" copied out to the group's workstation and to collaborators "as needed", with no mention of the airlock or statistical disclosure control [TRE-3]. Every file leaving the NSRE must be checked first [TRE-3]. "Results files" could include record-level files, which can never go through the airlock [TRE-3]. Rewrite section 4.3 so that only summarised outputs leave the NSRE, all through the airlock with output checking [TRE-3]. Summarised outputs means figures, summary statistics and gene-level count tables [TRE-3]. Allow three working days for each release [TRE-3]. State that no record-level files leave by this route [TRE-3].

### Section 5.1

**There is no retention period or arrangement for preservation after the project.** Section 5.1 keeps data only "for the duration of the grant" and defers all retention decisions [STW-7]. The NSRE archive depends on a retention period stated in the plan [STW-7]. MRC and UKRI expect at least 10 years and expect archiving arrangements to be described at proposal stage [STW-7]. As written, nothing is guaranteed to survive the project [STW-7]. State what will be kept: raw reads, VCFs, the clinical extract, metadata and code [STW-7]. State where it will be kept, namely the NSRE archive plus EGA and ArrayExpress, and for how long [STW-7]. The minimum is 10 years after publication or study completion [STW-7]. Consider 20 years, since clinical data from NHS records are included, and confirm the sponsor's own policy [STW-7]. Name who reviews the data at the end of the retention period [STW-7].

### Section 6.1

**Raw WGS and RNA-seq reads are planned for open deposit in ENA.** Section 6.1 plans open-access deposit of WGS and RNA-seq FASTQ files in ENA [STW-1, IG-7, ETH-1]. Human genome sequences can identify the people they come from [STW-1, IG-7]. Public archives offer no access control, and open release cannot be undone [STW-1]. RNA-seq reads also carry genotype information [STW-1]. Publishing special category personal data to everyone cannot meet the safeguards required under Article 9(2)(j) [IG-7].

Open release also goes beyond the consent given, which covers use "for this study" only [IG-7, ETH-1]. Section 3.6 does not say the REC will be asked to approve public release [ETH-1]. Open release would also expose genetic information about participants' relatives [ETH-1].

The plan does not say how the files would leave the NSRE [TRE-5]. Sequence reads are record-level data, so they can never go through the airlock and must use the formal NSRE data release process [TRE-5].

Deposit raw reads, and any record-level genotype data, in the European Genome-phenome Archive under controlled access, using the NSRE data release route [STW-1, TRE-5]. State that any deposit of reads, alignments or variant calls is carried out by the NSRE team through that process, to a controlled-access archive [TRE-5]. Share participant-level sequence data only under controlled access with a data access committee [IG-7]. Name the committee and include independent members [STW-1]. State the data access agreement that requesters will sign [STW-1]. Cover controlled-access sharing in the DPIA and the transparency information [IG-7]. Panel members differ on whether open release could ever be acceptable (see Points of disagreement) [IG-7, ETH-1].

### Section 6.3

**The UK-US data bridge is unlikely to cover a transfer to Calder University.** The plan relies on the UK-US data bridge to send VCFs and clinical data to Calder University, Ohio [IG-4]. The bridge covers only US organisations that are FTC-regulated, have self-certified to the UK Extension and are on the DPF List [IG-4]. The FTC does not have jurisdiction over most non-profit organisations, which usually include universities [IG-4]. The plan gives no evidence that Calder is certified, so the transfer of special category data probably has no valid mechanism [IG-4]. Check whether Calder University is on the DPF List under the UK Extension, for non-HR data [IG-4]. If it is not, use an Article 46 safeguard (the IDTA, or the EU SCCs with the UK Addendum) plus a transfer risk assessment [IG-4]. Get Information Governance Office approval of the transfer mechanism [IG-4]. Better still, give the Calder collaborators NSRE accounts so that no data leave the UK [IG-4].

**VCF and clinical data would be sent to a US collaborator outside the NSRE release process.** The VCFs and clinical data planned for Calder University are record-level, Highly Confidential data [TRE-4]. They can leave only through the NSRE data release process, which requires three things [TRE-4]:
- an IGO-approved data sharing agreement;
- IGO approval of the transfer mechanism;
- a transfer carried out by the NSRE team.

The plan mentions none of these [TRE-4]. Preferably give the Calder collaborators NSRE accounts under a collaborator agreement, so they analyse the data inside the NSRE [TRE-4]. If a release is truly needed, describe the data release process [TRE-4]. That means an IGO-approved data sharing agreement, IGO approval of the transfer mechanism, and a transfer by the NSRE team using the secure transfer service [TRE-4].

### Section 7.2

**NSRE storage, archive and curation costs are not requested.** NSRE project storage is chargeable [STW-8, TRE-7]. It must be requested when the workspace is set up and costed in grant applications [STW-8, TRE-7]. Yet section 7.2 requests nothing and relies on an "existing allocation", which is not an NSRE project workspace [STW-8, TRE-7]. At a realistic volume of terabytes rather than 60 GB, project and archive storage have a material cost that cannot be absorbed informally [STW-8, TRE-7]. An NSRE allocation that is too small would create pressure to hold data on the shared drive, as section 4.2 already proposes [TRE-7]. Staff time for metadata curation, EGA and ArrayExpress submission, and access-committee work is also missing [STW-8].

Request an NSRE project workspace sized to the corrected volume, including pipeline scratch space [STW-8, TRE-7]. Cost project storage at £250 per TB per year for 36 months and NSRE archive storage at £60 per TB per year for the retention period, and state these figures in section 7.2 [STW-8, TRE-7]. For 1.3 to 2.5 TB of retained data, this comes to about £975 to £1,875 for project storage and about £780 to £1,500 for 10 years of archive [TRE-7]. Taking 2.5 TB of retained data plus working space, project storage costs at least £1,875 over 3 years [STW-8]. On the same basis, the archive costs £1,500 over 10 years or £3,000 over 20 years [STW-8]. Add staff time for curation, deposit and access management [STW-8]. MRC guidance 4.10 does not accept lack of resources as a reason not to share [STW-8].

## Minor issues

### Section 1.2

**Consent and approvals do not cover the creation, storage and future of the iPSC lines.** Section 1.2 creates a permanent iPSC line from each participant's skin biopsy [ETH-6]. The lines are renewable and can be shared, banked or used commercially [ETH-6]. Neither section 3.4 nor section 3.6 covers making the lines, storing them after the study, giving them to others, or what happens to them if a participant withdraws [ETH-6]. Add consent items covering iPSC derivation, long-term storage, sharing with other researchers or biobanks, any commercial use, and withdrawal [ETH-6]. Confirm that the approvals and tissue governance cover storage of the samples and lines beyond the study [ETH-6].

### Section 1.5

**Reference and analysis software versions are not specified.** "GRCh38 with GENCODE annotation" names neither the GENCODE release nor the GRCh38 assembly variant [BIO-5]. R, DESeq2 and package versions are not pinned [BIO-5]. Counts and variant calls depend on these choices, so the analysis cannot be reproduced exactly [BIO-5]. State the GENCODE release number and the exact GRCh38 FASTA, with checksums [BIO-5]. Pin the R and Bioconductor versions with renv or a container [BIO-5]. Record the nf-core release, Nextflow version and parameter files for each run [BIO-5].

**The WGS pipeline as specified will not confirm the C9orf72 repeat expansion.** The plan says WGS will "confirm genotypes" [BIO-8]. The defining genotype is a GGGGCC repeat expansion that standard short-read variant calling does not detect [BIO-8]. nf-core/sarek with its standard callers will therefore not confirm case status, and no alternative is named [BIO-8]. Name the method for confirming the expansion, such as a repeat-expansion caller on the WGS data and/or repeat-primed PCR [BIO-8]. Say how expansion status, line identity and genomic integrity will be confirmed in the iPSC lines [BIO-8].

### Section 2.1

**The samplesheet is incomplete and inconsistently formatted.** Section 2.1 says RNA quality and library details are recorded, but the samplesheet has no columns for RIN, library preparation, sex, age, clone or passage [STW-3, BIO-7]. MINSEQE element 1 requires these attributes [STW-3]. Without them, the 6 versus 6 comparison cannot be checked for imbalance or adjusted [BIO-7]. Harvest dates also differ within each batch, a sub-batch structure that is not recorded [BIO-7]. Categorical fields use inconsistent values [STW-3]. Dates mix ISO 8601 with '15/02/2028' for MNT-006 [STW-3, BIO-7]. File naming is inconsistent: MNT-003 has an uncompressed FASTQ, and MNT-011 has a file name containing a space [BIO-7]. These problems will fail validation or break parsing [BIO-7]. MNT-007's sample ID does not follow the study's coding scheme [BIO-7]. As planned for deposit in section 6.4, the record would be incomplete and error-prone [STW-3].

Build the deposit sample table from a MINSEQE-aligned template [STW-3]. Include sex, age band, disease status, cell type, clone, passage, differentiation batch, harvest date, RIN and library preparation batch [STW-3, BIO-7]. Use these columns in QC and as candidate covariates [BIO-7]. Use fixed-case controlled vocabularies, with ontology terms where available, and ISO 8601 dates [STW-3, BIO-7]. Gzip all FASTQs, remove spaces from file names and restrict sample IDs to study codes [BIO-7]. Validate the table before deposit, and release it only after NSRE output checking [STW-3].

### Section 3.4 (also 6.1 and 6.3)

**The transparency information does not cover the planned sharing and transfer.** The only information given to participants is consent for use "for this study" [IG-8]. The plan does not say that participants will be told about four things: the lawful basis, the transfer to the US, deposit in an archive, and the "future analyses" mentioned in the summary [IG-8]. Under UK GDPR, transparency information has to support all planned sharing [IG-8]. Write a privacy notice as part of the participant information [IG-8]. It should cover the controllers, the public task and Article 9(2)(j) basis, and the recipients, including Calder University in the US and the transfer safeguard [IG-8]. It should also cover controlled-access deposit, retention and participants' rights [IG-8].

### Section 3.5

**The implications of C9orf72 genotype data for relatives are not addressed.** WGS will confirm genotypes of a dominantly inherited expansion [ETH-5]. That information bears directly on blood relatives who have not consented [ETH-5]. The risk grows if the reads are released openly or shared overseas [ETH-5]. Neither the plan nor the consent process says what participants are told about these implications for their families [ETH-5]. Cover the implications for relatives in the participant information sheet: what genetic information is generated, who could see it, and what it may reveal about relatives [ETH-5]. Link this to the feedback policy and to any genetic counselling offered [ETH-5].

### Section 4.1

**The data classification is not recorded in the plan.** The plan does not give the classification of each data type [TRE-8]. WGS reads, BAMs, VCFs, clinical data and the sample spreadsheet are Highly Confidential [TRE-8]. Gene-level count tables become Confidential only after output checking [TRE-8]. Without these classifications, the plan treats derived files such as VCFs and count tables as if they could be held on group storage [TRE-8]. Add a table giving the classification of each data type and its permitted storage location under section 4 of the classification policy [TRE-8].

### Section 5.2

**The analysis code is kept only in the institutional GitLab, with no archived release or persistent identifier.** A working repository is not an archive, and it gives no persistent identifier to cite in a data access statement [STW-10]. This weakens provenance (FAIR R1.2) for the published analyses [STW-10]. At each publication, archive a tagged release of the code in a repository that issues DOIs [STW-10]. Record the pinned pipeline versions and containers, licence the code, and cite the DOI in the data access statement [STW-10].

### Section 6 (general)

**No licence or conditions of reuse are stated.** The plan gives no licence for the open processed data in ArrayExpress and no conditions of use for any controlled-access data [STW-6]. Without these, reusers do not know what they may do with the data, and the plan does not meet UKRI policy or FAIR R1.1 [STW-6]. State an open licence, such as CC BY 4.0 or CC0, for the summary-level counts and metadata [STW-6]. For data held in EGA, set out the conditions of use in a data access agreement [STW-6]. For example, limit use to the stated research purposes and prohibit re-identification [STW-6]. Licence the analysis code as well [STW-6].

**Clinical data and WGS variant calls have no deposit route and no reason given for not sharing them.** The study relates expression to clinical features [STW-9]. Section 6 gives no deposit route for the clinical data or the WGS variant calls, which are only sent to a US collaborator [STW-9]. Data needed to validate published findings must be shared, or the plan must explain why they cannot be [STW-9]. Deposit the clinical variables and VCFs with the raw data in EGA under controlled access, or give a specific justification for withholding them [STW-9].

### Section 6.1

**Release timing has no backstop, and the exclusive-use period is not justified.** Raw reads are released only "when the main results are published", with no latest date [STW-5]. The 12-month exclusive-use period in section 6.2 is asserted but not justified [STW-5]. It runs from an undefined "end of data generation" [STW-5]. If publication slips, deposit could be delayed indefinitely, contrary to UKRI policy [STW-5]. Give a fixed latest release date for every data set [STW-5]. That date must be no later than two years after the grant ends, which is January 2032 [STW-5]. Define the start date of exclusive use and justify its 12-month length [STW-5].

### Section 6.3

**The WGS design does not support the modifier-variant analysis.** Section 6.3 uses the WGS VCFs for a "joint analysis of C9orf72 modifier variants" [BIO-9]. Six carriers cannot support any genetic association analysis of modifiers [BIO-9]. The plan does not describe the combined cohort, the analysis or its power [BIO-9]. It is therefore unclear whether the WGS can answer this question, or whether the analysis can be reproduced [BIO-9]. Describe the joint analysis: the combined cohort size and the source of the Calder data [BIO-9]. Describe the joint-calling approach, for example gVCF-based joint genotyping on the same GRCh38 build and caller versions, and the phenotype and statistical method [BIO-9]. Alternatively, state that this cohort contributes only to a larger external effort and is not powered on its own [BIO-9].

### Section 6.4

**The processed-data and raw-data deposits are split and unlinked.** Processed counts go to ArrayExpress at the end of exclusive use, while raw reads go separately to ENA at publication [STW-4]. Neither section says how the two records will cross-reference each other [STW-4]. Through the standard ArrayExpress sequencing route, raw reads go into open ENA, so the controlled-access requirement could be breached by default [STW-4]. MINSEQE also expects raw and processed data to be linked through a sample-to-data table [STW-4]. State that the ArrayExpress/BioStudies record will hold only gene-level counts and non-identifying sample metadata, released through NSRE output checking [STW-4]. The record should cross-reference the EGA accession for the raw reads, and no reads should be submitted through ArrayExpress [STW-4]. Align the release dates of the two records [STW-4].

### Section 7.1

**Recruitment by the treating clinical team has no safeguards against undue influence, and control recruitment is not specified.** People with a terminal illness are recruited from the MND clinic by the clinical team that treats them [ETH-7]. The plan describes no safeguard against them feeling obliged to take part [ETH-7]. The plan also does not say how the six healthy volunteers are found [ETH-7]. The fairness of control recruitment and the risk of undue influence therefore cannot be assessed [ETH-7]. Describe how patients and controls will be recruited [ETH-7]. Where practicable, have someone other than the treating clinician take consent, and give participants enough time to decide [ETH-7]. State explicitly that declining will not affect their care [ETH-7]. Confirm that controls are not recruited from groups dependent on the research team [ETH-7].

## Points of disagreement

**Whether open release of sequence reads could ever be acceptable (section 6.1).** The information governance position is that WGS and RNA-seq reads should not be published openly at all [IG-7]. In this view, publishing special category personal data to everyone cannot meet the safeguards required under Article 9(2)(j) [IG-7]. The ethics position offers two options [ETH-1]. One is to remove open release of WGS and raw RNA-seq reads [ETH-1]. The other is to keep it, provided the deposit route and access level are set out in the participant information sheet and consent form and receive explicit REC approval [ETH-1]. The ethics position also states that controlled access is the more defensible option [ETH-1].

## Withdrawn during discussion

None.
