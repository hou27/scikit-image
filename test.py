import itertools
from structural_similarity import match

image_paths = [
    "/content/drive/MyDrive/siamese-net/content/sign_data/jeong/j1_converted.png",
    "/content/drive/MyDrive/siamese-net/content/sign_data/jeong/j2_converted.png",
    "/content/drive/MyDrive/siamese-net/content/sign_data/jeong/j3_converted.png",
]

combinations = itertools.combinations(image_paths, 2)

for path1, path2 in combinations:
    filename1 = path1.rsplit("/", 1)[-1]
    filename2 = path2.rsplit("/", 1)[-1]
    similarity = match(path1, path2)
    print(f"Similarity between {filename1} and {filename2} : {similarity}%")

image3 = "/content/drive/MyDrive/siamese-net/content/sign_data/jeong/j3_converted.png"
weird_image = "/content/drive/MyDrive/siamese-net/content/sign_data/jeong/04_0114049.PNG"
similarity = match(image3, image3)
print(f"Similarity between j3_converted.png and j3_converted.png : {similarity}%")
similarity = match(image3, weird_image)
print(f"Similarity between j3_converted.png and j3_converted.png : {similarity}%")