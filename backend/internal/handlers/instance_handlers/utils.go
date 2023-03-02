package instance_handlers

import (
	"carlosabdoamaral/stocks_fy.git/backend/internal/responses"
	"errors"
	"strings"
)

func SomeFieldIsEmptyOnCreateInstance(req *responses.CreateInstanceRequest) error {
	if req.IdCountry <= 0 ||
		req.IdCurrency <= 0 ||
		req.IdMostUsedEcommerce <= 0 ||
		req.IdRiskProfile <= 0 ||
		req.IdSchoolLevel <= 0 ||
		req.IdLastStock <= 0 ||
		req.IdPretendStock <= 0 ||
		strings.EqualFold(req.Fullname, "") ||
		strings.EqualFold(req.Email, "") ||
		strings.EqualFold(req.Ddd, "") ||
		strings.EqualFold(req.Phone, "") ||
		strings.EqualFold(req.Gender, "") ||
		strings.EqualFold(req.MobileDeviceOS, "") ||
		strings.EqualFold(req.CurentJobCategory, "") {
		return errors.New("some field is empty")
	}

	return nil
}
