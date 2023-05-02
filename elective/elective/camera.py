import cv2

# Load YOLOv3 model
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Set minimum confidence level for detections
conf_threshold = 0.5

# Set non-maximum suppression threshold
nms_threshold = 0.4

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()
    
    # Convert frame to blob format for input to network
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    
    # Pass blob through network
    net.setInput(blob)
    outputs = net.forward(output_layers)
    
    # Process detections
    boxes = []
    confidences = []
    class_ids = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold and class_id == 0:
                # Object detected is a person
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                boxes.append([left, top, width, height])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    
    # Apply non-maximum suppression to eliminate overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        # Draw bounding box around detected person
        cv2.rectangle(frame, (left, top), (left+width, top+height), (0, 255, 0), 2)
    
    # Display output frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all windows
cap.release()
cv2.destroyAllWindows()
