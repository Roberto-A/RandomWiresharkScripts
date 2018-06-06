import csv


# filename is wireshark file.
# Returns a set of MAC addresses.
def get_unique_macs(filename):
    f = open(filename)
    reader = csv.DictReader(f)
    mac_set = set()

    for row in reader:
        mac_set.add(row['Source'])

    return mac_set


if __name__ == "__main__":
    import sys
    file = sys.argv[1]

    macs = get_unique_macs(file)

    print(file, ',', len(macs))


