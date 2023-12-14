import numpy as np
import cv2
from skimage.measure import label, regionprops


def find_my_image(img, number):
    img = np.array(img).mean(2)
    img[img > 50] = 0
    img[img != 0] = 1
    regions = regionprops(label(img))
    if len(regions) != 1:
        return False
    if regions[0].euler_number == 0:
        img[105:115, :] = 1
        regions = regionprops(label(img))
        if regions[0].euler_number == -2:
            print(f"'Моя' картинка найдена на кадре: {number + 1}")
            # plt.imshow(img)
            # plt.show()
            return True
    return False


print("Поиск начат...")

# cv2.namedWindow("Video")

cap = cv2.VideoCapture("output.avi")
success, img = cap.read()

i = 0
count = 0

while success:
    # cv2.imshow('Video', np.array(img))
    if find_my_image(img, i):
        count += 1
    i += 1

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

    success, img = cap.read()

print(f"В видео 'Моя' картинка встречается: {count} раз")
