# BT SIG Assigned Numbers UUID Parser

- [BT SIG Assigned Numbers UUID Parser](#bt-sig-assigned-numbers-uuid-parser)
  - [Usage](#usage)

Dump the BT SIG Assigned Numbers 16-bit UUID data.

Outputs in the form used by bluez c code:

```c
	{ 0xfdff, "OSRAM GmbH"					},
```

## Usage

You might run this like:

```bash
# curl the uuid list and feed it in
python3 bt_sig_16_bit_uuids.py \
    <(curl https://www.bluetooth.com/specifications/assigned-numbers/16-bit-uuids-for-members/)
```
