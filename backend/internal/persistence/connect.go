package persistence

import (
	"database/sql"
	"fmt"

	"carlosabdoamaral/stocks_fy.git/backend/common"

	_ "github.com/lib/pq"
)

func Connect() (*sql.DB, error) {
	fmt.Println("[*] Connecting to Database")
	db, err := sql.Open(common.DatabaseDriver, fmt.Sprintf("user=%s password=%s dbname=%s sslmode=disable", common.DatabaseUser, common.DatabasePass, common.DatabaseName))
	if err != nil {
		return nil, err
	}

	fmt.Println("[*] Connected to Database")

	common.Database = db
	return db, nil
}
