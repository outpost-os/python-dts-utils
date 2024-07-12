# SPDX-FileCopyrightText: 2023 - 2024 Ledger SAS
#
# SPDX-License-Identifier: Apache-2.0

# flake8: noqa

import pathlib
import dts_utils
import dts_utils.dump
import dts_utils.filters


def _get_dtsload() -> dts_utils.Dts:
    return dts_utils.Dts(pathlib.Path(__file__).parent.absolute() / "dts/sample.dts")


def test_dump():
    dts = _get_dtsload()
    usart1_info = dts_utils.dump.dump(dts, "usart1", True)
