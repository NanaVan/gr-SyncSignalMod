# gr-SyncSignalMod
Test for phase shift for Comb signal step by step

## Block for phase rotator
code: /python/PhaseRotator_py_cc.py

      input/output: complex/complex

      setter function: set_phaseIncrease(phaseChange)

      work function: multiply exp(ij * phaseChange)

test: /phython/qa_PhaseRotator_py_cc.py

## Steps for test
grc: /work
1. ~~PhaseRotator: Comparing two cosine waves' specturm (one with phase rotator)~~^{\%}
2. SignalGenerator: Geting an impulse train from square wave
3. TestForSpectrum: Comparing two sine waves' spectrum (one with phase rotator)^{\#\*}
4. CombSignalRotator: Comparing two impulse trains' specturm (one with phase rotator)^{\#\*}
5. CombSignalDelay: Comparing two impulse trains' specturm (one with sample delay)^{\#}
\% No use
\# Showed in Report
\* Using the -Mo.py version, since the phase rotator setter function cannot be automatically added into GUI display.
   Put `self.SyncSignalMod_PhaseRotator_py_cc_x.set_phaseIncrease(phaseChange)` after `self.phaseRotate = phaseRotate`

## Summer school report
WQ - report: All work done in 2017 Summer School
