package main

import (
	"fmt"
	"regexp"
	"bufio"
	"os"
	"log"
)

func main() {
	var input_str string
	var contain_bool bool = false
	

	
	fmt.Printf("Please input a string: ")
    //reading a string
    reader := bufio.NewReader(os.Stdin)
    input_str, err := reader.ReadString('\n')
    if err != nil {
    	log.Fatal(err)
    }else{
    	fmt.Printf(input_str)
    	// -i-a-n- no matter lower case or upper case
		re := regexp.MustCompile(`.*[iI].*[aA].*[nN].*`)

		contain_bool =re.MatchString(input_str)
		if contain_bool {
			fmt.Printf("Found\n")
		}else{
			fmt.Printf("Not Found\n")
		}
    }
	
}
