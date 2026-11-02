# Metadata standards: FAIR principles and MINSEQE

**Digest of:**
- Wilkinson MD et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data 3, 160018. https://doi.org/10.1038/sdata.2016.18
- Functional Genomics Data Society (FGED), MINSEQE (Minimum Information about a high-throughput Sequencing Experiment): https://www.fged.org/projects/minseqe

Digest in the preparer's own words, checked against the sources on 29 October 2026.

## 1. FAIR principles relevant to metadata

The FAIR principles set out how to make data findable, accessible, interoperable and reusable. Those most relevant to metadata are:
- **F2:** data are described with rich metadata.
- **R1.1:** data and metadata are released with a clear and accessible data usage licence.
- **R1.2:** data and metadata are associated with detailed provenance.
- **R1.3:** data and metadata meet domain-relevant community standards.

## 2. MINSEQE

MINSEQE is a community standard setting out the minimum information needed to describe a high-throughput sequencing experiment, such as RNA-seq, so that others can interpret and reuse the data. It lists five elements:
1. A description of the biological system, the samples, and the experimental variables being studied.
2. The sequence read data for each assay, with base-level quality scores, ideally in FASTQ format.
3. The final processed or summary data for the assays in the study, with a description of their format.
4. General information about the experiment and the relationships between samples and data files, including a sample-to-data table.
5. The essential experimental and data processing protocols, from sample preparation and library construction to alignment, filtering and analysis.

## 3. Related requirements

UKRI policy requires shared data to carry adequate descriptive metadata and supporting documentation, and to be prepared to FAIR standards (see document 05).
