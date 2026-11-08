# Retail Revenue Forecasting (RMT3)

This repository contains the notebook and plotting scripts for a pilot study of retail sales and revenue forecasting on the M5 Forecasting Accuracy data.

## Files

- `RMT3.ipynb` — data preparation, model fitting, and evaluation.
- `fig_models.py` and `fig_windows.py` — generate the manuscript figures from values embedded in the scripts.
- `requirements.txt` — pinned dependencies from the recorded Google Colab run.
- `LICENSE` — MIT License for the repository code.

## Environment

The recorded Colab environment used Python 3.13.16, Kaggle 2.2.5, LightGBM 4.7.0, XGBoost 3.4.1, StatsForecast 2.1.1, statsmodels 0.15.0, SciPy 1.18.1, pandas 2.2.3, NumPy 2.1.3, Matplotlib 3.10.0, and PyTorch 2.14.1+cu130 on a Tesla T4 GPU. All package versions are pinned in `requirements.txt`; the CUDA wheel source is included there for PyTorch.

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Reproducing the pilot

1. Accept the M5 Forecasting Accuracy competition data-use rules on Kaggle.
2. In Google Colab, add a secret named `KAGGLE_API_TOKEN` containing your Kaggle API token. Do not place the token in notebook code or commit it to the repository. An earlier public notebook revision contained a token; revoke it and replace it before relying on it.
3. Open `RMT3.ipynb` in Colab and run its cells in order. It downloads the competition files through the Kaggle API; the M5 data are not included here.
4. The article reports the pre-specified W4 holdout only (store `CA_1`, seed `0`). The notebook includes an optional W1–W4 exploratory run, disabled by default. Those post hoc results are disclosed separately and are excluded from the article's primary W4 conclusions.
5. Run `fig_models.py` and `fig_windows.py` from the repository root to regenerate the figures. Both scripts use values embedded in the files and do not require `preds.pkl` or `results_long.csv`.

## Exploratory four-window results

A later exploratory pass scored W1–W4. Direct LightGBM beat the units-times-price version in 2 of 4 windows. Its mean WRMSSE gain over ETS was 0.2%. For the matched-row hybrid comparison, changes were −0.6% on shock days and −1.2% on normal days. Diebold–Mariano p-values were 0.6651 for direct LightGBM versus units-times-price, 0.5390 for direct LightGBM versus ETS, and below 0.0001 for the hybrid versus its matched-row LightGBM control; Holm-adjusted values were 1.0000, 1.0000, and 0.0000. These post hoc summaries are disclosed for transparency and are not used for the article's W4-only conclusions.

The M5 data remain subject to Kaggle's competition rules.
