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
    num_hands=2
)

detector = vision.HandLandmarker.create_from_options(options)

# 2. Open webcam
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


# ---------------------------------------------------
# Function to count fingers
# ---------------------------------------------------
def count_fingers(hand):

    fingers = 0

    # Landmark IDs:
    # Thumb  -> 4
    # Index  -> 8
    # Middle -> 12
    # Ring   -> 16
    # Pinky  -> 20

    # -------------------------
    # Thumb
    # -------------------------
    if hand[4].x < hand[3].x:
        fingers += 1

    # -------------------------
    # Other 4 fingers
    # -------------------------
    if hand[8].y < hand[6].y:
        fingers += 1

    if hand[12].y < hand[10].y:
        fingers += 1

    if hand[16].y < hand[14].y:
        fingers += 1

    if hand[20].y < hand[18].y:
        fingers += 1

    return fingers


# ---------------------------------------------------
# Main loop
# ---------------------------------------------------
while cap.isOpened():

    success, frame = cap.read()

    if not success:
        continue

    # Mirror view
    frame = cv2.flip(frame, 1)

    # Convert BGR -> RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get actual frame dimensions
    h, w, _ = frame.shape

    # MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    # Detect hands
    detection_result = detector.detect(mp_image)

    total_fingers = 0

    # ---------------------------------------------------
    # If hands detected
    # ---------------------------------------------------
    if detection_result.hand_landmarks:

        for hand_index, hand in enumerate(
            detection_result.hand_landmarks
        ):

            # -------------------------
            # Draw landmarks
            # -------------------------
            for idx, landmark in enumerate(hand):

                cx = int(landmark.x * w)
                cy = int(landmark.y * h)

                cv2.circle(
                    frame,
                    (cx, cy),
                    5,
                    (0, 255, 0),
                    cv2.FILLED
                )

            # -------------------------
            # Count fingers
            # -------------------------
            finger_count = count_fingers(hand)

            total_fingers += finger_count

            # -------------------------
            # Display count for each hand
            # -------------------------
            text = f"Hand {hand_index + 1}: {finger_count}"

            cv2.putText(
                frame,
                text,
                (20, 40 + hand_index * 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    # ---------------------------------------------------
    # Total fingers
    # ---------------------------------------------------
    cv2.putText(
        frame,
        f"Total Fingers: {total_fingers}",
        (20, HEIGHT - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # Show frame
    cv2.imshow(
        "Finger Counter",
        frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Cleanup
cap.release()
cv2.destroyAllWindows()