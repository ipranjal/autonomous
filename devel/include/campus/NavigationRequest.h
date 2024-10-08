// Generated by gencpp from file campus/NavigationRequest.msg
// DO NOT EDIT!


#ifndef CAMPUS_MESSAGE_NAVIGATIONREQUEST_H
#define CAMPUS_MESSAGE_NAVIGATIONREQUEST_H

#include <ros/service_traits.h>


#include <campus/NavigationRequestRequest.h>
#include <campus/NavigationRequestResponse.h>


namespace campus
{

struct NavigationRequest
{

typedef NavigationRequestRequest Request;
typedef NavigationRequestResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct NavigationRequest
} // namespace campus


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::campus::NavigationRequest > {
  static const char* value()
  {
    return "dc84dc8ba58937ecacbf6f0bdb152093";
  }

  static const char* value(const ::campus::NavigationRequest&) { return value(); }
};

template<>
struct DataType< ::campus::NavigationRequest > {
  static const char* value()
  {
    return "campus/NavigationRequest";
  }

  static const char* value(const ::campus::NavigationRequest&) { return value(); }
};


// service_traits::MD5Sum< ::campus::NavigationRequestRequest> should match
// service_traits::MD5Sum< ::campus::NavigationRequest >
template<>
struct MD5Sum< ::campus::NavigationRequestRequest>
{
  static const char* value()
  {
    return MD5Sum< ::campus::NavigationRequest >::value();
  }
  static const char* value(const ::campus::NavigationRequestRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::campus::NavigationRequestRequest> should match
// service_traits::DataType< ::campus::NavigationRequest >
template<>
struct DataType< ::campus::NavigationRequestRequest>
{
  static const char* value()
  {
    return DataType< ::campus::NavigationRequest >::value();
  }
  static const char* value(const ::campus::NavigationRequestRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::campus::NavigationRequestResponse> should match
// service_traits::MD5Sum< ::campus::NavigationRequest >
template<>
struct MD5Sum< ::campus::NavigationRequestResponse>
{
  static const char* value()
  {
    return MD5Sum< ::campus::NavigationRequest >::value();
  }
  static const char* value(const ::campus::NavigationRequestResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::campus::NavigationRequestResponse> should match
// service_traits::DataType< ::campus::NavigationRequest >
template<>
struct DataType< ::campus::NavigationRequestResponse>
{
  static const char* value()
  {
    return DataType< ::campus::NavigationRequest >::value();
  }
  static const char* value(const ::campus::NavigationRequestResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CAMPUS_MESSAGE_NAVIGATIONREQUEST_H
