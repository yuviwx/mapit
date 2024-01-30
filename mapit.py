import webbrowser, sys, pyperclip

sys.argv

if (len(sys.argv)) > 1:
    address = ' '.join(sys.argv[1:])
    print(sys.argv)
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open(r'https://www.google.com/maps/place/' + address)
