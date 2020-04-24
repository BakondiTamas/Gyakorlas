import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (1280,720))

cap.set(3, 1280)
cap.set(4, 720)

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cap.get(3)
        cap.get(4)

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()