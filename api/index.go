package main

import (
	"net/http"
	"fmt"
)

func main(w http.ResponseWriter) {
	fmt.Fprintf("Olá, Mundo!")
}