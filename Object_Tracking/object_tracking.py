import cv2
import numpy as np

# Kamera bağlantısını açın
cap = cv2.VideoCapture(0)

# Takip edilecek nesnenin rengini tanımlayın (örneğin, mavi)
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

while True:
    # Kamera görüntüsünü okuyun
    ret, frame = cap.read()

    # Görüntüyü HSV renk uzayına dönüştürün
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Belirtilen renk aralığında maske oluşturun
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Maskeyi kullanarak orijinal görüntüyü filtreleyin
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları gösterin
    cv2.imshow('Original', frame)
    cv2.imshow('Object Tracking', res)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapatın ve pencereleri kapatın
cap.release()
cv2.destroyAllWindows()
