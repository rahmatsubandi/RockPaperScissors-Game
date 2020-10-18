import cv2
import numpy as np
import random
import threading


l = []


def generate():
    D = {0: "stone", 1: "paper", 2: "scissors"}
    x = random.randint(0, 2)
    threading.Timer(2, generate).start()
    l.append((D[x]))
    # print(D[x])


generate()

stone_cascade = cv2.CascadeClassifier('./xml/fist.xml')
paper_cascade = cv2.CascadeClassifier('./xml/palm.xml')
sci_cascade = cv2.CascadeClassifier('./xml/fingers.xml')
none_cascade = cv2.CascadeClassifier('./xml/none.xml')

cap = cv2.VideoCapture(0)
count_s = 0
count_p = 0
count_sc = 0
count_n = 0
c_win = 0
c_lose = 0
c_tie = 0
while True:

    ret, img = cap.read()
    img = img[100:500, 100:500]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stone = stone_cascade.detectMultiScale(gray, 1.1, 5)
    paper = paper_cascade.detectMultiScale(gray, 1.2, 5)
    scissors = sci_cascade.detectMultiScale(gray, 1.1, 150)
    none = none_cascade.detectMultiScale(gray, 1.1, 1)

    for(x, y, w, h) in stone:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        count_s += 1
        if(count_s == 1):
            # print("stone-user")
            count_p = 0
            count_n = 0
            count_sc = 0
            cv2.destroyWindow('none')
            if(l[len(l)-1] == "scissors"):
                img1 = cv2.imread("./img/scissors.jpg")
                cv2.imshow('S_P', img1)
                print("Kamu Menang!")
                c_win += 1
            elif(l[len(l)-1] == "paper"):
                img1 = cv2.imread("./img/paper.jpg")
                cv2.imshow('S_P', img1)
                print("Kamu Kalah!")
                c_lose += 1
                # cv2.destroyWindow('S_P')
            else:
                img1 = cv2.imread("./img/stone.jpg")
                cv2.imshow('S_P', img1)
                print("Seri!")
                c_tie += 1
    for(x, y, w, h) in paper:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        count_p += 1
        if(count_p == 1):
            # print("paper-user")
            count_s = 0
            count_n = 0
            count_sc = 0
            cv2.destroyWindow('none')
            if(l[len(l)-1] == "stone"):
                img1 = cv2.imread("./img/stone.jpg")
                cv2.imshow('S_P', img1)
                print("Kamu Menang!")
                c_win += 1
            elif(l[len(l)-1] == "scissors"):
                img1 = cv2.imread("./img/scissors.jpg")
                cv2.imshow('S_P', img1)
                print("Kamu Kalah!")
                c_lose += 1
                # cv2.destroyWindow('S_P')
            else:
                img1 = cv2.imread("./img/paper.jpg")
                cv2.imshow('S_P', img1)
                print("Seri!")
                c_tie += 1
    if len(stone) == 0 and len(paper) == 0:
        for(x, y, w, h) in scissors:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            count_sc += 1
            if(count_sc == 1):
                cv2.destroyWindow('none')
                # print("paper-user")
                count_s = 0
                count_n = 0
                count_p = 0
                if(l[len(l)-1] == "paper"):
                    img1 = cv2.imread("./img/paper.jpg")
                    cv2.imshow('S_P', img1)
                    print("Kamu Menang!")
                    c_win += 1
                elif(l[len(l)-1] == "stone"):
                    img1 = cv2.imread("./img/stone.jpg")
                    cv2.imshow('S_P', img1)
                    print("Kamu Kalah!")
                    c_lose += 1
                    # cv2.destroyWindow('S_P')
                else:
                    img1 = cv2.imread("./img/scissors.jpg")
                    cv2.imshow('S_P', img1)
                    print("Seri!")
                    c_tie += 1

    if len(stone) == 0 and len(paper) == 0 and len(scissors) == 0:
        for(x, y, w, h) in none:
            # cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            img1 = cv2.imread("./img/none.jpg")
            cv2.imshow('Computer', img1)
            count_n += 1
            if(count_n == 1):
                # print("None")
                count_p = 0
                count_s = 0
                count_sc = 0
                cv2.destroyWindow('S_P')

    cv2.imshow('Player', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


print("Final Scores:-")
print("Player:", c_win, "Computer:", c_lose, "Tied:", c_tie)
cap.release()
cv2.destroyAllWindows()
