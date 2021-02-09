package main

import (
	"fmt"
	"strconv"
	"log"
)

func main() {
	fmt.Printf("Please input a float number: ")

	var f_num_str string
	var i_num int
	fmt.Scan(&f_num_str)
	f_num,err := strconv.ParseFloat(f_num_str, 64)
	i_num = int(f_num)
	if err == nil{
		fmt.Printf(strconv.Itoa(i_num)+"\n")
	}else{
		log.Fatal("Error:",err)
	}
	
	
}

