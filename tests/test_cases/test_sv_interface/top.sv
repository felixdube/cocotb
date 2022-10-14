// Copyright cocotb contributors
// Licensed under the Revised BSD License, see LICENSE for details.
// SPDX-License-Identifier: BSD-3-Clause

`timescale 1us/1us

interface sv_if();
  logic a;
  reg b;
  wire c;
 
  `include "./sv_if_include.sv"

  modport source(
    output data
  );
endinterface

module sub_module (
  sv_if.source sv_if_p
);
endmodule

module top ();
  sv_if sv_if_i();
  sub_module sub_module_inst(.sv_if_p(sv_if_i));
endmodule
