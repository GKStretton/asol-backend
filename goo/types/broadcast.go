package types

type VoteStatus struct {
	VoteType             VoteType
	CollectionVoteStatus *CollectionVoteStatus
	LocationVoteStatus   *LocationVoteStatus
}

type CollectionVoteStatus struct {
	TotalVotes    int
	VoteCounts    map[uint64]uint64
	VialPosToName map[uint64]string
}

type LocationVoteStatus struct {
	TotalVotes int
	XAvg       float32
	YAvg       float32
}
