import yaml
import typing
import os
import argparse
from PIL import Image
import machinepb.machine as pb
from dataclasses import dataclass
from pathlib import Path

def get_session_metadata(base_dir: str, session_number: int):
	filename = "{}_session.yml".format(session_number)
	path = os.path.join(base_dir, "session_metadata", filename)
	yml = None
	with open(path, 'r') as f:
		yml = yaml.load(f, Loader=yaml.FullLoader)
	print("Loaded session metadata: {}\n".format(yml))
	return yml
	
def get_session_content_path(args: argparse.Namespace):
	return os.path.join(args.base_dir, "session_content", args.session_number)

def get_state_reports(args: argparse.Namespace) -> typing.Tuple[float, pb.StateReport]:
	content_path = get_session_content_path(args)
	raw_state_reports = None
	with open(os.path.join(content_path, "state-reports.yml"), 'r') as f:
		raw_state_reports = yaml.load(f, yaml.FullLoader)
	
	state_report_list = pb.StateReportList().from_dict(raw_state_reports).state_reports
	print("Loaded {} state report entries\n".format(len(state_report_list)))

	state_reports: typing.Tuple[float, pb.StateReport] = []
	for i in range(len(state_report_list)):
		report = state_report_list[i]
		report_ts = float(report.timestamp_unix_micros) / 1.0e6
		state_reports.append((report_ts, report))

	return state_reports

def get_selected_dslr_image(base_dir: str, session_number: int, image_choice: str) -> Image.Image:
	filename = f"{image_choice}.jpg"
	path = os.path.join(base_dir, "session_content", session_number, "dslr/post", filename)
	return Image.open(path)

# look up creationtime of selected.jpg dslr/post image
def get_selected_dslr_image_number(base_dir: str, session_number: int) -> int:
	linkname = f"selected.jpg"
	path = os.path.join(base_dir, "session_content", str(session_number), "dslr/post", linkname)

	# resolves symlink
	real_path = ""
	try:
		real_path = os.path.realpath(path)
	except:
		print("Error: could not resolve symlink {}".format(path))
		exit(1)

	name = Path(real_path).stem

	return int(name)

@dataclass
class MiscData:
	selected_dslr_number: int = 0

def get_misc_data(base_dir: str, session_number: int) -> MiscData:
	return MiscData(
		selected_dslr_number=get_selected_dslr_image_number(base_dir, session_number)
	)