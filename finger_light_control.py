import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

WIDTH = 640
HEIGHT = 360

# 1. Setup the detector
model_path = 'hand_landmarker.task'

base_options = python.BaseOptions(
    model_asset_path=model_path
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.IMAGE,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)


# 2. Function to count fingers
def count_fingers(hand):

    fingers = 0

    # Thumb
    if hand[4].x < hand[3].x:
        fingers += 1

    # Index
    if hand[8].y < hand[6].y:
        fingers += 1

    # Middle
    if hand[12].y < hand[10].y:
        fingers += 1

    # Ring
    if hand[16].y < hand[14].y:
        fingers += 1

    # Pinky
    if hand[20].y < hand[18].y:
        fingers += 1

    return fingers


# 3. Open webcam
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


while cap.isOpened():

    success, frame = cap.read()

    if not success:
        continue

    # Mirror view
    frame = cv2.flip(frame, 1)

    # Convert BGR -> RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get actual dimensions
    h, w, _ = frame.shape

    # Create MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # Detect hand
    detection_result = detector.detect(mp_image)

    finger_count = 0

    # 4. Check if hand detected
    if detection_result.hand_landmarks:

        hand = detection_result.hand_landmarks[0]

        # Count fingers
        finger_count = count_fingers(hand)

        # Draw landmarks
        for landmark in hand:

            cx = int(landmark.x * w)
            cy = int(landmark.y * h)

            cv2.circle(
                frame,
                (cx, cy),
                5,
                (0, 255, 0),
                cv2.FILLED
            )


    # 5. Convert fingers to brightness
    brightness = finger_count * 51

    # 0 fingers  -> 0
    # 1 finger   -> 51
    # 2 fingers  -> 102
    # 3 fingers  -> 153
    # 4 fingers  -> 204
    # 5 fingers  -> 255


    # 6. Display finger count
    cv2.putText(
        frame,
        f"Fingers: {finger_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3
    )


    # 7. Display brightness
    percentage = int((brightness / 255) * 100)

    cv2.putText(
        frame,
        f"Brightness: {percentage}%",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )


    # 8. Show result
    cv2.imshow(
        "Finger Light Control",
        frame
    )


    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Cleanup
cap.release()
cv2.destroyAllWindows()