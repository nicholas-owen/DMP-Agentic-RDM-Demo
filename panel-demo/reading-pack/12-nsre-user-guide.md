# Northbridge Secure Research Environment (NSRE): user guide

| | |
|---|---|
| **Version** | 2.4 |
| **Owner** | Research Computing, University of Northbridge |
| **Issued** | June 2026 |

*The University of Northbridge and the NSRE are fictional. This guide was written for a training exercise.*

## 1. What the NSRE is

The NSRE is the University's trusted research environment for Highly Confidential research data, as defined in the Information Classification Policy. Users work through a virtual desktop, with access to analysis software and a high-performance computing partition inside the environment.

## 2. The Five Safes

The NSRE is run on the Five Safes framework:
- **Safe people:** only trained, approved users have access.
- **Safe projects:** each project is approved, with ethics approval and a completed DPIA where required.
- **Safe settings:** data are stored and analysed only inside the NSRE.
- **Safe data:** projects receive only the data they need, pseudonymised where possible.
- **Safe outputs:** everything leaving the NSRE is checked before release.

## 3. Getting access

Each project applies for an NSRE workspace. Every user must complete the NSRE training before their account is activated. External collaborators, including those overseas, can be given NSRE accounts under a collaborator agreement. This lets them work on the data inside the NSRE instead of receiving copies.

## 4. Working inside the NSRE

All storage and analysis of Highly Confidential data must take place inside the NSRE. Copies must not be made outside it, including working copies, temporary copies and derived record-level files such as variant calls or extracts of clinical data.

## 5. No internet access: importing software and reference data

The NSRE has no internet access. Software, containers, reference genomes and annotation files cannot be downloaded from inside the environment. They must be brought in through a software and reference data import request, which the NSRE team checks and installs within five working days.

A catalogue of pre-approved tools is already available, including common nf-core pipelines and their containers. Pipelines must be configured to run offline, using containers and reference files that have been imported.

## 6. Getting results out: output checking

Every file leaving the NSRE passes through the airlock, where two trained output checkers review it against the University's statistical disclosure control rules before release. Allow three working days.

Only summarised results, such as summary tables (including gene-level expression counts), figures and summary statistics, can be released through the airlock. Record-level data, including sequence reads, alignments, variant calls, individual genotypes and clinical records, are never released through the airlock.

## 7. Releasing record-level data

Record-level data can leave the NSRE only through the formal data release process. A release needs:
1. a data sharing agreement approved by the Information Governance Office;
2. for any recipient outside the UK, Information Governance Office approval of the legal transfer mechanism;
3. a transfer carried out by the NSRE team using the University's secure transfer service.

Researchers cannot transfer record-level data out of the NSRE themselves. Giving the recipient an NSRE account (section 3) is often quicker and safer than a release.

The NSRE team can also deposit approved data directly in a controlled-access archive, such as the European Genome-phenome Archive, through the data release process.

## 8. Storage, backup and charges

NSRE storage is backed up nightly. Project storage is charged at £250 per terabyte per year, including backup, and must be requested when the workspace is set up and costed in grant applications. When a project closes, its data are moved to the NSRE archive for the retention period stated in the project's data management plan. Archive storage is charged at £60 per terabyte per year.

## 9. Help

Contact the NSRE team through the Research Computing service desk.
