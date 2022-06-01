import ROOT,os

# Load supera library by hand as it's not bound to python through PyROOT
import supera
ROOT.gSystem.Load(os.path.join(supera.get_lib_dir(),'libsupera.so'))

# Now load larnd2supera library
lib_path = os.path.dirname(__file__) + "/lib/"
inc_path = os.path.dirname(__file__) + "/include/"
ROOT.gSystem.Load(os.path.join(lib_path,'liblarnd2supera.so'))

from ROOT import larnd2supera

def get_includes():
    return inc_path

def get_lib_dir():
    return lib_path
