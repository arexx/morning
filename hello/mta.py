import requests

STATUS_URL = "http://service.mta.info/ServiceStatus/status.html"

def get_mta_html():
	html = requests.get(STATUS_URL).text

	# Inject style overrides before body close tag.
	extra_style = """
		<style>
		  * { background-color: black; }
		  body { font-family: "Helvetica Neue", helvetica, arial, clean, sans-serif; font-size: 13px; }
		  td { border-width: 0 !important; }
		  table { border-width: 0 !important; }
		  .list_h { background-image: none; }
		  .gw { color: black; }
		  td.subwayCategory span { color: white; position: relative; top: 1px; left: 2px; }
		  td.subwayCategory span.subway_servicechange { color: #D00 }
		  td.subwayCategory span.subway_plannedwork { color: #D00 }
		  td.subwayCategory span.subway_suspended { color: #D00 }
		  td.subwayCategory span.subway_delays { color: #D00 }
		</style>
	"""
	html = html.replace("</body>", extra_style + "</body>")
	html = html.replace("widgetImages/bullets/", "/static/img/")
	html = html.replace(".gif", ".png")
	return html