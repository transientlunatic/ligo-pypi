# -*- coding: utf-8 -*-
# git_version.py - vcs information module
#
# Copyright (C) 2010 Nickolas Fotopoulos
# Copyright (C) 2012-2013 Adam Mercer
# Copyright (C) 2016 Leo Singer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with with program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307 USA

id = "f1c13e21f6d66f7c1c83367f585289fcbe0a95f1"
date = "2017-05-11 14:34:43 +0000"
branch = "minke"
tag = "None"
if tag == "None":
    tag = None
author = "Daniel Williams <mail@daniel-williams.co.uk>"
builder = "Daniel Williams <mail@daniel-williams.co.uk>"
committer = "Daniel Williams <mail@daniel-williams.co.uk>"
status = "CLEAN: All modifications committed"
version = id
verbose_msg = """Branch: minke
Tag: None
Id: f1c13e21f6d66f7c1c83367f585289fcbe0a95f1

Builder: Daniel Williams <mail@daniel-williams.co.uk>
Repository status: CLEAN: All modifications committed"""

import warnings

class VersionMismatchError(ValueError):
    pass

def check_match(foreign_id, onmismatch="raise"):
    """
    If foreign_id != id, perform an action specified by the onmismatch
    kwarg. This can be useful for validating input files.

    onmismatch actions:
      "raise": raise a VersionMismatchError, stating both versions involved
      "warn": emit a warning, stating both versions involved
    """
    if onmismatch not in ("raise", "warn"):
        raise ValueError(onmismatch + " is an unrecognized value of onmismatch")
    if foreign_id == "f1c13e21f6d66f7c1c83367f585289fcbe0a95f1":
        return
    msg = "Program id (f1c13e21f6d66f7c1c83367f585289fcbe0a95f1) does not match given id (%s)." % foreign_id
    if onmismatch == "raise":
        raise VersionMismatchError(msg)

    # in the backtrace, show calling code
    warnings.warn(msg, UserWarning)
