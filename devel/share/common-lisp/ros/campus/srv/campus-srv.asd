
(cl:in-package :asdf)

(defsystem "campus-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "NavigationRequest" :depends-on ("_package_NavigationRequest"))
    (:file "_package_NavigationRequest" :depends-on ("_package"))
  ))