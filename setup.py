from setuptools import setup

setup(
    name="bt-sig-16-bit-uuids",
    description="Parse bt sig uuid html page into bluez c data",
    py_modules=["parse_uuids"],
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "bt-sig-16-bit-uuids=parse_uuids:main",
        ]
    },
)
