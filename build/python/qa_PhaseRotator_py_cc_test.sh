#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/vanwang/gnuradio/gr-tutorial/work/gr-SyncSignalMod/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/vanwang/gnuradio/gr-tutorial/work/gr-SyncSignalMod/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/vanwang/gnuradio/gr-tutorial/work/gr-SyncSignalMod/build/swig:$PYTHONPATH
/usr/bin/python2 /home/vanwang/gnuradio/gr-tutorial/work/gr-SyncSignalMod/python/qa_PhaseRotator_py_cc.py 
