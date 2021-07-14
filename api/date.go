package handler

import (
	"fmt"
	"net/http"
	"time"
)

func Handler(w http.ResponseWriter, r *http.Request) {
	currentTime := time.Now().Format(time.UTC-3).UTC()
	fmt.Fprintf(w, currentTime)
}