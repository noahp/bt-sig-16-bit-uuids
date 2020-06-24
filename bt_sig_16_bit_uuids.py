import sys
from dataclasses import dataclass
import bs4
import pprint
import re
import math
import argparse


@dataclass
class UuidEntry:
    """uuid data"""

    UUID: int
    Hexadecimal: str
    Company: str
    DateAllocated: str

    def bluez_fmt(self):
        """return bluez format"""
        tabs = "\t" * math.ceil((65 - 21 - len(self.Company)) / 8.0) or " "
        return f'\t{{ 0x{self.UUID:04x}, "{self.Company}"{tabs}}},'


def parse_html(htmlfile):
    """parse html file-like, return list of UuidEntry"""
    soup = bs4.BeautifulSoup(htmlfile, "html.parser")

    table = soup.find("table", attrs={"id": "table_3"})

    uuids = []
    for row in table.find_all("tr"):
        tds = row.find_all("td")
        if len(tds) == 4:

            tds = list(map(lambda x: x.text.strip(), tds))
            uuids.append(
                UuidEntry(
                    UUID=int(tds[0]),
                    Hexadecimal=f"0x{int(tds[1], 16):04}",
                    Company=tds[2],
                    DateAllocated=tds[3],
                )
            )

    # # sanity check; doesn't work with curl'd output
    # # <div class="dataTables_info" id="table_3_info" role="status" aria-live="polite">Showing 1 to 50 of 417 entries</div>
    # dataTableInfo = soup.find("div", attrs={"id": "table_3_info"})
    # assert dataTableInfo, "can't find data table info in html"

    # m = re.search(r".*?(\d+) entries", dataTableInfo.text)
    # entries_found = len(uuids)
    # info_count = int(m.group(1))
    # assert (
    #     entries_found == info_count
    # ), f"didn't find all entries: found {entries_found}, info lists: {info_count}"
    return uuids


def main():
    """cli entrance point"""
    parser = argparse.ArgumentParser(description="Parse bt sig 16 bit uuid html")
    parser.add_argument("infile", help="input html file path")
    args = parser.parse_args()

    with open(args.infile, "r") as htmlfile:
        uuids = parse_html(htmlfile)

    print("\n".join([x.bluez_fmt() for x in uuids]))


if __name__ == "__main__":
    main()
