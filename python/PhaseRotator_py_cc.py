#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr

class PhaseRotator_py_cc(gr.sync_block):
    """
    docstring for block PhaseRotator_py_cc
    """
    def __init__(self, phaseIncrease):
		gr.sync_block.__init__(self,
            name="PhaseRotator_py_cc",
            in_sig=[np.complex64],
			out_sig=[np.complex64])
		self.phaseIncrease = phaseIncrease
	
    def set_phaseIncrease(self, phaseIncrease):
        self.phaseIncrease = phaseIncrease

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0*np.exp(self.phaseIncrease*1j)
        return len(output_items[0])

