#!/usr/bin/env python3

"""
Copyright (c) 2018 Mickaël "Kilawyn" Walter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import requests
import re

version = '0.1'

def main():
    parser = argparse.ArgumentParser(description='Reads a WP-JSON API on a WordPress installation to retrieve a maximum of publicly available information. These information comprise, but not only: posts, comments, pages, medias or users. As this tool could allow to access confidential (but not well-protected) data, it is recommended that you get first a written permission from the site owner. The author won\'t endorse any liability for misuse of this software',
    epilog='(c) 2018 Mickaël "Kilawyn" Walter. This program is licensed under the MIT license, check LICENSE.txt for mor information')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('target', type=str,
                        help='the base path of the WordPress installation to examine')
    parser.add_argument('-i', '--info', dest='info', action='store_true',
                        help='dumps basic information about the WordPress installation')
    parser.add_argument('-a', '--all', dest='all', action='store_true',
                        help='dumps all available information from the target API')

    args = parser.parse_args()

    motd = """
 _    _______  ___                  _____
| |  | | ___ \|_  |                /  ___|
| |  | | |_/ /  | | ___  ___  _ __ \ `--.  ___ _ __ __ _ _ __   ___ _ __
| |/\| |  __/   | |/ __|/ _ \| '_ \ `--. \/ __| '__/ _` | '_ \ / _ \ '__|
\  /\  / |  /\__/ /\__ \ (_) | | | /\__/ / (__| | | (_| | |_) |  __/ |
 \/  \/\_|  \____/ |___/\___/|_| |_\____/ \___|_|  \__,_| .__/ \___|_|
                                                        | |
                                                        |_|
    WPJsonScraper v%s
    By Mickaël \"Kilawyn\" Walter

    Make sure you use this tool with the approval of the site owner. Even if these information are public or available with proper authentication, this could be considered as an intrusion.

    Target: %s""" % (version, args.target)

    print(motd)




if __name__ == "__main__":
    main()