import argparse
import os.path
from ctypes import windll, create_unicode_buffer, WinError,  HRESULT
from ctypes.wintypes import BOOL, LPCWSTR
import winreg

# Define the function prototypes
wer = windll.wer
WerAddExcludedApplication = wer.WerAddExcludedApplication
WerAddExcludedApplication.argtypes = [LPCWSTR, BOOL]
WerAddExcludedApplication.restype = HRESULT

WerRemoveExcludedApplication = wer.WerRemoveExcludedApplication
WerRemoveExcludedApplication.argtypes = [LPCWSTR, BOOL]
WerRemoveExcludedApplication.restype = HRESULT

def check_wer_exclusion(exe_name):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\Windows Error Reporting\ExcludedApplications", 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, exe_name)
            return value == 1
    except FileNotFoundError:
        return False
    except OSError:
        return False

def add_excluded_application(exe_name):
    if check_wer_exclusion(exe_name):
        print(f"{exe_name} is already in the WER exclusion list.")
        return
    print(f"Adding {exe_name} to the WER exclusion list.")
    all_users=False
    hr = WerAddExcludedApplication(create_unicode_buffer(exe_name), BOOL(all_users))
    if hr != 0:
        raise WinError(hr)
    print(f"Success.")

def remove_excluded_application(exe_name):
    if not check_wer_exclusion(exe_name):
        print(f"{exe_name} is not in the WER exclusion list.")
        return
    print(f"Removing {exe_name} from the WER exclusion list.")
    all_users=False
    hr = WerRemoveExcludedApplication(create_unicode_buffer(exe_name), BOOL(all_users))
    if hr != 0:
        raise WinError(hr)
    print(f"Success.")

def main():
    try:
        parser = argparse.ArgumentParser(description='Manage the WER exclusion list.')
        parser.add_argument('action', choices=['add', 'remove'], help='Action to perform (add or remove).')
        parser.add_argument('exe_name', help='Name of the executable to exclude from WER.')

        args = parser.parse_args()

        # Strip any path off the executable name; it should only be filename.ext
        args.exe_name = os.path.basename(args.exe_name)

        if args.action == 'add':
            add_excluded_application(args.exe_name)
        elif args.action == 'remove':
            remove_excluded_application(args.exe_name)
        exit(0)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
