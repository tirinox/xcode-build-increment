from __future__ import print_function
import os
import plistlib
import sys

def error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def usage():
    print("Usage:", os.path.basename(sys.argv[0]), "file1.plist file2.plist ...")


def increase_build(plist_name):
    try:
        with open(plist_name, 'rb') as fp:
            info = plistlib.load(fp)
            curr_build = int(info["CFBundleVersion"])
            print("Current build no:", curr_build)
            next_build = curr_build + 1
            print("Next build no:", next_build)
            info["CFBundleVersion"] = str(next_build)
            with open(plist_name, "wb") as fb_write:
                plistlib.dump(info, fb_write)
                print("OK!\n")
    except Exception:
        error("Error: can't process file", plist_name)


def main():
    if len(sys.argv) < 2:
        usage()
    else:
        plist_names = sys.argv[1:]
        for plist_name in plist_names:
            print("Increasing build number for file:", plist_name)
            increase_build(plist_name)


if __name__ == "__main__":
    main()