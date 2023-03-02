package responses

type StatusResponse struct {
	Status  int
	Message string `json:"message"`
}
