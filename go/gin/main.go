package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
	"strconv"
)


const constStrUnit = "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket"


func main() {
	var constStr = ""
	for i:=0; i < 200; i++ {
		constStr += constStrUnit
	}
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		var length, err = strconv.Atoi(c.Query("length"))
		if err != nil {

		}
		c.String(200 , "%s", constStr[:length])
	})
	s := &http.Server{
		Addr:           ":3000",
		Handler:        r,
		ReadTimeout:    60 * time.Second,
		WriteTimeout:   60 * time.Second,
		IdleTimeout:    6000 * time.Second,
		MaxHeaderBytes: 1 << 20,
	}
	s.ListenAndServe()
}