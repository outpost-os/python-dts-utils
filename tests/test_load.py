# SPDX-FileCopyrightText: 2023 - 2024 Ledger SAS
#
# SPDX-License-Identifier: Apache-2.0

# flake8: noqa

import pathlib
import dts_utils


def test_dtsload():
    dts = dts_utils.Dts(pathlib.Path(__file__).parent.absolute() / "dts/sample.dts")


def test_socload():
    dts = dts_utils.Dts(pathlib.Path(__file__).parent.absolute() / "dts/sample.dts")
    soc = dts.soc
