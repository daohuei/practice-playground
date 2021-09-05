import pprint
import json

json_string = '{"motion_filter_type": "h264", "motion_interval": 1.0, "motion_threshold": 68, "motion_bbx_area_threshold": 196, "amf_variance_threshold": 500, "amf_history_variance": false, "amf_frame_reduction": true}'
formatted_string = json.dumps(json_string, indent=4)
print(json_string)
print(formatted_string)
print(type(formatted_string))
print(json.loads(formatted_string))