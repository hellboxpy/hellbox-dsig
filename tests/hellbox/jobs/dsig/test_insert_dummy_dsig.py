from fontTools import ttLib

from hellbox.source_file import SourceFile
from hellbox.jobs.dsig import InsertDummyDsig


class TestGenerateOtf(object):
    def test_init(self):
        assert InsertDummyDsig()

    def test_run_without_files(self):
        assert InsertDummyDsig().run([]) == []

    def test_run(self):
        source = SourceFile("AdobeBlank.otf", "./tests/fixtures/blank/AdobeBlank.otf")

        result = InsertDummyDsig().run([source])
        assert len(result) is 1

        font = ttLib.TTFont(result[0].content_path)
        assert font.getTableData("DSIG") == b'\x00\x00\x00\x01\x00\x00\x00\x00'