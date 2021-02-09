package main

import (
	"crypto/md5"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

type Employee struct {
	Name   string `json:"empname"`
	Number int    `json:"empid"`
}

type User struct {
	ID        uint       `json:"id"`
	Email     string     `gorm:"not null;unique" json:"email"`
	CreatedAt time.Time  `json:"createdAt"`
	UpdatedAt time.Time  `json:"updatedAt"`
	DeletedAt *time.Time `json:"deletedAt"`
}

func main() {
	checkSumMigrate(&User{}, "User")

}

// fileExists checks if a file exists before we try using it to prevent further errors.
func fileExists(filename string) bool {
	_, err := os.Stat(filename)
	if os.IsNotExist(err) {
		return false
	}
	return true
}
func checkSumMigrate(structToMigrate interface{}, structName string) {

	structObj := structToMigrate
	jsonStruct, err := json.Marshal(structObj)
	if err != nil {
		fmt.Println(err)
		return
	}
	md5 := md5.Sum([]byte(jsonStruct))
	fmt.Printf("%x\n", md5)
	/*
	   dir := "./checksum_model"
	   filename := dir + "/" + structName + ".json"
	   migrateBool := false

	   if err != nil {
	       fmt.Println(err)
	       return
	   }
	   // Check if model_struct/ directory exist
	   if !fileExists(dir) {
	      fmt.Println(dir + " directory not exist, create a new one.")
	      os.Mkdir(dir, 0777)
	   }
	   if fileExists(filename) {
	       fmt.Println("Reading File")
	       // read the file from json
	       existJsonStruct, err := ioutil.ReadFile(filename)
	       if err != nil {
	           fmt.Println(err)
	           return
	       }
	       // compare the current struct from data
	       if (string(existJsonStruct) == string(jsonStruct)) {
	           fmt.Println("data match")
	       }else{
	           fmt.Println("Data unmatched: rewrite the data!")
	           migrateBool = true
	       }
	   } else {
	       fmt.Println(filename + " does not exist (or is a directory)")
	       migrateBool = true
	   }
	   if migrateBool {
	       // Write the file
	       fmt.Println(string(jsonStruct))
	       _ = ioutil.WriteFile(filename,jsonStruct, 0777)
	       // Migrate
	   }
	*/
}
func needMigrate(structToMigrate interface{}, structName string) {

	structObj := structToMigrate
	jsonStruct, err := json.Marshal(structObj)
	dir := "./model_struct"
	filename := dir + "/" + structName + ".json"
	migrateBool := false

	if err != nil {
		fmt.Println(err)
		return
	}
	// Check if model_struct/ directory exist
	if !fileExists(dir) {
		fmt.Println(dir + " directory not exist, create a new one.")
		os.Mkdir(dir, 0777)
	}
	if fileExists(filename) {
		fmt.Println("Reading File")
		// read the file from json
		existJsonStruct, err := ioutil.ReadFile(filename)
		if err != nil {
			fmt.Println(err)
			return
		}
		// compare the current struct from data
		if string(existJsonStruct) == string(jsonStruct) {
			fmt.Println("data match")
		} else {
			fmt.Println("Data unmatched: rewrite the data!")
			migrateBool = true
		}
	} else {
		fmt.Println(filename + " does not exist (or is a directory)")
		migrateBool = true
	}
	if migrateBool {
		// Write the file
		fmt.Println(string(jsonStruct))
		_ = ioutil.WriteFile(filename, jsonStruct, 0777)
		// Migrate
	}

}
