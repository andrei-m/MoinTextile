"""
	A Textile parser for MoinMoin

	@copyright: 2011 by Andrei Mackenzie
	@license: GNU GPL
"""

import textile

class Parser:
		"""
				Parse the raw markup as Textile
		"""

		def __init__(self, raw, request, **kw):
				""" Initialize this parser with the raw markup, request, etc. """
				self.raw = raw
				self.request = request
				self.form = request.form
				self._ = request.getText

		def format(self, formatter):
				""" Process the raw markup as Textile and write the result to
						the request """
				processed = textile.textile(self.raw)
				self.request.write(processed)

