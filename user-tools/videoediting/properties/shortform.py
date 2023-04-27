from videoediting.constants import *
from videoediting.properties.content_property_manager import *
from videoediting.loaders import MiscData

class ShortFormPropertyManager(BasePropertyManager):
	def get_format(self) -> Format:
		return Format.PORTRAIT

	def get_section_properties(self, video_state: VideoState, state_report: pb.StateReport, dm_wrapper: DispenseMetadataWrapper, misc_data: MiscData) -> [SectionProperties, float, float]:
		props, delay, min_duration = self.common_get_section_properties(video_state, state_report)
		if props.skip:
			return props

		# todo: Implement logic specific to SHORTFORM ContentType
		return props, delay, min_duration
