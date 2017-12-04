#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

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
