# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import cocotb


@cocotb.test()
async def test_sv_if(dut):
    """Test that signals in an interface are discovered and iterable"""

    dut.sv_if_i._discover_all()
    assert hasattr(dut.sv_if_i, "a")
    assert hasattr(dut.sv_if_i, "b")
    assert hasattr(dut.sv_if_i, "c")
    assert hasattr(dut.sv_if_i, "data")
    assert dut.sv_if_i.data.value == 0
    
    dut.sub_module_inst.sv_if_p._discover_all()
    assert hasattr(dut.sub_module_inst.sv_if_p, "a")
    assert hasattr(dut.sub_module_inst.sv_if_p, "b")
    assert hasattr(dut.sub_module_inst.sv_if_p, "c")
    assert hasattr(dut.sub_module_inst.sv_if_p, "data")
    assert dut.sub_module_inst.sv_if_p.data.value == 0
