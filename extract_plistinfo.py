import plistlib
import sys


def parse_plist(plist_file_name):

    with open(plist_file_name,'rb') as fp:
        plist = plistlib.load(fp)

        print('App name: ' + plist['CFBundleDisplayName'])
        print('Package: ' + plist['CFBundleIdentifier'])
        print('Version code: '  + plist['CFBundleShortVersionString'])
        print('Version bundle: ' + plist['CFBundleVersion'])
        print('Version platform: ' + plist['DTPlatformVersion'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_plistinfo <Info.plist>")
        sys.exit(1)

    plist_file_name = sys.argv[1]

    parse_plist(plist_file_name)
