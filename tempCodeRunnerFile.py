import cv2
# import mediapipe as mp

# mp_hands=mp.solutions.hands
# mp_drawing=mp.solutions.drawing_utils
# hands=mp_hands.Hands(max_num_hand = 1,min_detection_confidence = 0.7)
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Camera is not working")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("can't receive frame")
#         break
    
#     frame = cv2.flip(frame,1)
#     cv2.imshow("live video", frame)
#     rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#     result = hands.process(rgb)
#     if result.multi_hand_landarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    
    
#     if cv2.waitKey(1)==ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()