import uniquemacs


# file0 & file1 are Wireshark files.
# Returns common set of mac addresses.
def get_common_users(file0, file1):
    mac0 = uniquemacs.get_unique_macs(file0)
    mac1 = uniquemacs.get_unique_macs(file1)
    return mac0 & mac1


if __name__ == "__main__":
    import sys
    file0 = sys.argv[1]
    file1 = sys.argv[2]

    users = get_common_users(file0, file1)
    print(file0, '-', file1)
    print(len(users))
    # for user in users:
    #     print(user)