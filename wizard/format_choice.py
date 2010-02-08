# -*- coding: utf-8 -*-
##############################################################################
#
#    jasper_server module for OpenERP, 
#    Copyright (C) 2010 SYLEAM Info Services (<http://www.Syleam.fr/>) Damien CRIER
#
#    This file is a part of jasper_server
#
#    jasper_server is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    jasper_server is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import wizard
import pooler

form  = """<?xml version="1.0" ?>
<form string="Format choice">
  <field name="format_choice" colspan="4" width="300"/>
</form>
"""

def _get_formats(self, cr, uid, ids):
    pool = pooler.get_pool(cr.dbname)
    return pool.get('jasper.document')._get_formats(cr, uid, ids)

fields = {
    'format_choice' : {'string': 'Format', 'type': 'selection', 'selection': _get_formats, 'required': True},

}


def _select_format(self, cr, uid, data, context=None):
    if not context:
        context={}

    pool = pooler.get_pool(cr.dbname)
    document_obj = pool.get('jasper.document')
    document = document_obj.browse(cr, uid, data[ids], context=context)
    if document_id :
        if document.format_choice == 'mono':
            action = 'create_wizard'
        elif document.format_choice == 'multi':
            action = 'format_choice'
    return action


def _create_wizard(self, cr, uid, data, context=None):

    return True

class format_choice(wizard.interface):
 states = {
        'init':{
            'actions': [],
            'result': {
                    'type': 'choice',
                    'next_state': _select_format,
                }
            },
        'format_choice':{
            'actions': [],
            'result': {
                    'type': 'form',
                    'arch': form,
                    'fields': fields,
                    'state' : (
                            ('end','Cancel'),
                            ('create_wizard', 'OK', 'gtk-ok', True),
                        )
                }
            },
        'create_wizard':{
            'actions': [_create_wizard],
            'result' : {
                    'type' : 'state',
                    'state' : 'end',
                }
            },
        }

format_choice('jasper_document_format_choice')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
