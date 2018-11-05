(ns aweb.main
  (:require [ring.adapter.jetty :refer [run-jetty]]
            [ring.middleware.defaults :refer [wrap-defaults site-defaults]]
            [compojure.core :refer :all]
            ))


(def const-str (apply str (repeat 200 "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket")))


(defn index-handler [req]
  (let [length (or (Integer/parseInt (-> req :query-params first (val))) 1024)]
    (subs const-str 0 (max (min 10240 length) 1))))

(defroutes app-routes
           (GET "/" request index-handler))


(def app (-> app-routes
             (wrap-defaults site-defaults)))


(defn -main []
  (run-jetty #'app {:port 3000
                    :host "0.0.0.0"
                    :max-threads 100}))