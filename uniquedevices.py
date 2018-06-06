import csv


# filename is wireshark file.
# Returns {device: frequency} dictionary.
def get_device_freq(filename):
    f = open(filename)
    reader = csv.DictReader(f)
    device_freq = {}

    for row in reader:
        device = row['Source']

        # Filter out IPs
        if not valid_ip(device):
            device_freq[device] = device_freq.get(device, 0) + 1

    return device_freq

def valid_ip(ip):
    try:
        ip = ip.split('.')
        valid = [int(b) for b in ip]
        valid = [b for b in valid if b >= 0 and b <= 255]
        return len(ip) == 4 and len(valid) == 4
    except:
        return False


if __name__ == "__main__":
    import sys
    file = sys.argv[1]

    devices = get_device_freq(file)

    print(file, ',', len(devices))

    # min_freq = 500
    # other = 0
    # for k, v in devices.items():
    #     if v > min_freq:
    #         print(k, ',', v)
    #     else:
    #         other += 1

    # print('Other', ',', other)

