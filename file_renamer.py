#File renamer - script to automatize renaming files with given pattern.
#Author: Piotr Maślankowski, pmaslankowski@gmail.com

#Example of use:
#File to rename: House.of.Cards.S04E01.720p.WEBRip.5.1Ch.X264-KiMO.srt
#Input pattern: House.of.Cards.S04E[index].720p.WEBRip.5.1Ch.X264-KiMO.srt
#Output pattern: Episode [index].srt
#File will be renamed to Episode 1.srt

import os
import re

def pattern(pattern, filename):
    return False if re.match(pattern.replace("[index]", "[0-9]*"), filename) == None else True

def evalFilename(inPatt, outPatt, filename):
    i = inPatt.find("[index]")
    n = len(filename)
    curr = 0
    while i < n and filename[i].isdigit():
        curr = 10 * curr + int(filename[i])
        i += 1
    return outPatt.replace("[index]", str(curr))

def main():
    try:
        print("----------File renamer----------")
        path = input ("Enter directory path: ")
        inPattern = input ("Enter input pattern: ")

        files = [file for file in os.listdir(path) if pattern(inPattern, file)]
        size = len(files)

        print("Files which satisfies given pattern:")
        for file in files:
            print(file)
        print("( " + str(size) + " files found. )")

        outPattern = input ("Enter out pattern: ")

        os.chdir(path)
        for file in files:
            os.rename(file, evalFilename(inPattern, outPattern, file))

        input("Done. Renamed: " + str(size) + " files.")
    except FileNotFoundError as error:
        print(str(error))

if __name__ == "__main__":
    main()
