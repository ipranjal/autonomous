;; Auto-generated. Do not edit!


(when (boundp 'campus::NavigationRequest)
  (if (not (find-package "CAMPUS"))
    (make-package "CAMPUS"))
  (shadow 'NavigationRequest (find-package "CAMPUS")))
(unless (find-package "CAMPUS::NAVIGATIONREQUEST")
  (make-package "CAMPUS::NAVIGATIONREQUEST"))
(unless (find-package "CAMPUS::NAVIGATIONREQUESTREQUEST")
  (make-package "CAMPUS::NAVIGATIONREQUESTREQUEST"))
(unless (find-package "CAMPUS::NAVIGATIONREQUESTRESPONSE")
  (make-package "CAMPUS::NAVIGATIONREQUESTRESPONSE"))

(in-package "ROS")





(defclass campus::NavigationRequestRequest
  :super ros::object
  :slots (_visitor_name _host_name _building ))

(defmethod campus::NavigationRequestRequest
  (:init
   (&key
    ((:visitor_name __visitor_name) "")
    ((:host_name __host_name) "")
    ((:building __building) "")
    )
   (send-super :init)
   (setq _visitor_name (string __visitor_name))
   (setq _host_name (string __host_name))
   (setq _building (string __building))
   self)
  (:visitor_name
   (&optional __visitor_name)
   (if __visitor_name (setq _visitor_name __visitor_name)) _visitor_name)
  (:host_name
   (&optional __host_name)
   (if __host_name (setq _host_name __host_name)) _host_name)
  (:building
   (&optional __building)
   (if __building (setq _building __building)) _building)
  (:serialization-length
   ()
   (+
    ;; string _visitor_name
    4 (length _visitor_name)
    ;; string _host_name
    4 (length _host_name)
    ;; string _building
    4 (length _building)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _visitor_name
       (write-long (length _visitor_name) s) (princ _visitor_name s)
     ;; string _host_name
       (write-long (length _host_name) s) (princ _host_name s)
     ;; string _building
       (write-long (length _building) s) (princ _building s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _visitor_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _visitor_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _host_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _host_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _building
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _building (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass campus::NavigationRequestResponse
  :super ros::object
  :slots (_navigation_path ))

(defmethod campus::NavigationRequestResponse
  (:init
   (&key
    ((:navigation_path __navigation_path) "")
    )
   (send-super :init)
   (setq _navigation_path (string __navigation_path))
   self)
  (:navigation_path
   (&optional __navigation_path)
   (if __navigation_path (setq _navigation_path __navigation_path)) _navigation_path)
  (:serialization-length
   ()
   (+
    ;; string _navigation_path
    4 (length _navigation_path)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _navigation_path
       (write-long (length _navigation_path) s) (princ _navigation_path s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _navigation_path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _navigation_path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass campus::NavigationRequest
  :super ros::object
  :slots ())

(setf (get campus::NavigationRequest :md5sum-) "dc84dc8ba58937ecacbf6f0bdb152093")
(setf (get campus::NavigationRequest :datatype-) "campus/NavigationRequest")
(setf (get campus::NavigationRequest :request) campus::NavigationRequestRequest)
(setf (get campus::NavigationRequest :response) campus::NavigationRequestResponse)

(defmethod campus::NavigationRequestRequest
  (:response () (instance campus::NavigationRequestResponse :init)))

(setf (get campus::NavigationRequestRequest :md5sum-) "dc84dc8ba58937ecacbf6f0bdb152093")
(setf (get campus::NavigationRequestRequest :datatype-) "campus/NavigationRequestRequest")
(setf (get campus::NavigationRequestRequest :definition-)
      "# Request part
string visitor_name
string host_name
string building
---
# Response part
string navigation_path

")

(setf (get campus::NavigationRequestResponse :md5sum-) "dc84dc8ba58937ecacbf6f0bdb152093")
(setf (get campus::NavigationRequestResponse :datatype-) "campus/NavigationRequestResponse")
(setf (get campus::NavigationRequestResponse :definition-)
      "# Request part
string visitor_name
string host_name
string building
---
# Response part
string navigation_path

")



(provide :campus/NavigationRequest "dc84dc8ba58937ecacbf6f0bdb152093")


