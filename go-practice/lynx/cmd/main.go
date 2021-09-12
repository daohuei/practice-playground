package main

import (
	"fmt"

	"github.com/daohuei/lynx/testdb"
)

func main() {
	// fmt.Printf("hello, world\n")
	// db.Test()
	currentDB := testdb.TestDB{DBPath: "db.json"}
	err := currentDB.New()
	if err != nil {
		panic(err)
	}
	fmt.Println(currentDB.Stats())
	// newValueByte, err := json.Marshal(map[string]string{"name": "HoiHoi"})
	// if err != nil {
	// 	panic(err)
	// }
	// err = currentDB.Put([]byte("_456"), newValueByte)
	// data, err := alphaDB.Get([]byte("_123"))
	// err = alphaDB.Delete([]byte("_456"))
	// if err != nil {
	// 	panic(err)
	// }
	// fmt.Println(string(data))
	// dbs := []db.BackendDatabase{db.AlphaDB{}, db.BetaDB{}}
	// for _, currentDB := range dbs {
	// 	fmt.Println(currentDB.Stats())
	// }
	currentDB.Close()
}
