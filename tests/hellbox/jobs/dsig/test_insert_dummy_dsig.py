from pathlib import Path

from fontTools import ttLib

from hellbox.source_file import SourceFile
from hellbox.jobs.dsig import InsertDummyDsig

FIXTURE = Path("tests/fixtures/blank/AdobeBlank.otf")


class TestInsertDummyDsig(object):
    def test_init(self):
        assert InsertDummyDsig()

    def test_flush_empty(self):
        assert InsertDummyDsig().flush([]) == []

    def test_process(self, tmp_path):
        source = SourceFile(FIXTURE, FIXTURE, tmp_path)
        result = InsertDummyDsig().process(source)
        assert result is not None
        font = ttLib.TTFont(result.content_path)
        assert font.getTableData("DSIG") == b"\x00\x00\x00\x01\x00\x00\x00\x00"
