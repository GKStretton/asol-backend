from moviepy.editor import VideoClip, CompositeVideoClip
from moviepy.video.fx import crop
import pycommon.image as image

from pycommon.crop_util import CropConfig

from videoediting.properties.content_property_manager import SectionProperties
from videoediting.constants import Scene, Format
from videoediting.compositor_helpers import (
    build_session_number,
    build_speed,
    build_title,
)


def composeLandscape(metadata, props: SectionProperties, top_subclip: VideoClip, front_subclip: VideoClip) -> VideoClip:
    landscape_dim = (1920, 1080)

    if props.scene == Scene.DUAL:
        return CompositeVideoClip([
            front_subclip.resize(0.7).with_position((50, 'center')),
            top_subclip.resize(1.05).with_position((960, 'center')),

            build_title((490, 110), top_subclip.duration),
            build_session_number(metadata, (195, 990), top_subclip.duration),
            build_speed(props.speed, (1700, 20), top_subclip.duration),
        ], size=landscape_dim)

    print("scene {} not supported for landscape format".format(props.scene))
    exit(1)


def composePortrait(metadata, props: SectionProperties, top_subclip: VideoClip, front_subclip: VideoClip) -> VideoClip:
    portrait_dim = (1080, 1920)

    if props.scene != Scene.UNDEFINED:
        return CompositeVideoClip([
            front_subclip.resize(0.75).with_position(('center', 1120)),
            top_subclip.resize(1.05).with_position(('center', 50)),

            build_title((portrait_dim[0] // 2, 1055), top_subclip.duration),
            build_session_number(metadata, (195, 80), top_subclip.duration),
            build_speed(props.speed, (900, 20), top_subclip.duration),
        ], size=portrait_dim)

    print("scene {} not supported for portrait format".format(props.scene))
    exit(1)


def compositeContentFromFootageSubclips(
    top_subclip: VideoClip,
    top_crop: CropConfig,
    front_subclip: VideoClip,
    front_crop: CropConfig,
    props: SectionProperties,
    fmt: Format,
    session_metadata
) -> VideoClip:
    #! speed and skip are already applied, this is just for layout!

    # CROP & OVERLAY
    if props.crop:
        if top_crop is not None:
            top_subclip = crop.crop(top_subclip, x1=top_crop.x1, y1=top_crop.y1, x2=top_crop.x2, y2=top_crop.y2)
        if front_crop is not None:
            front_subclip = crop.crop(front_subclip, x1=front_crop.x1, y1=front_crop.y1,
                                      x2=front_crop.x2, y2=front_crop.y2)

        def add_top_overlay(img):
            i = img.copy()
            image.add_overlay(i)
            return i

        def add_front_feather(img):
            i = img.copy()
            image.add_feather(i)
            return i
        if props.vig_overlay:
            top_subclip = top_subclip.fl_image(add_top_overlay)
        if props.front_feather:
            front_subclip = front_subclip.fl_image(add_front_feather)

    # COMPOSITE
    clip: VideoClip = None
    if fmt == Format.LANDSCAPE:
        clip = composeLandscape(session_metadata, props, top_subclip, front_subclip)
    elif fmt == Format.PORTRAIT:
        clip = composePortrait(session_metadata, props, top_subclip, front_subclip)

    return clip
