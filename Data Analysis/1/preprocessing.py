import scipy.io
import mne
import matplotlib.pyplot as plt




def process():
    mat_raw = scipy.io.loadmat("Data/P01_Ses1.mat")
    raw_array = mat_raw["data_ses1"][1:]

    ch_names = ["PO3", "POz", "PO4", "O1", "Oz", "O2", "02", "03", "04"]
    ch_types = ["eeg"] * 6 + ['misc'] * 2 + ['stim']

    info = mne.create_info(ch_names = ch_names, ch_types = ch_types, sfreq=512)
    info.set_montage("standard_1020")

    raw = mne.io.RawArray(raw_array, info)
    raw.pick_types(eeg=True)

    return raw 



def Hz_channels():
    mat_raw = scipy.io.loadmat("Data/P01_Ses1.mat")

    plt.plot(mat_raw["data_ses1"][0], mat_raw["data_ses1"][8])
    plt.plot(mat_raw["data_ses1"][0], mat_raw["data_ses1"][9] * 1e-6)
    plt.show()



Hz_channels()

raw = process()

raw = process()
raw.plot(block=True, scalings='auto')
