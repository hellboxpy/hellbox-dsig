from typing import Any, cast

from fontTools import ttLib
from hellbox import Chute, Hellbox


class InsertDummyDsig(Chute):
    """InsertDummyDsig adds a valid DSIG table with no signatures."""

    def process(self, file):
        Hellbox.info(f"Updating DSIG: {file.name}")

        copy = file.copy()

        font = ttLib.TTFont(copy.content_path)
        font.tables[cast(Any, "DSIG")] = self._create_signature()
        font.save(copy.content_path)

        return copy

    def _create_signature(self):
        table = cast(Any, ttLib.newTable("DSIG"))
        table.ulVersion = 1
        table.usFlag = 0
        table.usNumSigs = 0
        table.signatureRecords = []
        return table
