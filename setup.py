from setuptools import setup, find_packages
setup(
    name="israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ",
    version="1.0.0",
    description="This dataset provides a comprehensive overview of Israel's economic impact over the last five years ",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/israel-economic-impact-database-2020-2024-key-indicators-main-factors-and-financ",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="cc0, citation, dataset, defense-spending, economic-impact, economics, fair-data, gdp, geopolitical-risk, inflation, israel, juan-moises-de-la-serna, macroeconomics, middle-east-economy, open-data, open-science, orcid, research, tech-sector, zenodo, zenodo, open-data",
)