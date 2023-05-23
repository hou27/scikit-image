import cv2
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

# TODO add contour detection for enhanced accuracy

def imshow(imgs):
    # 이미지 출력
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    for i in range(len(imgs)):
        image = imgs[i]
        # 이미지 출력
        axes[i].imshow(image)
        axes[i].axis("off")

    plt.subplots_adjust(wspace=0.01)

    # 출력된 이미지 보이기
    plt.show()

def match(path1, path2):
    # read the images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    # display both images
    imshow([img1, img2])
    # turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # resize images for comparison
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    similarity_value = "{:.2f}".format(ssim(img1, img2)*100)

    return float(similarity_value)