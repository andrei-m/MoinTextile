"""
    A Textile parser for MoinMoin

    @copyright: 2011 by Andrei Mackenzie
    @license: GNU GPL

    The following license terms pertain to all code inside the MoinTextile
    class:

Copyright (c) 2009, Jason Samsa, http://jsamsa.com/
Copyright (c) 2004, Roberto A. F. De Almeida, http://dealmeida.net/
Copyright (c) 2003, Mark Pilgrim, http://diveintomark.org/

Original PHP Version:
Copyright (c) 2003-2004, Dean Allen <dean@textism.com>
All rights reserved.

Thanks to Carlo Zottmann <carlo@g-blog.net> for refactoring
Textile's procedural code into a class framework

Additions and fixes Copyright (c) 2006 Alex Shiels http://thresholdstate.com/

L I C E N S E
=============
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name Textile nor the names of its contributors may be used to
  endorse or promote products derived from this software without specific
  prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

"""

import textile
import re

class MoinTextile(textile.Textile):
    """
    Special handling for hyperlinks
    """

    def links(self, text):
        """
        Accept '%' as a valid character in URLs so as to accept URLs that
        contain %20, etc.
        """

        punct = '!"#$%&\'*+,-./:;=?@\\^_`|~'

        pattern = r'''
            (?P<pre>    [\s\[{(]|[%s]   )?
            "                          # start
            (?P<atts>   %s       )
            (?P<text>   [^"]+?   )
            \s?
            (?:   \(([^)]+?)\)(?=")   )?     # $title
            ":
            (?P<url>    (?:ftp|https?)? (?: :// )? [-A-Za-z0-9+&@#/?=~_()|!:,.;%%]*[-A-Za-z0-9+&@#/=~_()|]   )
            (?P<post>   [^\w\/;]*?   )
            (?=<|\s|$)
        ''' % (re.escape(punct), self.c)

        text = re.compile(pattern, re.X).sub(self.fLink, text)

        return text

class Parser:
    """
    Parse the raw markup as Textile
    """

    def __init__(self, raw, request, **kw):
        """ 
        Initialize this parser with the raw markup, request, etc. 
        """
        self.raw = raw
        self.request = request
        self.form = request.form
        self._ = request.getText
        self.textiler = MoinTextile()

    def format(self, formatter):
        """ 
        Process the raw markup as Textile and write the result to
        the request 
        """
        processed = self.textiler.textile(self.raw)
        self.request.write(processed)

