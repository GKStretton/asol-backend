package server

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/gkstretton/study-of-light/twitch-ebs/openapi"
)

func (s *server) CollectFromVial(c *gin.Context) {
	var collectionRequest *openapi.CollectFromVialJSONRequestBody
	err := c.Bind(&collectionRequest)
	if err != nil {
		c.AbortWithError(http.StatusBadRequest, fmt.Errorf("could not bind: %w", err))
		return
	}

	if collectionRequest == nil || collectionRequest.Id == nil {
		c.AbortWithError(http.StatusBadRequest, fmt.Errorf("could not get id"))
		return
	}

	err = s.goo.CollectFromVial(*collectionRequest.Id)
	if err != nil {
		c.AbortWithError(http.StatusInternalServerError, err)
		return
	}

	c.Status(http.StatusAccepted)
}

func (s *server) Dispense(c *gin.Context) {
	err := s.goo.Dispense()
	if err != nil {
		c.AbortWithError(http.StatusInternalServerError, err)
		return
	}

	c.Status(http.StatusAccepted)
}

func (s *server) GoToPosition(c *gin.Context) {
	var goToRequest *openapi.GoToPositionJSONRequestBody
	err := c.Bind(&goToRequest)
	if err != nil {
		c.AbortWithError(http.StatusBadRequest, fmt.Errorf("could not bind: %w", err))
		return
	}

	if goToRequest == nil || goToRequest.X == nil || goToRequest.Y == nil {
		c.AbortWithError(http.StatusBadRequest, fmt.Errorf("could not get x and y fields from request"))
		return
	}

	err = s.goo.GoToPosition(*goToRequest.X, *goToRequest.Y)
	if err != nil {
		c.AbortWithError(http.StatusInternalServerError, err)
		return
	}

	c.Status(http.StatusAccepted)
}
