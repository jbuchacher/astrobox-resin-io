# coding=utf-8
__author__ = "Gina Häußge <osd@foosel.net>"
__author__ = "Daniel Arroyo <daniel@astroprint.com>"
__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'

import json

import octoprint.util as util

from flask import request, make_response, jsonify

from octoprint.server import restricted_access, NO_CONTENT
from octoprint.server.api import api

from astroprint.printer.manager import printerManager

@api.route("/job", methods=["POST"])
@restricted_access
def controlJob():
	printer = printerManager()

	if not printer.isOperational():
		return make_response("Printer is not operational", 409)

	valid_commands = {
		"start": [],
		"restart": [],
		"pause": [],
		"cancel": []
	}

	command, data, response = util.getJsonCommandFromRequest(request, valid_commands)
	if response is not None:
		return response

	activePrintjob = printer.isPrinting() or printer.isPaused()

	if command == "start":
		if activePrintjob:
			return make_response("Printer already has an active print job, did you mean 'restart'?", 409)
		printer.startPrint()
	elif command == "restart":
		if not printer.isPaused():
			return make_response("Printer does not have an active print job or is not paused", 409)
		printer.startPrint()
	elif command == "pause":
		if not activePrintjob:
			return make_response("Printer is neither printing nor paused, 'pause' command cannot be performed", 409)
		printer.togglePausePrint()
	elif command == "cancel":
		if not activePrintjob:
			response = make_response(json.dumps({
				'id': 'no_active_print',
				'msg': "Printer is neither printing nor paused, 'cancel' command cannot be performed"
			}), 409)
			response.headers['Content-Type'] = 'application/json';
			return response

		return jsonify(printer.cancelPrint())

	return NO_CONTENT


@api.route("/job", methods=["GET"])
def jobState():
	currentData = printerManager().getCurrentData()
	return jsonify({
		"job": currentData["job"],
		"progress": currentData["progress"],
		"state": currentData["state"]["text"]
	})
