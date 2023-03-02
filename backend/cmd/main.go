package main

import (
	"carlosabdoamaral/stocks_fy.git/backend/common"
	"carlosabdoamaral/stocks_fy.git/backend/internal/handlers/instance_handlers"
	"carlosabdoamaral/stocks_fy.git/backend/internal/persistence"

	"github.com/gin-gonic/gin"
)

func main() {
	err := common.GetEnvVariables()
	if err != nil {
		return
	}

	_, err = persistence.Connect()
	if err != nil {
		return
	}

	common.Router = gin.Default()
	common.Router.Use(CORS())
	instance_handlers.DeclareInstancesRoutes()
	common.Router.Run()
}

// https://github.com/gin-contrib/cors/issues/29
func CORS() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT, DELETE")

		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(204)
			return
		}

		c.Next()
	}
}
