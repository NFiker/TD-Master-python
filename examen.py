# -*- coding: utf-8 -*-
from psychopy import core, visual, event, data, gui
import csv, random, time

items = ["DD000","DD090","DD180","DD270","DU000","DU090","DU180","DU270","GD000","GD090","GD180","GD270","GU000","GU090","GU180","GU270"]
win = visual.Window([1366, 768], color = (256,256,256), fullscr = True, 
monitor="testMonitor")
datafile = open("FICHIER"+".csv","w")
writer = csv.writer(datafile, delimiter=";")

writer.writerow(["numero item",
    "nom item",
    "touche pressée",
    "accuracy",
    "RT",
    ])
    
compteur = 0
for j in range(4):
    random.shuffle(items)
    for i in range(len(items)):
        fix = visual.ImageStim(win, image = "fix.jpg")
        fix.draw()
        win.flip()
        core.wait(0.5)
        whitescreen = visual.ImageStim(win, image = "blanc.jpg")
        whitescreen.draw()
        win.flip()
        core.wait(0.5)
        image = visual.ImageStim(win, image = items[i]+".jpg")
        image.draw()
        win.flip()
        imageTime = time.time()
        key = event.waitKeys(2.000, ['s','k'])
        responseTime = time.time()
        if key == None:
            key=[]
            key.append("no key")
            cond = 0
        elif key[0] == 'k' and items[i][0] == "DD000" or "DD090" or "DD180" or "DD270" or "DU000" or "DU090" or "DU180" or "DU270":
            cond = 1
        elif key[0] == 's' and items[i][0] == "GD000" or "GD090" or "GD180" or "GD270" or "GU000" or "GU090" or "GU180" or "GU270":
            cond = 1
       
        else:
            cond = 0
        compteur += 1
        writer.writerow([compteur,
            items[i],
            key,
            cond,
            "{:.3f}".format(responseTime-imageTime),
            ])
            
        
event.clearEvents()
datafile.close()
win.close()
core.quit()

fixation = visual.ShapeStim(win, 
    vertices=((0, -0.5), (0, 0.5), (0,0), (-0.5,0), (0.5, 0)),
    lineWidth=5,
    closeShape=False,
    lineColor="red"
    )
fixation.draw(500) 
win.flip()


    


