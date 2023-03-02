package persistence

import (
	"carlosabdoamaral/stocks_fy.git/backend/common"
	"carlosabdoamaral/stocks_fy.git/backend/internal/responses"
	"context"
	"errors"
	"fmt"
)

type InstancesPersistence struct{}

func (p *InstancesPersistence) Create(ctx context.Context, req *responses.CreateInstanceRequest) (*responses.StatusResponse, error) {
	query := fmt.Sprintf(`
		INSERT INTO birthdate_tb(day, month, year) VALUES (%d, %d, %d) RETURNING id`,
		req.Birthdate.Day(), req.Birthdate.Month(), req.Birthdate.Year(),
	)

	db := common.Database

	birthdateID := 0
	row := db.QueryRowContext(ctx, query)
	row.Scan(&birthdateID)
	if birthdateID == 0 {
		return nil, errors.New("some error occurred")
	}

	query = fmt.Sprintf(`
		INSERT INTO data_tb(
			id_birthdate,
			id_country,
			id_currency,
			id_most_used_ecommerce,
			id_risk_profile,
			id_school_level,
			id_last_stock,
			id_pretend_stock,
			fullname,
			email,
			ddd,
			phone,
			gender,
			mobile_device_os,
			current_job_category,
			current_amount,
			amount_avg_per_month,
			already_invested,
			technology_knowledge_level,
			use_ecommerce
		) VALUES
		(
			%d,
			%d,
			%d,
			%d,
			%d,
			%d,
			%d,
			%d,
			'%s',
			'%s',
			'%s',
			'%s',
			'%s',
			'%s',
			'%s',
			%v,
			%v,
			%v,
			%d,
			%v
		);`,
		birthdateID,
		req.IdCountry,
		req.IdCurrency,
		req.IdMostUsedEcommerce,
		req.IdRiskProfile,
		req.IdSchoolLevel,
		req.IdLastStock,
		req.IdPretendStock,
		req.Fullname,
		req.Email,
		req.Ddd,
		req.Phone,
		req.Gender,
		req.MobileDeviceOS,
		req.CurentJobCategory,
		req.CurrentAmount,
		req.AmountAvgPerMonth,
		req.AlreadyInvested,
		req.TechnologyKnowledgeLevel,
		req.UseEcommerce,
	)
	_, err := db.ExecContext(ctx, query)
	if err != nil {
		return nil, err
	}

	return &responses.StatusResponse{
		Status:  common.STATUS_OK,
		Message: "OK",
	}, nil
}
