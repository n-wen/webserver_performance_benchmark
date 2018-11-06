package main

import (
	"net/http"
	"github.com/labstack/echo"
	"strconv"
	"time"
)

const constStrUnit = "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket"


func main() {
	var constStr = ""
	for i:=0; i < 200; i++ {
		constStr += constStrUnit
	}

	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		var length, err = strconv.Atoi(c.QueryParam("length"))
		if err != nil {

		}
		return c.String(http.StatusOK, constStr[:length])
	})
	s := &http.Server{
		Addr:           "0.0.0.0:3000",
		ReadTimeout:    60 * time.Second,
		WriteTimeout:   60 * time.Second,
		IdleTimeout:    6000 * time.Second,
	}
	e.Logger.Fatal(e.StartServer(s))
}