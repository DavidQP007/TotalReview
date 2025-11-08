from setuptools import setup, find_packages

setup(
    name="TotalReview",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.35.0",
        "pandas>=2.0.0",
        "biopython>=1.81",
        "tqdm>=4.66.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "PyYAML>=6.0",
        "requests>=2.31.0",
        "numpy>=1.24.0"
    ],
    entry_points={
        'console_scripts': [
            'totalreview=src.cli.main:main',
            'totalreview-screen=src.cli.screen:main',
            'totalreview-prisma=src.cli.prisma:main',
        ],
    },
    author="Tu nombre",
    author_email="tu.email@universidad.edu",
    description="Orquestador de IA open source para revisiones sistemáticas y metaanálisis",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tuusuario/TotalReview",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.8",
)