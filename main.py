#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def buildPage(textAreaContent):
    rotationLabel = "<label>Rotate by</label>"
    rotationInput = "<input type='number' name='rotation' />"

    messageLabel = "<label>Type a message:</label>"
    textArea = "<textarea name='message'>" +textAreaContent+ "</textarea>"

    submit = "<input type='submit'/>"
    form = "<form method='post'>" + rotationLabel + rotationInput + "<br>" + messageLabel + textArea + "<br>" + submit + "</form>"

    header = "<h2>Web Caesar</h2>"

    return header+form


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = buildPage("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encryptedMessage = caesar.encrypt(message, rotation)
        escapedMessage = cgi.escape(encryptedMessage)
        content = buildPage(escapedMessage)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
