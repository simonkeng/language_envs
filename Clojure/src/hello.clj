#!/usr/local/bin/clojure

(def helloworld "Hello World!")

(defn greet [name]
    (def greeting (str "Hello " name))
    (println greeting)
)

(println helloworld)
(println (str "and"))
(greet "Simon")