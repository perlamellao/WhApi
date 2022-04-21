from whapi import whaDriver as wd
import os
import time

def qrLoop(driver):
    while True:
        if driver.loggedIn:
            break
        driver.getQr()
        print("QR code found")
        time.sleep(5)


def InitMenu():
    return("""
1. Initialize Whatsapp Driver           
2. Login with QR
3. Send message
4. Close

>>> """)

if __name__ == "__main__":
    DriverInitialized = False
    while True:
        os.system("clear")
        try:            
            choice = int(input(InitMenu()))
        except ValueError:
            print("Invalid input")
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            print("\nDetected ctrl+c, exiting...\nRemember that this may cause your session not to be closed properly")
            exit()
        
        if choice == 1:
            wd = wd()
            DriverInitialized = True
            print("Driver initialized")
            time.sleep(1)
            
        elif choice == 2:
            if DriverInitialized:
                print("\nThis will open multiple tabs of firefox showing you the qrCode\n You may need to close them manually\n")
                input("Press enter to continue")
                qrLoop(wd)
                print("Logged in")
                time.sleep(3)
                
            else:
                print("Driver not initialized")
                time.sleep(1)
    
        elif choice == 3:
            if DriverInitialized:
                os.system("clear")
                chatName = input("Enter chat name: ")
                msg = input("Enter message: ")
                wd.SendMsg(chatName, msg)
                time.sleep(1)
            else:
                print("Driver not initialized")
                time.sleep(1)
                
        elif choice == 4:
            try:
                wd.CloseSession()
                time.sleep(3)
                wd.close()
                
            except:
                pass
            
            os.system("clear")
            print("Closing and ending driver")
            print("Driver closed")
            time.sleep(2)
            break
        
        else:
            print("Invalid input")
            time.sleep(1)