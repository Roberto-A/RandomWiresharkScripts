import csv


# filename is csv file containing device name and frequency.
# This function combines the ones with similar names.
def combine_similar(filename):
    f = open(filename)
    reader = csv.DictReader(f)
    device_freqs = {}

    for row in reader:
        device = row['Device']
        device_freqs[device] = device_freqs.get(device, 0) + int(row['Freq'])

    return device_freqs

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    combined_freq = combine_similar(file)

    other = 0
    for k, v in combined_freq.items():
        if v > 10:
            print(k, '-', v)
        else:
            other += 1
    print('Other', ',', other)