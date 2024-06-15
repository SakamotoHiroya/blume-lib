import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def find_smallest_circle_center(image):
    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # エッジ検出
    edges = cv2.Canny(gray, 50, 150)

    # 輪郭を検出
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 一番小さい円の中心を見つける
    smallest_radius = float('inf')
    center_x, center_y = 0, 0

    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        if radius < smallest_radius:
            smallest_radius = radius
            center_x, center_y = int(x), int(y)
    
    return center_x, center_y

def get_circle_distances(image, center_x, center_y):
    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # バイナリ画像に変換
    _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    
    # 画像の幅と高さを取得
    height, width = binary.shape
    
    distances = []

    pre_dis = 0
    
    for angle in range(360):
        # Convert angle to radians
        theta = math.radians(angle)
        
        # Calculate direction vector
        dir_x = math.cos(theta)
        dir_y = math.sin(theta)
        
        # Initialize distance from center
        distance = -1
        
        # List to store multiple distances for the same angle
        angle_distances = []
        
        
        while True:
            # Calculate coordinates along the direction vector
            x = int(center_x + distance * dir_x)
            y = int(center_y + distance * dir_y)
            
            # Check if coordinates are within image boundaries
            if x < 0 or x >= width or y < 0 or y >= height:
                break
            
            # Check if the pixel is on the object edge
            if binary[y, x] == 255:
                # Hit the edge of the object
                if distance - pre_dis != 1:
                    angle_distances.append(distance)
                pre_dis = distance
            
            distance += 1
        
        # Append angle and its distances to the main distances list
        if angle_distances:
            distances.append((angle, angle_distances))
    
    return distances

def get_distances():
    # 画像を読み込む
    image_path = 'cropped_image.jpg'  # 入力画像のパスを指定
    img = cv2.imread(image_path)

    if img is None:
        print("画像を読み込めませんでした。")
        exit()

    # 一番小さい円の中心を見つける
    center_x, center_y = find_smallest_circle_center(img)

    # 中心から円の輪郭までの距離を1度ごとに取得
    distances = get_circle_distances(img, center_x, center_y)

    new_distances = []
    target_1_base = 0
    target_2_base = 0
    target_3_base = 0
    counter = 0
    scaling_factor = 7 / 360
    for angle, angle_distances in distances:
        new_distance = []
        target_1 = int((angle_distances[2] + angle_distances[3]) / 2) 
        target_2 = int((angle_distances[4] + angle_distances[5]) / 2)  
        target_3 = int((angle_distances[6] + angle_distances[7]) / 2)
        formated_target_3 = target_3
        formated_target_2 = target_2
        formated_target_1 = target_1
        if counter ==0:
            target_1_base = formated_target_1
            target_2_base = formated_target_2
            target_3_base = formated_target_3
            counter += 1
        new_distance.append(formated_target_1 - target_1_base)
        new_distance.append(formated_target_2 - target_2_base)
        new_distance.append(formated_target_3 - target_3_base)
        scaled_angle = angle * scaling_factor
        new_distances.append((scaled_angle, new_distance))

    return new_distances
