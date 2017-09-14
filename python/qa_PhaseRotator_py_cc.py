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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from PhaseRotator_py_cc import PhaseRotator_py_cc
import numpy as np

class qa_PhaseRotator_py_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
		src_data = (1+1j, 2+0j, 3+4j, 5+7j)
		expected_result = (1-1j, 0-2j, 4-3j, 7-5j)
		src = blocks.vector_source_c(src_data)
		phin = PhaseRotator_py_cc(-np.pi/2)
		snk = blocks.vector_sink_c()
		self.tb.connect(src, phin)
		self.tb.connect(phin, snk)
		self.tb.run()
        # check data
		result_data = snk.data()
		self.assertFloatTuplesAlmostEqual(expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_PhaseRotator_py_cc, "qa_PhaseRotator_py_cc.xml")
