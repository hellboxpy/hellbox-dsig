# hellbox-dsig

A hellbox job that works with [digital signature tables](https://docs.microsoft.com/en-us/typography/opentype/spec/dsig).

## Usage

`InsertDummyDsig` adds a valid digital signature table to an OTF/TTF font file.

```python
from hellbox import Hellbox
from hellbox.jobs.dsig import InsertDummyDsig

with Hellbox("build") as task:
    source = task.read("./source/*.otf")
    source >> InsertDummyDsig() >> task.write("./build/otf")
```

## Installation

```sh
hell add hellbox-dsig
```

## Development

```sh
uv sync
uv run pytest
```
