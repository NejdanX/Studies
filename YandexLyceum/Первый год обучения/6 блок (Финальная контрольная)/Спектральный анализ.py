def spectral_analysis(spectrum_dict, waves_list):
    ent = []
    for element in spectrum_dict.items():
        if all(val in waves_list for val in element[1]):
            ent.append(element[0])
    ent = sorted(ent)
    return ent
