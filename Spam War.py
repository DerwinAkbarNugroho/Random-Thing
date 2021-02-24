import pyautogui, time
N = int(input("How Much? "))
M = input("Message ")
time.sleep(7)
for spam in range(N):
    pyautogui.typewrite(M)
    pyautogui.press("enter")
print("End Program")

#Thank you @runs-15 for helping