import cv2
from com.dtmilano.android.viewclient import ViewClient

device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device=device, serialno=serialno)

while True:
    # get a screenshot of the device's screen
    screenshot = vc.device.takeSnapshot()

    # convert the screenshot to a numpy array for OpenCV processing
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # display the screenshot
    cv2.imshow("Android Screen", image)

    # wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord('q'):
        break

# close the window
cv2.destroyAllWindows()

