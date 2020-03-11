"""
@author: J3ssie, M1ku, hanjyung
Simple FTP default cred testing v0.6

Written on Python 3.7.0 (W10)
Tested on Python 3.7.1 (Kali WSL, W10)
Should work on any Python 3.X installation.

Changelog:
    v0.6    Fixed output write html format.
    v0.5:   Fixed output write.
    v0.4:   Removed "ftp.txt" file.
            Added customized ftp file name.
            Added exception handlers.
    v0.3:   Fixed bugs.
    v0.2:   Added list support.
            Fixed '\n' bug.
    v0.1:   Initial release.
"""
import ftplib

i=0

def check_ftp():
    try:
        ftp = ftplib.FTP(c[i],'anonymous','', timeout=1)
        print('File List: ')
        files = ftp.dir()
        files2 = ftp.nlst()
        print('\n')
        print(files)
        for f in files2:
            result.write('- ' + f)
            result.write('\r')
    except ftplib.all_errors as error:
        print('Error: ',error)
        pass

print('Simple FTP anonymous cred testing v0.6 - ATHENA team')
print('')
print('[1]: Manual testing (manual input)')
print('[2]: Automatic testing (custom file)')
print('')
print('Save result .html file')
print('')
choice = input('Select your choice: ')

if choice == "1":
    target = input('Input IP/host: ')
    ftp = ftplib.FTP(target,'anonymous','', timeout=1)
    print('File List: ')
    files = ftp.dir()
    print('\n')
    print(files)
    print('Done. Quitting...')

elif choice == "2":
    name = input("Input list's name: ")
    result = input("Input results' name: ")
    with open(name) as a:
        b=a.readlines()
        
        c = [x.replace('\n','') for x in b ]
    
    result = open(result, 'w+')
    while i < len(c):
        print('\nTesting IP/host:',c[i])
        result.write('\r')
        result.write('<p>' + 'ftp://' + c[i] + '\r\n' + '</p>')
        check_ftp()
        i += 1
    result.close()
    print('Done. Quitting...')
else:
    print('Invalid choice. Quitting...')
