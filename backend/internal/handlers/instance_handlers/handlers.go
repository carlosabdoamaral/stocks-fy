package instance_handlers

import (
	"encoding/json"
	"io"
	"net/http"
	"time"

	"carlosabdoamaral/stocks_fy.git/backend/common"
	"carlosabdoamaral/stocks_fy.git/backend/internal/persistence"
	"carlosabdoamaral/stocks_fy.git/backend/internal/responses"

	"github.com/gin-gonic/gin"
)

func HandleCreateInstance(ctx *gin.Context) {
	bodyBytes, err := io.ReadAll(ctx.Request.Body)
	if err != nil {
		common.LogError(err.Error())
		ctx.IndentedJSON(http.StatusConflict, err.Error())
		return
	}

	model := &responses.CreateInstanceRequest{}
	err = json.Unmarshal(bodyBytes, model)
	if err != nil {
		common.LogError(err.Error())
		ctx.IndentedJSON(http.StatusConflict, err.Error())
		return
	}

	model.Birthdate, err = time.Parse("2006-01-02", model.JSONBirthdate)
	if err != nil {
		common.LogError(err.Error())
		ctx.IndentedJSON(http.StatusConflict, err.Error())
		return
	}

	err = SomeFieldIsEmptyOnCreateInstance(model)
	if err != nil {
		common.LogError(err.Error())
		ctx.IndentedJSON(http.StatusConflict, err.Error())
		return
	}

	instancePersistence := &persistence.InstancesPersistence{}
	res, err := instancePersistence.Create(ctx, model)
	if err != nil {
		common.LogError(err.Error())
		ctx.IndentedJSON(http.StatusConflict, err.Error())
		return
	}

	ctx.IndentedJSON(res.Status, res.Message)
}

func HandleFetchAllInstances(ctx *gin.Context) {
	ctx.IndentedJSON(http.StatusOK, "abc")
}

func HandleRemoveInstanceById(ctx *gin.Context) {
	ctx.IndentedJSON(http.StatusOK, "xyz")
}
