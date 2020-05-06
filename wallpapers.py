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

def main():
    # automate change_wallpaper function

while True:
    main()
