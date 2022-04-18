# %%
def get_peaks(data):
    for i in range(1, len(data)-1):
        peaks_x = []
        if (data[i] > data[i-1]) and (data[i] > data[i+1]):
            peaks_x.append(i)
    return peaks_x


# %%
peaks_x = get_peaks(x)
