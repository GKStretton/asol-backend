// Package openapi provides primitives to interact with the openapi HTTP API.
//
// Code generated by github.com/oapi-codegen/oapi-codegen/v2 version v2.3.0 DO NOT EDIT.
package openapi

import (
	"github.com/gin-gonic/gin"
)

const (
	BearerAuthScopes = "bearerAuth.Scopes"
)

// Error defines model for Error.
type Error struct {
	Message *string `json:"message,omitempty"`
}

// CollectFromVialJSONBody defines parameters for CollectFromVial.
type CollectFromVialJSONBody struct {
	// Id The ID of the vial to collect
	Id *int `json:"id,omitempty"`
}

// DispenseJSONBody defines parameters for Dispense.
type DispenseJSONBody struct {
	// X The x-coordinate to move to
	X *float32 `json:"x,omitempty"`

	// Y The y-coordinate to move to
	Y *float32 `json:"y,omitempty"`
}

// GoToPositionJSONBody defines parameters for GoToPosition.
type GoToPositionJSONBody struct {
	// X The x-coordinate to move to
	X *float32 `json:"x,omitempty"`

	// Y The y-coordinate to move to
	Y *float32 `json:"y,omitempty"`
}

// CollectFromVialJSONRequestBody defines body for CollectFromVial for application/json ContentType.
type CollectFromVialJSONRequestBody CollectFromVialJSONBody

// DispenseJSONRequestBody defines body for Dispense for application/json ContentType.
type DispenseJSONRequestBody DispenseJSONBody

// GoToPositionJSONRequestBody defines body for GoToPosition for application/json ContentType.
type GoToPositionJSONRequestBody GoToPositionJSONBody

// ServerInterface represents all server handlers.
type ServerInterface interface {
	// Claim control of the robot
	// (PUT /claim)
	Claim(c *gin.Context)
	// Collect from a vial
	// (POST /collect)
	CollectFromVial(c *gin.Context)
	// Bypass pubsub to get EBS state directly
	// (GET /direct-state)
	GetDirectState(c *gin.Context)
	// Dispense from pipette
	// (POST /dispense)
	Dispense(c *gin.Context)
	// Move the pipette tip to a specific position
	// (PUT /goto)
	GoToPosition(c *gin.Context)
	// Unclaim control of the robot
	// (PUT /unclaim)
	Unclaim(c *gin.Context)
}

// ServerInterfaceWrapper converts contexts to parameters.
type ServerInterfaceWrapper struct {
	Handler            ServerInterface
	HandlerMiddlewares []MiddlewareFunc
	ErrorHandler       func(*gin.Context, error, int)
}

type MiddlewareFunc func(c *gin.Context)

// Claim operation middleware
func (siw *ServerInterfaceWrapper) Claim(c *gin.Context) {

	c.Set(BearerAuthScopes, []string{})

	for _, middleware := range siw.HandlerMiddlewares {
		middleware(c)
		if c.IsAborted() {
			return
		}
	}

	siw.Handler.Claim(c)
}

// CollectFromVial operation middleware
func (siw *ServerInterfaceWrapper) CollectFromVial(c *gin.Context) {

	c.Set(BearerAuthScopes, []string{})

	for _, middleware := range siw.HandlerMiddlewares {
		middleware(c)
		if c.IsAborted() {
			return
		}
	}

	siw.Handler.CollectFromVial(c)
}

// GetDirectState operation middleware
func (siw *ServerInterfaceWrapper) GetDirectState(c *gin.Context) {

	c.Set(BearerAuthScopes, []string{})

	for _, middleware := range siw.HandlerMiddlewares {
		middleware(c)
		if c.IsAborted() {
			return
		}
	}

	siw.Handler.GetDirectState(c)
}

// Dispense operation middleware
func (siw *ServerInterfaceWrapper) Dispense(c *gin.Context) {

	c.Set(BearerAuthScopes, []string{})

	for _, middleware := range siw.HandlerMiddlewares {
		middleware(c)
		if c.IsAborted() {
			return
		}
	}

	siw.Handler.Dispense(c)
}

// GoToPosition operation middleware
func (siw *ServerInterfaceWrapper) GoToPosition(c *gin.Context) {

	c.Set(BearerAuthScopes, []string{})

	for _, middleware := range siw.HandlerMiddlewares {
		middleware(c)
		if c.IsAborted() {
			return
		}
	}

	siw.Handler.GoToPosition(c)
}

// Unclaim operation middleware
func (siw *ServerInterfaceWrapper) Unclaim(c *gin.Context) {

	c.Set(BearerAuthScopes, []string{})

	for _, middleware := range siw.HandlerMiddlewares {
		middleware(c)
		if c.IsAborted() {
			return
		}
	}

	siw.Handler.Unclaim(c)
}

// GinServerOptions provides options for the Gin server.
type GinServerOptions struct {
	BaseURL      string
	Middlewares  []MiddlewareFunc
	ErrorHandler func(*gin.Context, error, int)
}

// RegisterHandlers creates http.Handler with routing matching OpenAPI spec.
func RegisterHandlers(router gin.IRouter, si ServerInterface) {
	RegisterHandlersWithOptions(router, si, GinServerOptions{})
}

// RegisterHandlersWithOptions creates http.Handler with additional options
func RegisterHandlersWithOptions(router gin.IRouter, si ServerInterface, options GinServerOptions) {
	errorHandler := options.ErrorHandler
	if errorHandler == nil {
		errorHandler = func(c *gin.Context, err error, statusCode int) {
			c.JSON(statusCode, gin.H{"msg": err.Error()})
		}
	}

	wrapper := ServerInterfaceWrapper{
		Handler:            si,
		HandlerMiddlewares: options.Middlewares,
		ErrorHandler:       errorHandler,
	}

	router.PUT(options.BaseURL+"/claim", wrapper.Claim)
	router.POST(options.BaseURL+"/collect", wrapper.CollectFromVial)
	router.GET(options.BaseURL+"/direct-state", wrapper.GetDirectState)
	router.POST(options.BaseURL+"/dispense", wrapper.Dispense)
	router.PUT(options.BaseURL+"/goto", wrapper.GoToPosition)
	router.PUT(options.BaseURL+"/unclaim", wrapper.Unclaim)
}
