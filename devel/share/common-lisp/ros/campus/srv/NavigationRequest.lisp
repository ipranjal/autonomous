; Auto-generated. Do not edit!


(cl:in-package campus-srv)


;//! \htmlinclude NavigationRequest-request.msg.html

(cl:defclass <NavigationRequest-request> (roslisp-msg-protocol:ros-message)
  ((visitor_name
    :reader visitor_name
    :initarg :visitor_name
    :type cl:string
    :initform "")
   (host_name
    :reader host_name
    :initarg :host_name
    :type cl:string
    :initform "")
   (building
    :reader building
    :initarg :building
    :type cl:string
    :initform ""))
)

(cl:defclass NavigationRequest-request (<NavigationRequest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NavigationRequest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NavigationRequest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name campus-srv:<NavigationRequest-request> is deprecated: use campus-srv:NavigationRequest-request instead.")))

(cl:ensure-generic-function 'visitor_name-val :lambda-list '(m))
(cl:defmethod visitor_name-val ((m <NavigationRequest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader campus-srv:visitor_name-val is deprecated.  Use campus-srv:visitor_name instead.")
  (visitor_name m))

(cl:ensure-generic-function 'host_name-val :lambda-list '(m))
(cl:defmethod host_name-val ((m <NavigationRequest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader campus-srv:host_name-val is deprecated.  Use campus-srv:host_name instead.")
  (host_name m))

(cl:ensure-generic-function 'building-val :lambda-list '(m))
(cl:defmethod building-val ((m <NavigationRequest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader campus-srv:building-val is deprecated.  Use campus-srv:building instead.")
  (building m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NavigationRequest-request>) ostream)
  "Serializes a message object of type '<NavigationRequest-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'visitor_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'visitor_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'host_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'host_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'building))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'building))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NavigationRequest-request>) istream)
  "Deserializes a message object of type '<NavigationRequest-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'visitor_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'visitor_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'host_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'host_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'building) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'building) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NavigationRequest-request>)))
  "Returns string type for a service object of type '<NavigationRequest-request>"
  "campus/NavigationRequestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NavigationRequest-request)))
  "Returns string type for a service object of type 'NavigationRequest-request"
  "campus/NavigationRequestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NavigationRequest-request>)))
  "Returns md5sum for a message object of type '<NavigationRequest-request>"
  "dc84dc8ba58937ecacbf6f0bdb152093")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NavigationRequest-request)))
  "Returns md5sum for a message object of type 'NavigationRequest-request"
  "dc84dc8ba58937ecacbf6f0bdb152093")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NavigationRequest-request>)))
  "Returns full string definition for message of type '<NavigationRequest-request>"
  (cl:format cl:nil "# Request part~%string visitor_name~%string host_name~%string building~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NavigationRequest-request)))
  "Returns full string definition for message of type 'NavigationRequest-request"
  (cl:format cl:nil "# Request part~%string visitor_name~%string host_name~%string building~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NavigationRequest-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'visitor_name))
     4 (cl:length (cl:slot-value msg 'host_name))
     4 (cl:length (cl:slot-value msg 'building))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NavigationRequest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'NavigationRequest-request
    (cl:cons ':visitor_name (visitor_name msg))
    (cl:cons ':host_name (host_name msg))
    (cl:cons ':building (building msg))
))
;//! \htmlinclude NavigationRequest-response.msg.html

(cl:defclass <NavigationRequest-response> (roslisp-msg-protocol:ros-message)
  ((navigation_path
    :reader navigation_path
    :initarg :navigation_path
    :type cl:string
    :initform ""))
)

(cl:defclass NavigationRequest-response (<NavigationRequest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NavigationRequest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NavigationRequest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name campus-srv:<NavigationRequest-response> is deprecated: use campus-srv:NavigationRequest-response instead.")))

(cl:ensure-generic-function 'navigation_path-val :lambda-list '(m))
(cl:defmethod navigation_path-val ((m <NavigationRequest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader campus-srv:navigation_path-val is deprecated.  Use campus-srv:navigation_path instead.")
  (navigation_path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NavigationRequest-response>) ostream)
  "Serializes a message object of type '<NavigationRequest-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'navigation_path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'navigation_path))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NavigationRequest-response>) istream)
  "Deserializes a message object of type '<NavigationRequest-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'navigation_path) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'navigation_path) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NavigationRequest-response>)))
  "Returns string type for a service object of type '<NavigationRequest-response>"
  "campus/NavigationRequestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NavigationRequest-response)))
  "Returns string type for a service object of type 'NavigationRequest-response"
  "campus/NavigationRequestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NavigationRequest-response>)))
  "Returns md5sum for a message object of type '<NavigationRequest-response>"
  "dc84dc8ba58937ecacbf6f0bdb152093")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NavigationRequest-response)))
  "Returns md5sum for a message object of type 'NavigationRequest-response"
  "dc84dc8ba58937ecacbf6f0bdb152093")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NavigationRequest-response>)))
  "Returns full string definition for message of type '<NavigationRequest-response>"
  (cl:format cl:nil "# Response part~%string navigation_path~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NavigationRequest-response)))
  "Returns full string definition for message of type 'NavigationRequest-response"
  (cl:format cl:nil "# Response part~%string navigation_path~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NavigationRequest-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'navigation_path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NavigationRequest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'NavigationRequest-response
    (cl:cons ':navigation_path (navigation_path msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'NavigationRequest)))
  'NavigationRequest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'NavigationRequest)))
  'NavigationRequest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NavigationRequest)))
  "Returns string type for a service object of type '<NavigationRequest>"
  "campus/NavigationRequest")