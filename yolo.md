# Attributes used by the Ultralytics YOLO framework

Apart from the box metrics (.box) used for standard object detection, the Ultralytics YOLO framework provides several other attributes to evaluate different tasks and extract deep performance data.

These attributes can be split into Task-Specific Metrics Grouping and Deep-Dive Diagnostic Metrics.

1. Task-Specific Metrics Grouping
Just like .box holds bounding box metrics for standard object detection, YOLO provides distinct sub-objects for other tasks:

 .box (Bounding Box Metrics Group)
In YOLO, a model can perform different tasks (like object detection, instance segmentation, or pose estimation).

Meaning: .box is the sub-object inside the validation results containing all the evaluation metrics specifically related to bounding boxes (the rectangular boxes drawn around detected objects).

Why it's there: It groups box-related metrics together (like precision, recall, and mAP) so they don't get mixed up with segment mask or keypoint metrics.
.seg (Segmentation Metrics): Used in instance segmentation models (e.g., YOLOv8-seg). It contains metrics like .map50 and .map specifically calculated for the predicted pixel-level masks instead of bounding boxes.

.pose (Pose/Keypoint Metrics): Used in pose estimation models (e.g., YOLOv8-pose). It evaluates how accurately the model detected keypoints/skeleton joints.

.obb (Oriented Bounding Box Metrics): Used for models detecting rotated bounding boxes (commonly used in aerial/satellite imagery where objects are not perfectly aligned horizontally).

top1 and top5 (Classification Metrics): If you are running a classification model (e.g., YOLOv8-cls), you don't use .box. Instead, you extract accuracy using metrics.top1 (accuracy of the top prediction) and metrics.top5 (accuracy of the top 5 predictions).

2. Deep-Dive Diagnostic Metrics
When you are looking at .val_metrics.box (or .seg / .pose), you aren't limited to just overall average figures. You can access these granular attributes:

 .mp (Mean Precision)
Stands for: Mean Precision.

Meaning: Precision answers the question: "Out of all the bounding boxes the model predicted, how many were actually correct?"

# Precision= True Positives/True Positives+False Positives

In practice: A high .mp score (closer to 1.0) means your model is highly reliable when it makes a detection and rarely triggers false alarms (low false positives).

.mr (Mean Recall)
Stands for: Mean Recall.

Meaning: Recall (sometimes called sensitivity) answers the question: "Out of all the actual real objects in the images, how many did the model manage to find?"

# Recall= true positves/(true Positives+false Negatives)

 
In practice: A high .mr score (closer to 1.0) means the model is excellent at spotting target objects and rarely misses any (low false negatives).

 .map50 (mAP @ IoU 0.50)
Stands for: mean Average Precision at 50% Intersection over Union.

Meaning: This is a standard, relatively forgiving benchmark. It calculates the model's accuracy, counting a detection as correct ("True Positive") as long as the predicted bounding box overlaps with the real ground-truth box by at least 50%.

In practice: It shows how good the model is at generally locating and identifying the correct objects, even if its box boundaries are slightly loose or imperfect.

 .map (mAP @ IoU 0.50:0.95)
Stands for: mean Average Precision across a range of IoU thresholds.

Meaning: This is the gold standard and the strictest metric used to evaluate object detectors. It calculates the average mAP across 10 different overlap thresholds, starting from 50% up to 95% in steps of 5% (i.e., 0.50, 0.55, 0.60, ..., 0.95).

In practice: To score highly here, your model cannot just guess roughly where objects are. It has to draw highly precise, tightly-fitting bounding boxes around them. (Because of this strictness, .map values will always be lower than .map50 values).

.maps (Per-Class Performance)
What it is: A list or array of the final mAP 
50−95

  scores, broken down individually for every class in your dataset.

Why it's useful: If your overall .map is low, printing .maps helps you pinpoint exactly which object class is performing poorly and dragging the average down.

.f1 (F1-Score)
What it is: The F1-Score for each class. It is the harmonic mean of precision and recall:

# F1=2⋅ ((Precision⋅Recall)/(Precision+Recall))

Why it's useful: It gives you a single, balanced metric that takes both false positives and false negatives into account.

.p and .r (Per-Class Precision & Recall Vectors)
While .mp and .mr give you the mean precision and recall across the entire dataset, .p and .r return arrays containing the specific precision and recall values for each separate class.

.map75 (mAP @ IoU 0.75)
What it is: Calculates the mean Average Precision at a strict 75% overlap threshold. It serves as a middle-ground metric between the easy .map50 and the rigorous .map (50% to 95%).

.image_metrics (Per-Image Metrics)
What it is: A dictionary holding the validation metrics (precision, recall, F1, True Positives, False Positives, and False Negatives) computed individually for every single image in your validation set.

Why it's useful: It allows you to programmatically find the exact images your model struggled with the most.

.speed (Inference & Latency Metrics)
What it is: A dictionary returning the speed performance of your validation run.

Key words inside:

'preprocess': Time spent preparing the images (ms).

'inference': Pure model forwarding time (ms).

'postprocess': Time spent performing Non-Maximum Suppression (NMS) to clean up overlapping boxes (ms).
".mp, .mr, .box, .map, and .map50" 

These five terms are the core attributes used by the Ultralytics YOLO framework to organize and output object detection validation