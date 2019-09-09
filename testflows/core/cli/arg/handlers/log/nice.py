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
from argparse import FileType

import testflows.core.cli.arg.type as argtype

from testflows.core.cli.arg.common import epilog
from testflows.core.cli.arg.common import description
from testflows.core.cli.arg.common import RawDescriptionHelpFormatter
from testflows.core.cli.arg.handlers import Handler as HandlerBase
from testflows.core.transform.log.read import transform as read_transform
from testflows.core.transform.log.parse import transform as parse_transform
from testflows.core.transform.log.nice import transform as nice_transform

class Handler(HandlerBase):
    @classmethod
    def add_command(cls, commands):
        parser = commands.add_parser("nice", help="nice transform", epilog=epilog(),
            description=description("Transform log into a nice format."),
            formatter_class=RawDescriptionHelpFormatter)

        parser.add_argument("input", metavar="input", type=argtype.file("r", bufsize=0),
                nargs="?", help="input log, default: stdin", default="-")
        parser.add_argument("output", metavar="output", type=argtype.file("w", bufsize=0),
                nargs="?", help='output file, default: stdout', default="-")

        parser.set_defaults(func=cls())

    def pipeline(self, source):
        steps = [
            read_transform,
            parse_transform,
            nice_transform
        ]
        for step in steps:
            source = step(source)
        return source

    def handle(self, args):
        for item in self.pipeline(args.input):
            args.output.write(item)
