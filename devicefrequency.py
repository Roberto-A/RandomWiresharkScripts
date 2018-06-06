import csv

# differs from uniquedevices.py because this only includes,
# macs with word at the beginning.

# filename is name of Wireshark data file.
# returns dictionary {device_name: frequency}
def get_device_freq(filename):
    f = open(filename)
    reader = csv.DictReader(f)
    device_freq = {}

    for row in reader:
        device = row['Source'].partition('_')[0]
        add_device = True

        # If MAC has a word at the beginning
        # (Apple_59:29:98) put in frequency list.
        for c in device:
            if not c.isalpha():
                add_device = False
                break

        if add_device:
            device_freq[device] = device_freq.get(device, 0) + 1

    return device_freq

if __name__ == "__main__":
    import sys
    file = sys.argv[1]

    device_freq = get_device_freq(file)
    
    # If frequency is too small,
    # count as other.s
    min_frequency = 0
    other = 0

    # print(file)
    for k, v in device_freq.items():
        if v > min_frequency:
            print(k, ',', v)
        else:
            other += 1
    print('Other', ',', other)