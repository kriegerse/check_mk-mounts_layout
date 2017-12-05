#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

#
# (c) 2017 Sebastian Krieger <s_krieger@web.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

group = "mount_layout"
subgroup_applications = _("Storage, Filesystems and Files")

register_check_parameters(
    subgroup_applications,
    "mount_layout",
    _("Mount Layout definitions"),
    Dictionary(
        elements=[
	    ("blockdev",
	        ListOf(
                   TextUnicode(
                      title = _("Mountpoint"),
                      help = _("Add the fullpath of the mountpoint to check (e.g. /var)"),
                      size = 150,
                      default_value = "",
                   ),
                title = _("Block Device Mountpoints"),
                help = _("If your mountpoint to check is behind a block device add it here!"),
                add_label = _("Add mountpoint"),
                ),
            ),
            ("nfs",
                ListOf(
                   TextUnicode(
                      title = _("Mountpoint"),
                      help = _("Add the fullpath of the mountpoint to check (e.g. /home)"),
                      size = 150,
                      default_value = "",
                   ),
                title = _("NFS Mountpoints"),
                help = _("If your mountpoint to check is behind an NFS share add it here!"),
                add_label = _("Add mountpoint"),
                ),
            ),
            ("cifs",
                ListOf(
                   TextUnicode(
                      title = _("Mountpoint"),
                      help = _("Add the fullpath of the mountpoint to check (e.g. /srv/www)"),
                      size = 150,
                      default_value = "",
                   ),
                title = _("CIFS Mountpoints"),
                help = _("If your mountpoint to check is behind an CIFS share add it here!"),
                add_label = _("Add mountpoint"),
                ),
            ),
	    
   ]),
   None,
   "dict",
)
