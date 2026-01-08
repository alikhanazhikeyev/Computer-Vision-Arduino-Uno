import cv2
import mediapipe as mp
import serial

# Settings
SERIAL_PORT = "/dev/cu.usbserial-1130"
TARGET_FPS = 20  # For the sake of optimization, the number of fps was reduced

try:
    ser = serial.Serial(SERIAL_PORT, 115200, timeout=1)
    ser.flush()
    print(f'Serial connected: {ser.name}')
except Exception as e:
    print(f"Serial error: {e}")
    ser = None

WHITE_COLOR = (224, 224, 224)
BLUE_COLOR = (255, 0, 0)

mp_draw = mp.solutions.drawing_utils
draw_specs = mp_draw.DrawingSpec(color=WHITE_COLOR, thickness=2, circle_radius=2)

mp_pose = mp.solutions.hands
pose = mp_pose.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)

    image.flags.writeable = False
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    image.flags.writeable = True
    cv2.rectangle(image, (25, 130), (100, 200), BLUE_COLOR, cv2.FILLED)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Rendering
            mp_draw.draw_landmarks(image, hand_landmarks, mp_pose.HAND_CONNECTIONS, draw_specs, draw_specs)

            x_list = []
            y_list = []
            fingers_up = [0, 0, 0, 0, 0]

            h, w, c = image.shape

            for lm in hand_landmarks.landmark:
                x_list.append(int(lm.x * w))
                y_list.append(int(lm.y * h))

            # Fingers logic
            if x_list[4] <= x_list[5]: fingers_up[0] = 1
            if y_list[8] <= y_list[6]: fingers_up[1] = 1
            if y_list[12] <= y_list[10]: fingers_up[2] = 1
            if y_list[16] <= y_list[14]: fingers_up[3] = 1
            if y_list[20] < y_list[18]: fingers_up[4] = 1

            num_fingers_up = sum(fingers_up)
            message = ''.join(str(f) for f in fingers_up) + "\n"

            if ser:
                ser.write(message.encode('utf-8'))

            cv2.putText(image, str(num_fingers_up), (50, 180), cv2.FONT_HERSHEY_PLAIN, 3, WHITE_COLOR, 3)

    cv2.imshow('Video', image)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()