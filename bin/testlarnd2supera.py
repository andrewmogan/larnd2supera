#!/usr/bin/env python3
from __future__ import print_function
import sys
from ROOT import TChain
from past.builtins import xrange
import larcv 
from larnd2supera import larnd2supera

proc = larnd2supera.SuperaDriver()

# TODO: How to modify this? Take larnd-sim packets?
ch = TChain('EDepSimEvents')
print('Adding input:', sys.argv[1])
ch.AddFile(sys.argv[1])
print("Chain has", ch.GetEntries(), "entries")
event_range=(0, min(ch.GetEntries(),1))
print('Processing', event_range[1] - event_range[0], 'events')
sys.stdout.flush()
print("step1")
for entry in xrange(*event_range):
    print("considering event:", entry)
    sys.stdout.flush()
    bytes = ch.GetEntry(entry)
    if bytes < 1: break
    ev = ch.Event
    proc.ReadEvent(ev)
