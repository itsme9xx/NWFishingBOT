import pyautogui
import time
import keyboard

def main():
    # Tìm tất cả Windows với tiêu đề "New World"
    newWorldWindows = pyautogui.getWindowsWithTitle("New World")

    # Tìm Cửa sổ có tiêu đề chính xác là "New World" 
    for window in newWorldWindows:
        if window.title == "New World":
            newWorldWindow = window
            break

    # Chọn cửa sổ đó
    newWorldWindow.activate()

    while True:
        location = int(input('Nhập tọa độ cần câu của bạn: '))
        print(f'Tọa độ : {location}')
        time.sleep(5)
        pyautogui.press('b')
        time.sleep(1)
        #Với cần legendary thì y là 480 , tím thì y là 500 
        pyautogui.moveTo(880, location ,0.3)
        time.sleep(.5)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.move(50, 0,0.3)
        time.sleep(.5)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.move(0,-100,0.3)
        time.sleep(.5)
        pyautogui.click()
        break

# Chay chuong trinh
if __name__ == '__main__':
    main()      