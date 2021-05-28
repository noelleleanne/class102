import dropbox
import cv2
import time, random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
    
    return image_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = 'sl.AxplyfzllhD_Qa1HXrxRnigia_xkNh6C1oLUN-el8NIaS__2-7MY14MXcrK8-yKnLH5oVcokEiTHm-6bCESJ4pEQNg7muvn3yvpKsUzkCl27bhuv_Id1ZyQHsZRrwaUH0j-Kttk'
    file = image_name
    file_from = file
    file_to = "/NewFolder1/"+ (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()