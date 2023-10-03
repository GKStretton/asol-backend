package scheduler

import (
	"fmt"
	"time"

	"github.com/gkstretton/dark/services/goo/session"
)

type RecurringTime struct {
	day    time.Weekday
	hour   int
	minute int
	second int
}

type Schedule struct {
	name          string
	enabled       bool
	function      func()
	recurringTime RecurringTime
	// this long before or after the recurring time
	minuteOffset int
	secondOffset int
}

func (s *Schedule) nextRunTime() time.Time {
	// schedule items are defined in utc
	now := time.Now().UTC()
	// work out the time
	recurringTime := s.recurringTime
	nextRunTime := time.Date(
		now.Year(),
		now.Month(),
		now.Day(),
		recurringTime.hour,
		recurringTime.minute,
		recurringTime.second,
		0,
		now.Location(),
	)
	// offset the time
	nextRunTime = nextRunTime.Add(time.Minute * time.Duration(s.minuteOffset))
	nextRunTime = nextRunTime.Add(time.Second * time.Duration(s.secondOffset))

	// fix the day
	nextRun := nextRunTime.AddDate(0, 0, int(recurringTime.day)-int(now.Weekday()))
	if nextRun.Before(now) {
		nextRun = nextRun.AddDate(0, 0, 7)
	}
	return nextRun
}

func scheduleWatcher(s *Schedule) {
	for {
		// wait until next s.
		nextRun := s.nextRunTime()
		timeUntil := time.Until(nextRun)
		fmt.Printf("[schedule] scheduling %s for %s (%s)\n", s.name, nextRun, timeUntil)
		<-time.After(timeUntil)

		if !s.enabled {
			fmt.Printf("[schedule] skipping %s, not enabled\n", s.name)
			continue
		}

		// execute
		fmt.Printf("[schedule] executing %s\n", s.name)
		s.function()
	}
}

func Start(sm *session.SessionManager) {
	defineSchedule(sm)
}
