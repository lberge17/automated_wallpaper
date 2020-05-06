import subprocess
import time

def change_wallpaper(image):
    # change wallpaper on mac given an image
    command = """/usr/bin/osascript<<END
    tell application "Finder"
        set desktop picture to POSIX file "%s"
    end tell
    END"""
    subprocess.Popen(command%image, shell=True)
    subprocess.call(["killall dock"], shell=True)

def main(n):
    # automate change_wallpaper function
    # Note: be sure to edit path based on where your username and where files are stored
    change_wallpaper('/Users/laura/desktop/auto-wallpaper/images/'+str(n)+'.jpg')

n = 1
seconds = 20

while True:
    main(n)
    if n < 6:
        n += 1
    else:
        n = 1

    time.sleep(seconds)
