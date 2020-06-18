# BT SIG Assigned Numbers UUID Parser

- [BT SIG Assigned Numbers UUID Parser](#bt-sig-assigned-numbers-uuid-parser)
  - [Install](#install)
  - [Usage](#usage)

Dump the BT SIG Assigned Numbers 16-bit UUID data.

Outputs in the form used by bluez c code:

```c
	{ 0xfdff, "OSRAM GmbH"					},
```

## Install

Requires python3.

You can run the `parse_uuids.py` script directly, eg `python parse_uuids.py`.

Or use something like pipx etc to install this.

```bash
# install the pipx tool
pip install pipx

#install this repo
pipx install .

which bt-sig-16-bit-uuids
 /home/npendleton/.local/bin/bt-sig-16-bit-uuids
# done
```

## Usage

You might run this like:

```bash
# curl the uuid list and feed it in
bt-sig-16-bit-uuids \
    <(curl https://www.bluetooth.com/specifications/assigned-numbers/16-bit-uuids-for-members/)
```
