"""
===============================
Find global rejection threshold
===============================

This example demonstrates how to use :mod:`autoreject` to
find global rejection thresholds.
"""

# Author: Mainak Jas <mainak.jas@telecom-paristech.fr>
# License: BSD (3-clause)

###############################################################################
# Let us import the data using MNE-Python and epoch it.

import mne
from mne import io
from mne.datasets import sample

event_id = {'Visual/Left': 3}
tmin, tmax = -0.2, 0.5

data_path = sample.data_path()
raw_fname = data_path + '/MEG/sample/sample_audvis_filt-0-40_raw.fif'
event_fname = data_path + ('/MEG/sample/sample_audvis_filt-0-40_raw-'
                           'eve.fif')

raw = io.read_raw_fif(raw_fname, preload=True)
events = mne.read_events(event_fname)

include = []
picks = mne.pick_types(raw.info, meg=True, eeg=True, stim=False,
                       eog=True, include=include, exclude='bads')
epochs = mne.Epochs(raw, events, event_id, tmin, tmax,
                    picks=picks, baseline=(None, 0),
                    reject=None, verbose=False, detrend=1)

###############################################################################
# Now we get the rejection dictionary

from autoreject import get_rejection_threshold  # noqa
reject = get_rejection_threshold(epochs)

###############################################################################
# and print it

print('The rejection dictionary is %s' % reject)