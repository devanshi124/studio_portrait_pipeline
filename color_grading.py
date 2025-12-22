import cv2

def color_grade(input_path, output_path):
    img = cv2.imread(input_path)

    b, g, r = cv2.split(img)
    r = cv2.add(r, 10)
    b = cv2.subtract(b, 5)

    img = cv2.merge([b, g, r])
    cv2.imwrite(output_path, img)
