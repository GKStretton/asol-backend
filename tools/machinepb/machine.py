# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: machine.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


class Node(betterproto.Enum):
    UNDEFINED = 0
    HOME = 4
    HOME_TOP = 8
    # Above and inside test tube positions Note; INSIDE positions are valid for a
    # range of z values, determined outside Navigation.
    VIAL_1_ABOVE = 10
    MIN_VIAL_ABOVE = 10
    VIAL_1_INSIDE = 15
    MIN_VIAL_INSIDE = 15
    VIAL_2_ABOVE = 20
    VIAL_2_INSIDE = 25
    VIAL_3_ABOVE = 30
    VIAL_3_INSIDE = 35
    VIAL_4_ABOVE = 40
    VIAL_4_INSIDE = 45
    VIAL_5_ABOVE = 50
    VIAL_5_INSIDE = 55
    VIAL_6_ABOVE = 60
    VIAL_6_INSIDE = 65
    VIAL_7_ABOVE = 70
    MAX_VIAL_ABOVE = 70
    VIAL_7_INSIDE = 75
    MAX_VIAL_INSIDE = 75
    # The node to enter the lower (vial) regions at
    LOW_ENTRY_POINT = 30
    # High z but otherwise aligned for rinse container
    RINSE_CONTAINER_ENTRY = 80
    # Low z and aligned for rinse container (in water)
    RINSE_CONTAINER_LOW = 85
    OUTER_HANDOVER = 90
    INNER_HANDOVER = 110
    INVERSE_KINEMATICS_POSITION = 150
    IDLE_LOCATION = 80


class SolenoidValve(betterproto.Enum):
    """used in requests"""

    VALVE_UNDEFINED = 0
    VALVE_DRAIN = 1
    VALVE_WATER = 2
    VALVE_MILK = 3
    VALVE_AIR = 4


class Mode(betterproto.Enum):
    UNDEFINED_MODE = 0
    MANUAL = 1
    AUTONOMOUS = 2


class Status(betterproto.Enum):
    UNDEFINED_STATUS = 0
    ERROR = 1
    E_STOP_ACTIVE = 5
    SLEEPING = 6
    SHUTTING_DOWN = 9
    WAKING_UP = 10
    CALIBRATING = 20
    IDLE_STATIONARY = 30
    IDLE_MOVING = 31
    RINSING_PIPETTE = 40
    DISPENSING = 50
    WAITING_FOR_DISPENSE = 55
    COLLECTING = 60
    NAVIGATING_IK = 70
    NAVIGATING_OUTER = 75


class RinseStatus(betterproto.Enum):
    RINSE_UNDEFINED = 0
    RINSE_COMPLETE = 1
    RINSE_REQUESTED = 2
    RINSE_EXPELLING = 3


class FluidType(betterproto.Enum):
    FLUID_UNDEFINED = 0
    FLUID_DRAIN = 1
    FLUID_WATER = 2
    FLUID_MILK = 3


class ContentType(betterproto.Enum):
    CONTENT_TYPE_UNDEFINED = 0
    CONTENT_TYPE_LONGFORM = 1
    CONTENT_TYPE_SHORTFORM = 2
    CONTENT_TYPE_CLEANING = 3
    CONTENT_TYPE_DSLR = 4
    CONTENT_TYPE_STILL = 5


class SocialPlatform(betterproto.Enum):
    SOCIAL_PLATFORM_UNDEFINED = 0
    SOCIAL_PLATFORM_YOUTUBE = 1
    SOCIAL_PLATFORM_TIKTOK = 2
    SOCIAL_PLATFORM_INSTAGRAM = 3
    SOCIAL_PLATFORM_FACEBOOK = 4
    SOCIAL_PLATFORM_TWITTER = 5
    SOCIAL_PLATFORM_REDDIT = 6


@dataclass
class PipetteState(betterproto.Message):
    spent: bool = betterproto.bool_field(1)
    vial_held: int = betterproto.uint32_field(2)
    volume_target_ul: float = betterproto.float_field(3)
    # incremented every time a dispense is requested
    dispense_request_number: int = betterproto.uint32_field(4)


@dataclass
class CollectionRequest(betterproto.Message):
    completed: bool = betterproto.bool_field(1)
    request_number: int = betterproto.uint64_field(2)
    vial_number: int = betterproto.uint64_field(3)
    volume_ul: float = betterproto.float_field(4)


@dataclass
class MovementDetails(betterproto.Message):
    # ik target from -1 to 1
    target_x_unit: float = betterproto.float_field(1)
    # ik target from -1 to 1
    target_y_unit: float = betterproto.float_field(2)
    # ik z target in mm
    target_z_ik: float = betterproto.float_field(5)
    # fk target in degrees
    target_ring_deg: float = betterproto.float_field(10)
    # fk target in degrees
    target_yaw_deg: float = betterproto.float_field(11)


@dataclass
class FluidRequest(betterproto.Message):
    fluid_type: "FluidType" = betterproto.enum_field(1)
    volume_ml: float = betterproto.float_field(2)
    complete: bool = betterproto.bool_field(3)
    # if true, open drain while request is taking place (e.g. for rinsing with
    # water)
    open_drain: bool = betterproto.bool_field(4)


@dataclass
class FluidDetails(betterproto.Message):
    bowl_fluid_level_ml: float = betterproto.float_field(1)


@dataclass
class StateReport(betterproto.Message):
    # timestamp in microseconds since unix epoch, UTC. Added by gateway since
    # firmware doesn't know real time.
    timestamp_unix_micros: int = betterproto.uint64_field(2)
    # incremented on startup, currently 1 byte
    startup_counter: int = betterproto.uint64_field(3)
    mode: "Mode" = betterproto.enum_field(4)
    status: "Status" = betterproto.enum_field(5)
    # Useful for synchronisation with footage
    lights_on: bool = betterproto.bool_field(6)
    pipette_state: "PipetteState" = betterproto.message_field(10)
    collection_request: "CollectionRequest" = betterproto.message_field(11)
    movement_details: "MovementDetails" = betterproto.message_field(12)
    fluid_request: "FluidRequest" = betterproto.message_field(13)
    fluid_details: "FluidDetails" = betterproto.message_field(14)
    rinse_status: "RinseStatus" = betterproto.enum_field(15)
    # the following are populated by the backend, useful in post-processing
    paused: bool = betterproto.bool_field(50)
    timestamp_readable: str = betterproto.string_field(51)
    # e.g. 1 for 0001.jpg
    latest_dslr_file_number: int = betterproto.uint64_field(52)


@dataclass
class StateReportList(betterproto.Message):
    state_reports: List["StateReport"] = betterproto.message_field(1)


@dataclass
class SessionStatus(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    paused: bool = betterproto.bool_field(2)
    complete: bool = betterproto.bool_field(3)
    production: bool = betterproto.bool_field(4)
    production_id: int = betterproto.uint64_field(5)


@dataclass
class StreamStatus(betterproto.Message):
    live: bool = betterproto.bool_field(1)


@dataclass
class DispenseMetadataMap(betterproto.Message):
    # [startupCounter]_[dispenseRequestNumber]
    dispense_metadata: Dict[str, "DispenseMetadata"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass
class DispenseMetadata(betterproto.Message):
    failed_dispense: bool = betterproto.bool_field(1)
    # how many ms later than expected the dispense happened
    dispense_delay_ms: int = betterproto.uint64_field(2)
    # if non-zero, override the vial profile's duration with this value.
    min_duration_override_ms: int = betterproto.uint64_field(3)
    # if non-zero, override the vial profile's speed with this value.
    speed_mult_override: int = betterproto.uint64_field(4)


@dataclass
class ContentTypeStatuses(betterproto.Message):
    """statuses for all the content types for a specific session"""

    # str(ContentType) -> ContentTypeStatus
    content_statuses: Dict[str, "ContentTypeStatus"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    # splashtext for this session
    splashtext: str = betterproto.string_field(2)
    splashtext_hue: int = betterproto.uint64_field(3)


@dataclass
class ContentTypeStatus(betterproto.Message):
    raw_title: str = betterproto.string_field(1)
    raw_description: str = betterproto.string_field(2)
    caption: str = betterproto.string_field(3)
    posts: List["Post"] = betterproto.message_field(5)


@dataclass
class Post(betterproto.Message):
    platform: "SocialPlatform" = betterproto.enum_field(1)
    # e.g. subreddit
    sub_platform: str = betterproto.string_field(2)
    title: str = betterproto.string_field(3)
    description: str = betterproto.string_field(4)
    uploaded: bool = betterproto.bool_field(5)
    url: str = betterproto.string_field(6)
    # if true and relevant, crosspost rather than reuploading, e.g. for reddit
    crosspost: bool = betterproto.bool_field(7)
    # seconds ts of when to publish. If 0, publish immediately, because 0 is in
    # the past.
    scheduled_unix_timetamp: int = betterproto.uint64_field(8)


@dataclass
class Email(betterproto.Message):
    """
    emails used for administration, not intended for audience distribution
    """

    subject: str = betterproto.string_field(1)
    body: str = betterproto.string_field(2)


@dataclass
class VialProfile(betterproto.Message):
    """
    This contains information about each vial/test tube.These should be
    maintained over time by the frontend interface and the backendin response
    to dispenses.The current value is copied into session files when a session
    starts if it's inthe system.
    """

    # incremental unique id for each vial in and out the system
    id: int = betterproto.uint64_field(1)
    # this should have a complete description of the mixture, including base
    # fluids and the percentage makeup of each. This may be augmented by
    # quantised makeup data in future.
    description: str = betterproto.string_field(2)
    # the pipette slop, how much extra volume to move on the first dispense
    slop_ul: float = betterproto.float_field(3)
    # how much volume to dispense each time
    dispense_volume_ul: float = betterproto.float_field(4)
    # how long after dispense to slow down the footage in the videos
    footage_delay_ms: int = betterproto.uint64_field(5)
    # how long to keep the footage slowed down in the videos
    footage_min_duration_ms: int = betterproto.uint64_field(6)
    # what speed to give the footage in the videos
    footage_speed_mult: float = betterproto.float_field(7)
    # if true, footage of this profile will not be treated differently to other
    # footage (no slowdown etc.)
    footage_ignore: bool = betterproto.bool_field(8)
    # Volume when this was first put in vial
    initial_volume_ul: float = betterproto.float_field(9)
    # Current volume. Note this will be just volume at start of session in
    # session files.
    current_volume_ul: float = betterproto.float_field(10)


@dataclass
class SystemVialConfiguration(betterproto.Message):
    """
    contains a map of the current vial positions to vial profile ids vial
    position -> VialProfile id.
    """

    vials: Dict[int, int] = betterproto.map_field(
        1, betterproto.TYPE_UINT64, betterproto.TYPE_UINT64
    )


@dataclass
class VialProfileCollection(betterproto.Message):
    """this is for all the VialProfiles, mapped by id."""

    # VialProfile ID -> VialProfile
    profiles: Dict[int, "VialProfile"] = betterproto.map_field(
        1, betterproto.TYPE_UINT64, betterproto.TYPE_MESSAGE
    )


@dataclass
class SystemVialConfigurationSnapshot(betterproto.Message):
    """
    contains a static snapshot of the VialProfiles for each system position
    """

    profiles: Dict[int, "VialProfile"] = betterproto.map_field(
        1, betterproto.TYPE_UINT64, betterproto.TYPE_MESSAGE
    )
