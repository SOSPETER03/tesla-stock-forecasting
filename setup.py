from setuptools import setup, find_packages

setup(
    name='tesla_stock_forecasting',
    version='0.1.0',
    description='Advanced Time Series Forecasting of Tesla Stock using Classical, Seasonal, and Deep Learning Models',
    author='Sospeter Njenga Wainaina',
    author_email='sospeternjenga03@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'plotly',
        'statsmodels',
        'pmdarima',
        'tensorflow',
        'keras',
        'scikit-learn',
        'yfinance'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
