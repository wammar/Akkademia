import setuptools

with open(file="README.md", mode="r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="akkadian",
    version="1.0.12",
    author="Gai Gutherz, Ariel Elazary",
    author_email="gaigutherz@gmail.com, am.elazary@gmail.com",
    description="Translating Akkadian signs to transliteration using NLP algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaigutherz/Akkademia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={'akkadian': ["output/bilstm_model_windows.pkl", "output/bilstm_model_linux.pkl",
                               "output/memm_model.pkl", "output/hmm_model.pkl"]},
    install_requires=[
        'allennlp==0.8.5',
    ],
)