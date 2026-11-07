# Retail Revenue Forecasting (RMT3)

This repository contains the notebook and plotting scripts for a pilot study of retail sales and revenue forecasting on the M5 Forecasting Accuracy data.

## Files

- `RMT3 (4).ipynb` — data preparation, model fitting, and evaluation.
- `fig_models.py` and `fig_windows.py` — reproduce the figures used in the manuscript.
- `requirements.txt` — project dependencies and the versions recorded in the supplied notebook.
- `LICENSE` — MIT License for this repository's code.

## Environment

The notebook records Python 3.13.16, LightGBM 4.7.0, XGBoost 3.4.1, StatsForecast 2.1.1, pandas 2.2.3, and NumPy 2.1.3. The versions of Kaggle, SciPy, statsmodels, Matplotlib, and PyTorch were not recorded in the supplied run; those packages are listed without version pins in `requirements.txt`. Capture a fresh `pip freeze` from the actual Colab runtime before claiming an exact environment reproduction.

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Reproducing the pilot

1. Download the M5 Forecasting Accuracy competition files from Kaggle after accepting the competition data-use rules.
2. Open the notebook in Google Colab and set the data path to the downloaded sales, prices, and calendar files.
3. Run the notebook cells in order. The reported pilot used store `CA_1`, test window `W4`, and random seed `0`.
4. Run `fig_models.py` and `fig_windows.py` from the repository root to regenerate the figures.

The M5 data are not included in this repository and remain subject to Kaggle's competition rules.
