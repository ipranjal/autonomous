# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "campus: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/miniconda3/envs/ros_env/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(campus_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" NAME_WE)
add_custom_target(_campus_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "campus" "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(campus
  "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/campus
)

### Generating Module File
_generate_module_cpp(campus
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/campus
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(campus_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(campus_generate_messages campus_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" NAME_WE)
add_dependencies(campus_generate_messages_cpp _campus_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(campus_gencpp)
add_dependencies(campus_gencpp campus_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS campus_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(campus
  "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/campus
)

### Generating Module File
_generate_module_eus(campus
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/campus
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(campus_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(campus_generate_messages campus_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" NAME_WE)
add_dependencies(campus_generate_messages_eus _campus_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(campus_geneus)
add_dependencies(campus_geneus campus_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS campus_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(campus
  "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/campus
)

### Generating Module File
_generate_module_lisp(campus
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/campus
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(campus_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(campus_generate_messages campus_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" NAME_WE)
add_dependencies(campus_generate_messages_lisp _campus_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(campus_genlisp)
add_dependencies(campus_genlisp campus_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS campus_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(campus
  "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/campus
)

### Generating Module File
_generate_module_nodejs(campus
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/campus
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(campus_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(campus_generate_messages campus_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" NAME_WE)
add_dependencies(campus_generate_messages_nodejs _campus_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(campus_gennodejs)
add_dependencies(campus_gennodejs campus_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS campus_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(campus
  "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/campus
)

### Generating Module File
_generate_module_py(campus
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/campus
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(campus_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(campus_generate_messages campus_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/Users/pranjal/Desktop/autonomus-ai/src/campus/srv/NavigationRequest.srv" NAME_WE)
add_dependencies(campus_generate_messages_py _campus_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(campus_genpy)
add_dependencies(campus_genpy campus_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS campus_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/campus)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/campus
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(campus_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/campus)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/campus
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(campus_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/campus)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/campus
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(campus_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/campus)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/campus
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(campus_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/campus)
  install(CODE "execute_process(COMMAND \"/opt/miniconda3/envs/ros_env/bin/python3.11\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/campus\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/campus
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(campus_generate_messages_py std_msgs_generate_messages_py)
endif()
