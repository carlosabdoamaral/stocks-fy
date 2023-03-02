package responses

import "time"

type CreateInstanceRequest struct {
	Birthdate                time.Time
	JSONBirthdate            string  `json:"birthdate"`
	IdCountry                int     `json:"id_country"`
	IdCurrency               int     `json:"id_currency"`
	IdMostUsedEcommerce      int     `json:"id_most_used_ecommerce"`
	IdRiskProfile            int     `json:"id_risk_profile"`
	IdSchoolLevel            int     `json:"id_school_level"`
	IdLastStock              int     `json:"id_last_stock"`
	IdPretendStock           int     `json:"id_pretend_stock"`
	Fullname                 string  `json:"fullname"`
	Email                    string  `json:"email"`
	Ddd                      string  `json:"ddd"`
	Phone                    string  `json:"phone"`
	Gender                   string  `json:"gender"`
	CurrentAmount            float64 `json:"current_amount"`
	AmountAvgPerMonth        float64 `json:"amount_avg_per_month"`
	AlreadyInvested          bool    `json:"already_invested"`
	TechnologyKnowledgeLevel int64   `json:"technology_knowledge_level"`
	UseEcommerce             bool    `json:"use_ecommerce"`
	MobileDeviceOS           string  `json:"mobile_device_os"`
	CurentJobCategory        string  `json:"current_job_category"`
}
