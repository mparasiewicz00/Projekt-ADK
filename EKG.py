#Mateusz Parasiewicz WME19BC1S1
import wfdb
import pywt
import matplotlib.pyplot as mtpl
import wfdb.processing
import scipy
from scipy import signal

record = wfdb.rdrecord('ECGPCG0065', channels=[0])