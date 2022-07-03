import os
import shutil

desktopPath="C:\\Users\\morel\Desktop\\"
publicDesktopPath="C:\\Users\\Public\\Desktop"

filesNotToMove=["all","cleaner.py"]
toPath=desktopPath+"all\\"

#all files in the desktop folder
allFilesInDesktopPath=os.listdir(desktopPath)
allFilesInPublicDesktopPath=os.listdir(publicDesktopPath)

#move everything to all except links
for file in allFilesInDesktopPath:
    if file not in filesNotToMove:
        try:
            shutil.move(desktopPath+file,toPath+file)
        except Exception as e:
            print(e)
            print("Could not move "+file)
            continue

#remove links
for file in allFilesInPublicDesktopPath:
    try:
        os.remove(publicDesktopPath+"\\"+file)
    except:
        print("Could not remove "+file)
        continue

