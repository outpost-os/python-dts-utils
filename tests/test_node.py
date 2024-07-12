# SPDX-FileCopyrightText: 2023 - 2024 Ledger SAS
#
# SPDX-License-Identifier: Apache-2.0

# flake8: noqa

import pathlib
import dts_utils


def _get_dtsload() -> dts_utils.Dts:
    return dts_utils.Dts(pathlib.Path(__file__).parent.absolute() / "dts/sample.dts")


def test_node_id():
    dts = _get_dtsload()
    usart1 = dts.usart1
    assert usart1.label == "usart1"
    assert usart1.name == "serial@40013800"
