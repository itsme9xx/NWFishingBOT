import pyautogui
import time
import random
import mss
import numpy as np
from PIL import Image
import gc
import requests

def main():
    """
    Main function for the program
    """
    response = requests.get("https://62bef367be8ba3a10d6010c6.mockapi.io/api/manga/token")
    # print(response.json())
    data =response.json()
    tokenId =[]
    for d in data:
        so = d['tokenid']
        tokenId.append(so)

    # Thời gian cast tối đa là 1,9 giây
    # Thời gian cơ sở nó sẽ luôn cast
   
    castingBaseTime = 1.4
    # Lượng thời gian ngẫu nhiên tối đa để thêm vào cơ sở dữ liệu
    castingRandom = .1

    # Thời gian nhấp nhả cần
    lineSlackTime = 1.5

    # Thêm tính ngẫu nhiên vào thời gian chờ cho hoạt ảnh
    animationSleepTime = .1 + (.1 * random.random())

    # Ngẫu nhiên sẽ di chuyển sang phải hoặc trái để tránh AFK
    moveDirection = ["w", "s"]

    # Tìm tất cả Windows với tiêu đề "New World"
    newWorldWindows = pyautogui.getWindowsWithTitle("New World")

    # Tìm Cửa sổ có tiêu đề chính xác là "New World" 
    for window in newWorldWindows:
        if window.title == "New World":
            newWorldWindow = window
            break

    # Chọn cửa sổ đó
    newWorldWindow.activate()

    # Di chuyển chuột đến giữa cửa sổ trò chơi
    centerW = newWorldWindow.left + (newWorldWindow.width/2)    
    centerH = newWorldWindow.top + (newWorldWindow.height/2)
    pyautogui.moveTo(centerW, centerH)
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
            # Clicky Clicky
            time.sleep(animationSleepTime)
            pyautogui.click()
            time.sleep(animationSleepTime)
            
            # Chọn phần 3 ở giữa của New World Windown
            mssRegion = {"mon": 1, "top": newWorldWindow.top, "left": newWorldWindow.left + round(newWorldWindow.width/3), "width": round(newWorldWindow.width/3), "height": newWorldWindow.height}

            # Bắt đầu chụp màn hình đối tượng
            sct = mss.mss()

            # Điều này sẽ giải quyết các vấn đề với "cast" đầu tiên ngắn
            time.sleep(animationSleepTime * 3)
            #Khai báo các biến
            count = 0
            n =0 
            dem=10

            while True: 
                #Lấy giờ
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                # Ảnh chụp màn hình
                sctImg = Image.fromarray(np.array(sct.grab(mssRegion)))
                # Tính những thời điểm đó
                castingTime = castingBaseTime + (castingRandom * random.random())
                # Sửa cần
                # if count >= 70:
                #     # timesleep cho GeForce NOW
                #     # time.sleep(2)
                #     pyautogui.press('b')
                #     time.sleep(1)
                #     #Với cần legendary thì y là 480 , tím thì y là 500 
                #     pyautogui.moveTo(880, location,0.3)
                #     time.sleep(.5)
                #     pyautogui.click()
                #     time.sleep(.5)
                #     pyautogui.move(50, 0,0.3)
                #     time.sleep(.5)
                #     pyautogui.click()
                #     time.sleep(.5)
                #     pyautogui.move(0,-100,0.3)
                #     time.sleep(.5)
                #     pyautogui.click()
                #     pyautogui.press('b')
                #     time.sleep(2)
                #     pyautogui.press('f3')
                #     time.sleep(3)
                #     pyautogui.mouseDown()
                #     time.sleep(castingTime)
                #     pyautogui.mouseUp()
                #     # print('Sua can cau')
                #     count = 0
                # else: 
                #Press M
                # print("M Holding Down")
                #Code token timesleep ở đây
                # time.sleep(10)

                pyautogui.keyDown('m')
                time.sleep(random.uniform(0.1, 0.3))
                
                #Casting
                # print("Casting Line")
                pyautogui.mouseDown()
                time.sleep(castingTime)
                pyautogui.mouseUp()

                #Đếm Count
                count = count +1 

                #count = 10, 20, 30, 40 
                n = count / 10
                    
                
                # Tìm kiếm biểu tượng cá, thực hiện thu gom rác bắt buộc
                while pyautogui.locate("imgs/fishIcon.png", sctImg, grayscale=True, confidence=.6) is None:
                    gc.collect()
                    # Screenshot
                    sctImg = Image.fromarray(np.array(sct.grab(mssRegion)))

                # Câu cá
                # print("Fish Hooked")
                pyautogui.click()
                time.sleep(animationSleepTime)
                    
                # Tiếp tục giật cần với dòng chữ "HOLD Cast" hiển thị trên màn hình
                while pyautogui.locate("imgs/holdCast.png", sctImg, grayscale=True, confidence=.55) is None:
                    # print("Reeling....")
                    pyautogui.mouseDown()
                    

                    # Nếu biểu tượng nằm trong vùng màu cam nhả chuột
                    if pyautogui.locate("imgs/fishReelingCam.png" , sctImg, grayscale=True, confidence=.75) is not None:
                        # print("Slacking line...")
                        pyautogui.mouseUp()
                        time.sleep(lineSlackTime)

                    # Uses a lot of memory if you don't force collection
                    gc.collect()
                    # Screenshot
                    sctImg = Image.fromarray(np.array(sct.grab(mssRegion)))

                    # Reel down time
                    time.sleep(animationSleepTime)
                    
                # time.sleep(7)
                pyautogui.mouseUp()
                time.sleep(animationSleepTime)
                    
                # print("Caught Fish")

                # 20% cơ hội di chuyển để tránh bộ đếm thời gian AFK
                # if random.randint(1, 5) == 5:
                #     key = moveDirection[random.randint(0, 1)]
                #     pyautogui.keyDown(key)
                #     time.sleep(.2)
                #     pyautogui.keyUp(key)
                
                # time.sleep(animationSleepTime*3)

                #Press M
                # print("M Holding Up")
                pyautogui.keyUp('m')
                    
                # Di chuyển W, S
                if count % 10 ==0 : 
                    muoivong = count
                if n % 2 != 0 and n>=1 and dem % 10 ==0 and (dem / 10) %2 !=0 and (muoivong / 10) %2 !=0 :
                    pyautogui.keyDown('s')
                    time.sleep(.1)
                    pyautogui.keyUp('s')
                    dem =dem + 10    
                    # print('S')
                elif n % 2 == 0 and n>=1 and dem % 10 ==0 and (dem / 10) %2 ==0 and (muoivong / 10) %2 ==0  :
                    pyautogui.keyDown('w')
                    time.sleep(.1)
                    pyautogui.keyUp('w')
                    dem =dem + 10
                    # print('W')

                #Xác định Count , độ bền của cần câu /10 -10  (ex: 2400/10 -10 = 230)
                # if count >= 70 : 
                #     time.sleep(3)
                #     pyautogui.press('f3')
                    # print(current_time)
                    
                # if count == 1 :
                #     print('Thoi gian bat dau moi lan sua can cau: ',current_time )
                        

                # print('So lan Count',count)         
        
            
# Chay chuong trinh
if __name__ == '__main__':
    main()




