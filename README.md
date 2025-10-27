# C-MAPSS Data Curation Pipeline

## Overview

Open-source alternative to Palantir Foundry for aviation predictive maintenance data curation. Demonstrates transparent, reproducible data transformations for turbofan engine degradation analysis using MLOps best practices (DVC + Weights & Biases).

### Project Goal
Transform NASA's C-MAPSS turbofan engine dataset from raw sensor readings into analysis-ready fact tables through a documented, version-controlled ETL pipeline that proves open-source tools can replace expensive proprietary platforms.

### Key Achievement
**$0 open-source stack** (DVC, W&B, Python) vs. **six-figure Palantir Foundry contracts** — same capabilities for data versioning, lineage tracking, and reproducible pipelines

## Dataset: NASA C-MAPSS

**C**ommercial **M**odular **A**ero-**P**ropulsion **S**ystem **S**imulation — multivariate time series data from simulated turbofan engine degradation.

| Dataset | Train Units | Test Units | Operating Conditions | Fault Modes |
|---------|------------|-----------|---------------------|-------------|
| **FD001** | 100 | 100 | 1 (Sea level) | 1 (HPC) |
| **FD002** | 260 | 259 | 6 | 1 (HPC) |
| **FD003** | 100 | 100 | 1 (Sea level) | 2 (HPC + Fan) |
| **FD004** | 248 | 249 | 6 | 2 (HPC + Fan) |

**Sensors**: 21 sensor measurements (temperature, pressure, speed, ratios) + 3 operational settings per time cycle

## Pipeline Architecture

### 1. Data Processing (Section 2)
- **Load & Parse**: Ingest 8 raw text files (4 train, 4 test) into structured DataFrames
- **Schema Validation**: Type checking, range validation, completeness assessment
- **Metadata Mapping**: Create unified fact table with global identifiers

### 2. Data Cleaning (Section 3)
- **Outlier Detection** (M6): Z-score, Hampel, Isolation Forest, LOF, Mahalanobis (5-method consensus)
- **Deduplication** (M6): Remove exact and entity-level duplicates across sensor readings
- **Data Version Control** (M9, M15): DVC tracking with MD5 hashes for 4 pipeline stages

### 3. MLOps Integration
- **DVC**: Version control for datasets (CSV files tracked via `.dvc` files)
- **Weights & Biases**: Experiment tracking, artifact lineage, 114 logged metrics
- **Public Dashboard**: [wandb.ai/djhavera-aviationscience/cmapss-data-loading](https://wandb.ai/djhavera-aviationscience/cmapss-data-loading)

## Repository Structure

```
fdc/
├── cmapss_final.pynb              # Main data curation notebook
├── cmapss_erd.html                # Entity-Relationship Diagram (Mermaid.js)
├── cmapss_ontology.ttl            # RDFS ontology (M5)
├── requirements.txt               # Python dependencies
├── .dvc/                          # DVC configuration
├── *.csv.dvc                      # DVC tracking files (4 pipeline stages)
├── fact_table/                    # Raw NASA C-MAPSS data files
│   ├── train_FD001.txt
│   ├── test_FD001.txt
│   ├── RUL_FD001.txt
│   └── ... (FD002-FD004)
└── wandb/                         # Weights & Biases run history
```

## Quick Start

### Prerequisites
```bash
# Python 3.8+
pip install -r requirements.txt
```

### Run the Pipeline
```bash
# Open the main notebook
jupyter notebook cmapss_final.pynb

# Or use JupyterLab
jupyter lab cmapss_final.pynb
```

### View Results
- **Notebook**: Step-by-step data transformations with inline documentation
- **ERD**: Open `cmapss_erd.html` in browser for interactive data model visualization
- **W&B Dashboard**: Track experiment metrics and artifact lineage online


## Data Citation

**Saxena, A., & Goebel, K. (2008).** *Turbofan Engine Degradation Simulation Data Set*. NASA Ames Prognostics Data Repository, NASA Ames Research Center, Moffett Field, CA.

## License

Academic project for CS598 Final Data Curation. Original NASA data maintains its public domain status.

---

**Author**: David Havera | CS598 FDC Final Project  
**Context**: Demonstrating open-source alternatives to Palantir Foundry for aviation data curation