package common

import (
	"database/sql"

	"github.com/gin-gonic/gin"
)

var (
	MockModeActivated bool = false
)

var (
	ApiPort string      = "8080"
	Router  *gin.Engine = &gin.Engine{}
)

var (
	Database       *sql.DB = &sql.DB{}
	DatabaseUser   string  = ""
	DatabasePass   string  = ""
	DatabaseHost   string  = ""
	DatabaseName   string  = ""
	DatabasePort   string  = ""
	DatabaseSSL    string  = ""
	DatabaseURL    string  = ""
	DatabaseDriver string  = "postgres"
)

const (
	STATUS_OK                    = 200
	STATUS_FORBIDDEN             = 403
	STATUS_NOT_FOUND             = 404
	STATUS_INTERNAL_SERVER_ERROR = 500
)
