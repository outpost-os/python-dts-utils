# SPDX-FileCopyrightText: 2023 - 2024 Ledger SAS
#
# SPDX-License-Identifier: Apache-2.0

# flake8: noqa

import pathlib
import dts_utils
import dts_utils.filters


def _get_dtsload() -> dts_utils.Dts:
    return dts_utils.Dts(pathlib.Path(__file__).parent.absolute() / "dts/sample.dts")


def test_filter_enabled():
    dts = _get_dtsload()
    pinctrl_list = dts_utils.filters.f_peripherals(dts.soc.pinctrl)
    enabled_gpios = dts_utils.filters.f_enabled(pinctrl_list)
    assert len(enabled_gpios) == 7


def test_filter_enabled_exceptions():
    dts = _get_dtsload()
    try:
        enabled_gpios = dts_utils.filters.f_enabled(dts)
        assert False
    except dts_utils.exceptions.InvalidTemplateValueType:
        assert True


def test_filter_owner():
    dts = _get_dtsload()
    i2c1 = dts.i2c1
    assert dts_utils.filters.f_owner(i2c1) == 0xBABE


def test_filter_owner_exceptions():
    dts = _get_dtsload()
    try:
        enabled_gpios = dts_utils.filters.f_owner(dts)
        assert False
    except dts_utils.exceptions.InvalidTemplateValueType:
        assert True


def test_filter_has_property():
    dts = _get_dtsload()
    i2c1 = dts.i2c1
    assert dts_utils.filters.f_has_property(i2c1, "outpost,owner")


def test_filter_has_property_exception():
    dts = _get_dtsload()
    try:
        dts_utils.filters.f_has_property(dts, "outpost,owner")
        assert False
    except dts_utils.exceptions.InvalidTemplateValueType:
        assert True


def test_filter_with_property():
    dts = _get_dtsload()
    dev_list = dts_utils.filters.f_peripherals(dts.root)
    assert len(dts_utils.filters.f_with_property(dev_list, "outpost,owner")) == 1


def test_filter_with_property_exception():
    dts = _get_dtsload()
    try:
        dts_utils.filters.f_with_property(dts, "outpost,owner")
        assert False
    except dts_utils.exceptions.InvalidTemplateValueType:
        assert True
    try:
        dts_utils.filters.f_with_property(dts.usart1, "outpost,owner")
        assert False
    except dts_utils.exceptions.InvalidTemplateValueType:
        assert True
