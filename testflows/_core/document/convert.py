# Copyright 2019 Vitaliy Zakaznikov (TestFlows Test Framework http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

from testflows._core.contrib.markdown2 import Markdown

md = Markdown(extras={
    "header-ids":None,
    "fenced-code-blocks":{"cssclass":"highlight"},
    "footnotes":None,
    "references": None,
    "target-blank-links": None,
    "nofollow": None,
    "noopener": None,
    "noreferrer": None
})

template = """
<head>
<link href="https://fonts.googleapis.com/css?family=Open+Sans&display=swap" rel="stylesheet"> 
<style>
%(style)s
</style>
</head>
<body>
%(body)s
</body>
"""

file_dir = os.path.dirname(os.path.abspath(__file__))
stylesheet = os.path.join(file_dir, "style.css")

def generate(source, destination, stylesheet, format=None):
    body = md.convert(source.read())
    document = template % {
        "body": body,
        "style": stylesheet.read()
    }
    destination.write(document)
