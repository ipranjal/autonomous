// Auto-generated. Do not edit!

// (in-package campus.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class NavigationRequestRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.visitor_name = null;
      this.host_name = null;
      this.building = null;
    }
    else {
      if (initObj.hasOwnProperty('visitor_name')) {
        this.visitor_name = initObj.visitor_name
      }
      else {
        this.visitor_name = '';
      }
      if (initObj.hasOwnProperty('host_name')) {
        this.host_name = initObj.host_name
      }
      else {
        this.host_name = '';
      }
      if (initObj.hasOwnProperty('building')) {
        this.building = initObj.building
      }
      else {
        this.building = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NavigationRequestRequest
    // Serialize message field [visitor_name]
    bufferOffset = _serializer.string(obj.visitor_name, buffer, bufferOffset);
    // Serialize message field [host_name]
    bufferOffset = _serializer.string(obj.host_name, buffer, bufferOffset);
    // Serialize message field [building]
    bufferOffset = _serializer.string(obj.building, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NavigationRequestRequest
    let len;
    let data = new NavigationRequestRequest(null);
    // Deserialize message field [visitor_name]
    data.visitor_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [host_name]
    data.host_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [building]
    data.building = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.visitor_name);
    length += _getByteLength(object.host_name);
    length += _getByteLength(object.building);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'campus/NavigationRequestRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ab65d6ac818cfafd32c8fec858fa616b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Request part
    string visitor_name
    string host_name
    string building
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NavigationRequestRequest(null);
    if (msg.visitor_name !== undefined) {
      resolved.visitor_name = msg.visitor_name;
    }
    else {
      resolved.visitor_name = ''
    }

    if (msg.host_name !== undefined) {
      resolved.host_name = msg.host_name;
    }
    else {
      resolved.host_name = ''
    }

    if (msg.building !== undefined) {
      resolved.building = msg.building;
    }
    else {
      resolved.building = ''
    }

    return resolved;
    }
};

class NavigationRequestResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.navigation_path = null;
    }
    else {
      if (initObj.hasOwnProperty('navigation_path')) {
        this.navigation_path = initObj.navigation_path
      }
      else {
        this.navigation_path = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NavigationRequestResponse
    // Serialize message field [navigation_path]
    bufferOffset = _serializer.string(obj.navigation_path, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NavigationRequestResponse
    let len;
    let data = new NavigationRequestResponse(null);
    // Deserialize message field [navigation_path]
    data.navigation_path = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.navigation_path);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'campus/NavigationRequestResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd9261615c63201e97c01e9db2b0cb3c1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Response part
    string navigation_path
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NavigationRequestResponse(null);
    if (msg.navigation_path !== undefined) {
      resolved.navigation_path = msg.navigation_path;
    }
    else {
      resolved.navigation_path = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: NavigationRequestRequest,
  Response: NavigationRequestResponse,
  md5sum() { return 'dc84dc8ba58937ecacbf6f0bdb152093'; },
  datatype() { return 'campus/NavigationRequest'; }
};
