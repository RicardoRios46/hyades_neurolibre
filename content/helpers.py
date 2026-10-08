"""Output helpers for the analysis notebooks: static figures and results tables.

One source serves both outputs: the website uses the interactive figures and HTML tables, while the
Word/PDF/LaTeX exports use the static figure files (MyST `:placeholder:` with a `.*` extension, so each
export picks its format) and the Markdown tables.

Static figures are only written when the environment variable STATIC_FIGURE_FORMATS lists formats, e.g.
`png` (Word), `pdf` (LaTeX/journal) or `svg` (editable text, for Inkscape). Use the pixi task
`pixi run static-figures [png|pdf|svg]` (default png; a comma list such as png,svg writes several).
"""
import os

import matplotlib
import matplotlib.text
from matplotlib import font_manager

# Data folder (paths relative to content/, where the notebooks run). NeuroLibre and repo2data put the Zenodo record in
# data/<projectName>/ (binder/data_requirement.json); a plain download of the record into data/ works as well.
DATA_PROJECT_NAME = "hyades-tabular"
_DATA_ROOT = os.path.join("..", "data")
DATA_DIR = (os.path.join(_DATA_ROOT, DATA_PROJECT_NAME)
            if os.path.isdir(os.path.join(_DATA_ROOT, DATA_PROJECT_NAME)) else _DATA_ROOT)


def data_path(filename):
    """Path of a data file: data/hyades-tabular/<filename> if that folder exists, else data/<filename>."""
    return os.path.join(DATA_DIR, filename)


STATIC_FIGURE_DIR = os.path.join("..", "static", "figures")
STATIC_FIGURE_FORMATS = [f.strip().lower() for f in os.environ.get("STATIC_FIGURE_FORMATS", "").split(",") if f.strip()]
# Imaging Neuroscience asks for Arial or Helvetica in figures; Liberation Sans is metrically identical to Arial (Linux).
# Keep only installed fonts: matplotlib warns about every missing family in the list.
_PREFERRED_FONTS = ["Arial", "Helvetica", "Liberation Sans"]
_INSTALLED_FONTS = {f.name for f in font_manager.fontManager.ttflist}
FIGURE_FONTS = [f for f in _PREFERRED_FONTS if f in _INSTALLED_FONTS][:1] or ["DejaVu Sans"]


def save_static_figure(fig, label, folder=STATIC_FIGURE_DIR, dpi=200):
    """Save a matplotlib figure as <folder>/<label>.<format> for each format in STATIC_FIGURE_FORMATS.

    PNG is raster (for Word); PDF is vector (for LaTeX and the journal); SVG keeps text as text (for Inkscape).
    Files are written without timestamps, so re-running the notebooks does not change unchanged figures.
    """
    if not STATIC_FIGURE_FORMATS:
        return
    os.makedirs(folder, exist_ok=True)
    for text in fig.findobj(matplotlib.text.Text):
        text.set_fontfamily(FIGURE_FONTS)
    for ext in STATIC_FIGURE_FORMATS:
        path = os.path.join(folder, f"{label}.{ext}")
        if ext == "png":
            fig.savefig(path, dpi=dpi, bbox_inches="tight")
        elif ext == "pdf":
            fig.savefig(path, bbox_inches="tight", metadata={"CreationDate": None})
        elif ext == "svg":
            with matplotlib.rc_context({"svg.fonttype": "none"}):
                fig.savefig(path, bbox_inches="tight", metadata={"Date": None})
        else:
            raise ValueError(f"Unsupported static figure format: {ext}")


def display_table(df):
    """Display a results table as HTML (website) and Markdown (Word/PDF/LaTeX exports)."""
    from IPython.display import display
    display({"text/html": df.to_html(index=False),
             "text/markdown": df.to_markdown(index=False),  # requires the tabulate package
             "text/plain": df.to_string(index=False)}, raw=True)
