# el_panel_config_modify
f1 = {
    'admin_id': admin_check['_id'],
    'admin_name': info["admin_name"],
    'el_id': el_check.get('_id'),
    'el_no': info["el_no"],
    'time': info['time'],
    'action': "%s_change_el_config:%s_%s" % (info["admin_name"], info["el_no"], changes)
}

# el_string_config_modif
f2 = {
    'admin_id': admin_check['_id'],
    'admin_name': admin_name,
    'el_id': el_check.get('_id'),
    'string_line': string_line,
    'time': info_time,
    'action': "%s_change_el_string:%s_%s" % (admin_name, string_line, changes)
}

# el_panel_thresholds_modify
f3 = {
    'admin_id': admin_check['_id'],
    'admin_name': admin_name,
    'el_id': el_check['_id'],
    'el_no': el_no,
    'time': info_time,
    'action': "%s_change_el_config:%s_%s" % (admin_name, el_no, changes)
}

# gui_config_modify
f4 = {
    'admin_id': admin_check['_id'],
    'admin_name': admin_name,
    'gui_id': gui_check['_id'],
    'gui_no': gui_no,
    'time': info_time,
    'action': "%s_change_gui_config:%s_%s" % (admin_name, gui_no, changes)
}

# permission modify
f5 = {
    'admin_id': admin_check['_id'],
    'admin_name': admin_name,
    'type_id': permission_check['_id'],
    'type': i["type"],
    'time': info_time,
    'action': "%s_change_permission_config:%s_%s" % (admin_name, i["type"], changes)
}

# ----------------------------------

# user login operator
f6 = {
    'user_id': user_check['_id'],
    'user_name': user_name,
    'time': info_time,
    'action': 'login_%s' % user_name
}

# user login admin
f7 = {
    'user_id': user_check['_id'],
    'user_name': user_name,
    'time': info_time,
    'action': "login_%s" % user_name
}

# user logout
f8 = {
    'user_id': user_check['_id'],
    'user_name': user_name,
    'time': info_time,
    'action': "logout_%s" % user_name
}

# user add
f9 = {
    'admin_id': admin_check["_id"],
    'admin_name': admin_name,
    'time': info_time,
    'action': "%s_add_user_%s" % (admin_name, user_name)
}

# user delete
f10 = {
    'user_id': user_check['_id'],
    'admin_id': admin_check['_id'],
    'admin_name': admin_name,
    'time': info_time,
    'action': "%s_del_user_%s" % (admin_name, user_name)
}

# user modify
f11 = {
    'admin_id': admin_check['_id'],
    'user_name': user_name,
    'user_id': user_check['_id'],
    'admin_name': admin_name,
    'time': info_time,
    'action': "%s_change_user:%s_%s" % (admin_name, user_name, changes)
}

# user password change
f12 = {
    'user_id': admin_check['_id'],
    'user_name': admin_name,
    'time': info_time,
    'action': "%s_password_change{%s}" % (admin_name, user_name)
}
