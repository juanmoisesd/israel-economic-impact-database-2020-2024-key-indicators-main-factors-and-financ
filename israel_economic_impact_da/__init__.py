"""This dataset provides a comprehensive overview of Israel's economic impact over the last five years 
DOI: https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ | GitHub: https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). This dataset provides a comprehensive overview of Israel's economic impact over . Zenodo. https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ'
def info(): print(f"Dataset: This dataset provides a comprehensive overview of Israel's economic impact over \nDOI: https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ\nGitHub: https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ")