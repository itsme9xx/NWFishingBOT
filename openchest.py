import pyautogui
import time
import keyboard
import requests


def main():
    response = requests.get("https://62bef367be8ba3a10d6010c6.mockapi.io/api/manga/token")
    data =response.json()
    tokenId =[]
    for d in data:
        so = d['tokenid']
        tokenId.append(so)
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
        try:
            token=int(input("Nhập Token của bạn: "))
            print(f"Token của bạn : {token} ")
        except ValueError:
            print("Sorry, try again")
            continue
        else:
            break

    for x in tokenId:   
        if token == x: 
            print("Bạn có thể chạy chương trình!")
            while True:
                pyautogui.moveTo(1100,930,0.3)
                pyautogui.click()
                time.sleep(.1)
                try:
                    if keyboard.is_pressed('x'): # Bấm phím x để xác dừng chương trình
                        break
                    else:
                        pass
                finally: 
                    pass
        
# Chay chuong trinh
if __name__ == '__main__':
    main()