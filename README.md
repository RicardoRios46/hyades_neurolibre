# HYADES MyST Preprint

This repository contains the source for the manuscript *"Probing gray matter microstructure differences in neurodegenerative dementia using b-tensor encoding diffusion MRI"* (preprint on NeuroLibre; DOI to be added). It includes the manuscript source and the reproducible analysis notebooks written using [MyST Markdown](https://mystmd.org).

## Related repositories

This paper is part of a set of four linked repositories:

| Repository | Contents | Hosted on |
|---|---|---|
| **HYADES preprint** (this repository) | Manuscript source, reproducible analysis notebooks, MyST build | GitHub |
| [HYADES tabular data](https://doi.org/10.5281/zenodo.23212234) | CSV/TSV data files with the data required to reproduce the paper | Zenodo |
| HYADES imaging preprocessed data (released on FRDR at journal publication) | Preprocessed, de-identified NIfTI imaging derivatives (brain-extracted anatomicals, preprocessed dMRI, MTS source volumes, segmentations, masks) | FRDR |
| [HYADES processing pipeline](https://github.com/RicardoRios46/hyades_snakemake) | Snakemake workflow that generates the data from raw BIDS MRI data | GitHub |

## Repository structure

```
.
├── binder/           # NeuroLibre/Binder runtime configuration
│   ├── environment.yml       # Conda environment pinned to pixi.lock (pixi run binder-env)
│   ├── pin_environment.py    # Pins environment.yml to the linux-64 versions in pixi.lock
│   └── data_requirement.json # repo2data download specification
├── content/          # Reproducible analysis notebooks
├── data/             # CSV/TSV data files (not included; download from Zenodo, see Data)
├── static/           # Images and static assets
│   └── figures/      # Static figure versions for Word or editing (generated, not tracked)
├── myst.yml          # MyST project configuration
├── paper.md          # Main manuscript file
├── supplementary.md  # Supplementary material
├── paper.bib         # Bibliography
├── pixi.toml         # Pixi environment/dependency specification
└── pixi.lock         # Locked dependency versions
```

## Getting started

### 1. Install Pixi

This project uses [Pixi](https://pixi.sh) to manage the Python environment and dependencies. If you don't have Pixi installed, run:

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Restart your shell (or source your shell config file) so the `pixi` command is available:

```bash
source ~/.bashrc   # or ~/.zshrc, depending on your shell
```

### 2. Clone the repository

```bash
git clone https://github.com/RicardoRios46/hyades_neurolibre.git
cd hyades_neurolibre
```

### 3. Download the data

The CSV/TSV data files are not part of this repository. Download them from Zenodo into `data/hyades-tabular/` (or directly into `data/`); see [Data](#data).

### 4. Install the environment

Pixi reads `pixi.toml` and `pixi.lock` to create a reproducible environment with all dependencies needed to build the paper and run the analysis notebooks:

```bash
pixi install
```

### 5. Activate the environment

```bash
pixi shell
```

This drops you into a shell with the project's Python environment (and all notebook dependencies) active. Alternatively, you can run individual commands without entering a subshell using `pixi run <command>`.

`binder/environment.yml` is the same environment for NeuroLibre/Binder (which don't read `pixi.toml`), with each dependency pinned to the linux-64 version in `pixi.lock`. Regenerate it with `pixi run binder-env` after changing dependencies instead of editing it by hand.

### 6. Build the paper with MyST

With the environment active, build the manuscript using:

```bash
myst build
```

To preview the paper locally in the browser with live reload:

```bash
myst start
```

> **Windows:** run all notebook-related tasks (`run-notebooks`, `static-figures`) from PowerShell or Command Prompt, not Git Bash. In Git Bash, rpy2 can't locate R and fails to import.

## Data

The data are **not included in this repository**. Download them from the [HYADES tabular data repository](https://doi.org/10.5281/zenodo.23212234) (Zenodo) and place the files in **one** of these folders at the root of this repository:

- `data/hyades-tabular/`: the layout NeuroLibre uses (repo2data downloads the Zenodo record there, as set in `binder/data_requirement.json`)
- `data/`: directly in the data folder

The notebooks read the files from `data/hyades-tabular/` if that folder exists, otherwise from `data/`. They need these files:

- `participants.tsv`
- `exclusion_list.csv`
- `hyades_hippunfoldAD_surfmetrics.csv`
- `hyades_hippunfoldAD_volumes_normalized.tsv`
- `hyades_wholeBrain_ROIs.csv`

Full descriptions of each file and column are in the README of the tabular data repository. These CSV/TSV files are summary dataframes computed from the underlying NIfTI imaging derivatives (preprocessed volumes, segmentations, masks), which will be published separately in the HYADES imaging preprocessed data repository (released on FRDR at journal publication).

## Reproducible analysis

The `content/` folder contains three Jupyter notebooks that reproduce the analyses and figures reported in the paper. All dependencies required to run these notebooks are included in the Pixi environment — no separate setup is required. This includes Python (pandas, NumPy, SciPy, statsmodels, seaborn, plotly, and tabulate to render tables as Markdown), R with the packages `car`, `effectsize` and `marginaleffects` (called from Python through rpy2), and the Jupyter tools (`nbconvert`, `jupyter_server`) used by `pixi run run-notebooks` and `myst build --execute`.

| Notebook | Description |
|---|---|
| `demographics.ipynb` | Summarizes participant demographics and generates descriptive statistics/tables |
| `section1_wholebrain.ipynb` | Whole-brain analysis reported in Section 1 of the paper |
| `section2_hippocampus.ipynb` | Hippocampal subfield analysis reported in Section 2 of the paper |

To re-run all analysis notebooks (their outputs are written back into the notebooks and embedded in the paper):

```bash
pixi run run-notebooks
```

This re-runs the analyses only; it doesn't write static figures.

### Static figures

The paper website uses the interactive figures from the notebooks; MyST doesn't use static figures. For pasting into Word or for editing, static versions can be written to `static/figures/` (not tracked in git; reproduced from code) on demand:

```bash
pixi run static-figures       # PNG (default)
pixi run static-figures pdf   # PDF (vector)
pixi run static-figures svg   # SVG with editable text, for post-processing (e.g. in Inkscape)
```

To work with the notebooks interactively, open `content/` in an editor with Jupyter support (e.g. VS Code) using the Pixi environment, or add JupyterLab with `pixi add jupyterlab` and run `pixi run jupyter lab content/`.

Each notebook reads the data from `data/hyades-tabular/` or `data/` (see [Data](#data) for how to download them) and reproduces the figures and statistical results included in the manuscript.

## Citation

If you use this work, please cite:

```bibtex
@misc{rioscarrillo_hyades_2026,
  title  = {Probing gray matter microstructure differences in neurodegenerative dementia using b-tensor encoding diffusion {MRI}},
  author = {Rios-Carrillo, Ricardo and Malik, Rubina and So, Isis and Moon, Kyeongrim and Khan, Ali R. and Finger, Elizabeth and Baron, Corey A.},
  year   = {2026},
  note   = {Preprint on NeuroLibre; DOI to be added},
  url    = {https://github.com/RicardoRios46/hyades_neurolibre},
}
```

## License

This repository uses a split license (see [LICENSE](./LICENSE) for the full terms):

| Part | License |
|---|---|
| Code: analysis notebooks, scripts, build and environment configuration (`content/*.ipynb`, `*.py`, `myst.yml`, `pixi.toml`, `pixi.lock`, and other build/environment configuration files) | [MIT](https://opensource.org/license/mit) |
| Manuscript content: text, figures, bibliography (`paper.md`, `supplementary.md`, `static/`, `paper.bib`) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

The data used by the notebooks are not included here and are licensed separately in the [HYADES tabular data repository](#data).
