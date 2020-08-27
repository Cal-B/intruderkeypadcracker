import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()    # X = 1920, Y = 1080 for example

def click1():
    pyautogui.click(screenWidth / 2.7, screenHeight / 2.7)

def click2():
    pyautogui.click(screenWidth / 2.133, screenHeight / 2.7)

def click3():
    pyautogui.click(screenWidth / 1.761, screenHeight / 2.7)

def click4():
    pyautogui.click(screenWidth / 2.7, screenHeight / 1.8)

def click5():
    pyautogui.click(screenWidth / 2.133, screenHeight / 1.8)

def click6():
    pyautogui.click(screenWidth / 1.761, screenHeight / 1.8)

def click7():
    pyautogui.click(screenWidth / 2.7, screenHeight / 1.411)

def click8():
    pyautogui.click(screenWidth / 2.133, screenHeight / 1.411)

def click9():
    pyautogui.click(screenWidth / 1.761, screenHeight / 1.411)

def click0():
    pyautogui.click(screenWidth / 2.133, screenHeight / 1.161)

digitsToClicks = {0 : click0, 1 : click1, 2 : click2, 3 : click3, 4 : click4, 5 : click5, 6 : click6, 7 : click7, 8 : click8, 9 : click9}

def main():
    time.sleep(5)   # click back into game window
    print("executing...")
    # Alternatively you could generate all permutations using list(permutations(range(4))) and evaluate each permutation with the dictionary 
    for i in range(10):     
        for j in range(10):
            for k in range(10):
                for l in range (10):
                    # print(str(i) + str(j) + str(k) + str(l))  # This won't be accurate to the current input, as each 4 click cycle registers faster than the program prints to screen 
                    digitsToClicks[i]()
                    digitsToClicks[j]()
                    digitsToClicks[k]()
                    digitsToClicks[l]()

    print("all permutations exhausted")

if __name__ == '__main__':
    main()





