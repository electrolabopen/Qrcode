from pyzbar import pyzbar
import argparse
import cv2
ap = argparse.ArgumentParser()
args = vars(ap.parse_args())
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255, 0), 2)
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
     
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 0, 0), 2)
            print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
            

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()