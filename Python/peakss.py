# %%
def get_peaks(data):
    dat = {"pos": [], "peak": []}
    for i in range(1, len(data)-1):
        if (data[i] > data[i-1]) and (data[i] > data[i+1]):
            dat["pos"].append(i)
            dat["peak"].append(data[i])
    return dat


peak = get_peaks([1, 2, 3, 4, 3, 4, 3, 6, 3, 2, 6, 7, 2])
print(peak)

#%%
print("Well Hello There")