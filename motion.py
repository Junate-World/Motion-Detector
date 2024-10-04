import cv2

cap = cv2.VideoCapture(0)
bg_sub = cv2.createBackgroundSubtractorMOG2()

while True:
  ret, frame = cap.read()

  fg_mask = bg_sub.apply(frame)

  cv2.imshow('actual_frame', frame)
  cv2.imshow('motion_frame', fg_mask)

  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break

cap.release()
cv2.destroyAllWindows()