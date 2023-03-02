package instance_handlers

import (
	"carlosabdoamaral/stocks_fy.git/backend/common"
)

func DeclareInstancesRoutes() {
	router := common.Router
	g := router.Group("/instance")
	g.POST("/create", HandleCreateInstance)
	g.GET("/list", HandleFetchAllInstances)
	g.DELETE("/create", HandleCreateInstance)
}
