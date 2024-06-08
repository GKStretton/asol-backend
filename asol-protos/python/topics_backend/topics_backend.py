from typing import Literal

KV_KEY_ALL_VIAL_PROFILES: Literal["vial-profiles"] = "vial-profiles"
KV_KEY_SYSTEM_VIAL_PROFILES: Literal["system-vial-profiles"] = "system-vial-profiles"
KV_SCHEDULED_SESSION_FLAG_DISABLE_ACTOR: Literal["scheduled-session-flag-disable-actor"] = "scheduled-session-flag-disable-actor"
KV_SCHEDULED_SESSION_FLAG_SKIP: Literal["scheduled-session-flag-skip"] = "scheduled-session-flag-skip"
PAYLOAD_SMART_SWITCH_OFF: Literal["OFF"] = "OFF"
PAYLOAD_SMART_SWITCH_ON: Literal["ON"] = "ON"
TOPIC_ACTOR_START: Literal["asol/actor/start"] = "asol/actor/start"
TOPIC_ACTOR_STATUS_GET: Literal["asol/actor/status-get"] = "asol/actor/status-get"
TOPIC_ACTOR_STATUS_RESP: Literal["asol/actor/status-resp"] = "asol/actor/status-resp"
TOPIC_ACTOR_STOP: Literal["asol/actor/stop"] = "asol/actor/stop"
TOPIC_CLOSE_BLIND: Literal["asol/close_bedroom_blind"] = "asol/close_bedroom_blind"
TOPIC_EMAIL_SEND: Literal["asol/send-email"] = "asol/send-email"
TOPIC_FRIDGE_SWITCH: Literal["cmnd/tasmota_sw_fridge/Power1"] = "cmnd/tasmota_sw_fridge/Power1"
TOPIC_GENERATE_CONTENT: Literal["asol/generate-content"] = "asol/generate-content"
TOPIC_KV_GET: Literal["asol/kv/get/"] = "asol/kv/get/"
TOPIC_KV_GET_RESP: Literal["asol/kv/get-resp/"] = "asol/kv/get-resp/"
TOPIC_KV_SET: Literal["asol/kv/set/"] = "asol/kv/set/"
TOPIC_KV_SET_RESP: Literal["asol/kv/set-resp/"] = "asol/kv/set-resp/"
TOPIC_MARK_DELAYED_DISPENSE: Literal["asol/mark-delayed-dispense"] = "asol/mark-delayed-dispense"
TOPIC_MARK_FAILED_DISPENSE: Literal["asol/mark-failed-dispense"] = "asol/mark-failed-dispense"
TOPIC_MONITOR_OFF: Literal["asol/monitor_off"] = "asol/monitor_off"
TOPIC_MONITOR_ON: Literal["asol/monitor_on"] = "asol/monitor_on"
TOPIC_OPEN_BLIND: Literal["asol/open_bedroom_blind"] = "asol/open_bedroom_blind"
TOPIC_PIECE_SELECTED: Literal["asol/piece-selected"] = "asol/piece-selected"
TOPIC_RUN_END_SEQUENCE: Literal["asol/end-sequence"] = "asol/end-sequence"
TOPIC_RUN_FULL_SESSION: Literal["asol/run-full-session"] = "asol/run-full-session"
TOPIC_RUN_MANUAL_SESSION: Literal["asol/run-manual-session"] = "asol/run-manual-session"
TOPIC_RUN_START_SEQUENCE: Literal["asol/start-sequence"] = "asol/start-sequence"
TOPIC_RUN_TEST_SESSION: Literal["asol/run-test-session"] = "asol/run-test-session"
TOPIC_SESSION_BEGAN: Literal["asol/session/began"] = "asol/session/began"
TOPIC_SESSION_BEGIN: Literal["asol/session/begin"] = "asol/session/begin"
TOPIC_SESSION_END: Literal["asol/session/end"] = "asol/session/end"
TOPIC_SESSION_ENDED: Literal["asol/session/ended"] = "asol/session/ended"
TOPIC_SESSION_PAUSE: Literal["asol/session/pause"] = "asol/session/pause"
TOPIC_SESSION_PAUSED: Literal["asol/session/paused"] = "asol/session/paused"
TOPIC_SESSION_RESUME: Literal["asol/session/resume"] = "asol/session/resume"
TOPIC_SESSION_RESUMED: Literal["asol/session/resumed"] = "asol/session/resumed"
TOPIC_SESSION_STATUS_GET: Literal["asol/session/status-get"] = "asol/session/status-get"
TOPIC_SESSION_STATUS_RESP_JSON: Literal["asol/session/status-resp-json"] = "asol/session/status-resp-json"
TOPIC_SESSION_STATUS_RESP_RAW: Literal["asol/session/status-resp-raw"] = "asol/session/status-resp-raw"
TOPIC_SMART_SWITCH: Literal["cmnd/tasmota_sw1/Power1"] = "cmnd/tasmota_sw1/Power1"
TOPIC_STATE_REPORT_JSON: Literal["asol/state-report-json"] = "asol/state-report-json"
TOPIC_STILLS_GENERATED: Literal["asol/stills-generated"] = "asol/stills-generated"
TOPIC_STREAM_END: Literal["asol/stream/end"] = "asol/stream/end"
TOPIC_STREAM_START: Literal["asol/stream/begin"] = "asol/stream/begin"
TOPIC_STREAM_STATUS_GET: Literal["asol/stream/status-get"] = "asol/stream/status-get"
TOPIC_STREAM_STATUS_RESP_JSON: Literal["asol/stream/status-resp-json"] = "asol/stream/status-resp-json"
TOPIC_STREAM_STATUS_RESP_RAW: Literal["asol/stream/status-resp-raw"] = "asol/stream/status-resp-raw"
TOPIC_TRIGGER_DSLR: Literal["asol/dslr-crop-capture"] = "asol/dslr-crop-capture"
TOPIC_TRIGGER_DSLR_RESP: Literal["asol/dslr-crop-capture-resp"] = "asol/dslr-crop-capture-resp"
TOPIC_VIDEOS_GENERATED: Literal["asol/videos-generated"] = "asol/videos-generated"
TRIGGER_UPLOAD_FROM_CONTENT_PLAN: Literal["asol/upload-from-content-plan"] = "asol/upload-from-content-plan"
