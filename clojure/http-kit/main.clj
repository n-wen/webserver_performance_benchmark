(ns hk-demo.core
  (:use org.httpkit.server)
  (:require [compojure.core :refer :all]
            [ring.middleware.defaults :refer [wrap-defaults site-defaults]]))

(def const-str (apply str (repeat 200 "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket")))


(defn index-handler [req]
  (let [length (or (Integer/parseInt (-> req :query-params first (val))) 1024)]
    (subs const-str 0 (max (min 10240 length) 1))))

(defroutes app-routes
           (GET "/" request index-handler))


(def app (-> app-routes
             (wrap-defaults site-defaults)))


(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (run-server app {:port 3000}))
