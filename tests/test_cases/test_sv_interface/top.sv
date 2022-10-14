// Copyright cocotb contributors
// Licensed under the Revised BSD License, see LICENSE for details.
// SPDX-License-Identifier: BSD-3-Clause

`timescale 1us/1us

interface sv_if();
  logic a;
  reg b;
  wire c;
endinterface

module sub_module (
  sv_if sv_if_p
);
endmodule

module top ();
  logic clock = 1'b0;
  sv_if sv_if_i();
  sub_module sub_module_inst(.sv_if_p(sv_if_i));
endmodule
