import mne

data = mne.datasets.ssvep.data_path()

name = (
    data / "sub-02" / "ses-01" / "eeg" / "sub-02_ses-01_task-ssvep_eeg.vhdr"
)


raw = mne.io.read_raw_brainvision(name, preload=True)
raw.filter(l_freq=0.1, h_freq=None, fir_design="firwin", verbose=False)



raw.annotations.rename({"Stimulus/S255": "12hz", "Stimulus/S155": "15hz"})
tmin, tmax = -0.5, 20.0 



epochs = mne.Epochs(
    raw,
    event_id=["12hz", "15hz"],
    tmin=tmin,
    tmax=tmax,
    verbose=False,
)


tmin, tmax = 1.0, 20.0
fmin, fmax = 1.0, 90.0
sfreq = epochs.info["sfreq"]

spectrum = epochs.compute_psd(
    "welch",
    n_fft=int(sfreq * (tmax - tmin)),
    n_overlap=0,
    n_per_seg=None,
    tmin=tmin,
    tmax=tmax,
    fmin=fmin,
    fmax=fmax,
    window="boxcar",
    verbose=False,
)


spectrum.plot()
epochs.plot(block=True)
