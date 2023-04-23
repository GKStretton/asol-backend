package filesystem

import (
	"errors"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strconv"
)

var (
	basePath                 = flag.String("basePath", "/mnt/md0/light-stores/", "base path for storage data")
	contentPath              = flag.String("sessionPath", "session_content", "path for session content")
	metadataPath             = flag.String("metadataPath", "session_metadata", "path for session metadata")
	rawVideoPath             = flag.String("rawVideoPath", "video/raw", "path within session, of raw video")
	rawDslrPath              = flag.String("rawDslrPath", "dslr/raw", "path within session, of raw dslr captures")
	postDslrPath             = flag.String("postDslrPath", "dslr/post", "path within session, of post dslr captures")
	stateReportFileName      = flag.String("stateReportFileName", "state-reports.yml", "filename for list of state reports")
	dispenseMetadataFileName = flag.String("dispenseMetadataFileName", "dispense-metadata.yml", "filename for dispense metadata")
)

func AssertBasePaths() {
	e := Exists(*basePath)
	if !e {
		panic("base path '" + *basePath + "' does not exist")
	}
}

func GetBasePath() string {
	return *basePath
}

func Exists(filepath string) bool {
	_, err := os.Stat(filepath)
	if err == nil {
		return true
	} else if errors.Is(err, os.ErrNotExist) {
		return false
	} else {
		fmt.Printf("unkown Stat error for session base path assertion: %v\n", err)
		return false
	}
}

func GetMetadataDir() string {
	p := filepath.Join(*basePath, *metadataPath)
	err := os.MkdirAll(p, 0777)
	if err != nil {
		panic(fmt.Errorf("failed to create metadata path: %v", err))
	}
	SetPerms(p)
	return p
}

func GetStateReportPath(sessionId uint64) string {
	p := filepath.Join(
		*basePath,
		*contentPath,
		strconv.Itoa(int(sessionId)),
	)
	err := os.MkdirAll(p, 0777)
	if err != nil {
		panic(fmt.Errorf("failed to create state report path: %v", err))
	}
	SetPerms(p)
	return filepath.Join(p, *stateReportFileName)
}

func GetDispenseMetadataPath(sessionId uint64) string {
	p := filepath.Join(
		*basePath,
		*contentPath,
		strconv.Itoa(int(sessionId)),
	)
	err := os.MkdirAll(p, 0777)
	if err != nil {
		panic(fmt.Errorf("failed to create state report path: %v", err))
	}
	SetPerms(p)
	return filepath.Join(p, *dispenseMetadataFileName)
}

// GetRawVideoDir mkdirAlls the path if it doesn't exist.
//
//	e.g. 5, top-cam
func GetRawVideoDir(sessionId uint64, rtspPath string) string {
	p := filepath.Join(
		*basePath,
		*contentPath,
		strconv.Itoa(int(sessionId)),
		*rawVideoPath,
		rtspPath,
	)
	err := os.MkdirAll(p, 0777)
	if err != nil {
		panic(fmt.Errorf("failed to create raw video path: %v", err))
	}
	SetPerms(p)
	return p
}

func GetRawDslrDir(sessionId uint64) string {
	p := filepath.Join(
		*basePath,
		*contentPath,
		strconv.Itoa(int(sessionId)),
		*rawDslrPath,
	)
	err := os.MkdirAll(p, 0777)
	if err != nil {
		panic(fmt.Errorf("failed to create raw dslr path: %v", err))
	}
	SetPerms(p)
	return p
}

func GetPostDslrDir(sessionId uint64) string {
	p := filepath.Join(
		*basePath,
		*contentPath,
		strconv.Itoa(int(sessionId)),
		*postDslrPath,
	)
	err := os.MkdirAll(p, 0777)
	if err != nil {
		panic(fmt.Errorf("failed to create post dslr path: %v", err))
	}
	SetPerms(p)
	return p
}

// GetIncrementalFile considers 'outDir' and returns the **full path to** the
// next incremental file name on disk (w/ .'ext'). E.g:
//
//	1.mp4 2.mp4 3.mp4 -> [outDir]/4.mp4
func GetIncrementalFileName(outDir string, ext string) string {
	i := 1
	for {
		p := filepath.Join(outDir, fmt.Sprintf("%04d", i)+"."+ext)
		if !Exists(p) {
			return p
		}
		i++
		if i > 10000 {
			panic("bug in GetIncrementalFileName: filename should likely not exceed 10000")
		}
	}
}

func GetKeyValueStorePath() string {
	return filepath.Join(*basePath, "kv")
}
