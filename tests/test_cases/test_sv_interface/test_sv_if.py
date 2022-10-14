# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause

import cocotb
from cocotb_bus.monitors import BusMonitor

class bfm(BusMonitor):
    _signals = ["a"]
    def __init__(self, *args, **kwargs):
        BusMonitor.__init__(self, *args, **kwargs)
        assert self.bus.a is not None

    async def _monitor_recv(self):
        pass

@cocotb.test()
async def test_sv_if(dut):
    """Test that signals in an interface are discovered and iterable"""

    my_bfm1 = bfm(entity=dut.sv_if_i, clock=dut.clock, name="") 
    my_bfm2 = bfm(entity=dut.sub_module_inst.sv_if_p, clock=dut.clock, name="")

    dut.sv_if_i._discover_all()
    assert hasattr(dut.sv_if_i, "a")
    assert hasattr(dut.sv_if_i, "b")
    assert hasattr(dut.sv_if_i, "c")
    
    dut.sub_module_inst.sv_if_p._discover_all()
    assert hasattr(dut.sub_module_inst.sv_if_p, "a")
    assert hasattr(dut.sub_module_inst.sv_if_p, "b")
    assert hasattr(dut.sub_module_inst.sv_if_p, "c")
