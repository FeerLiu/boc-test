from openerp.osv import fields,osv
from openerp.tools.translate import _

class display_dialog_box(osv.osv_memory):
    _name = "display.dialog.box"
    _columns={
        'text': fields.text(),
    }
display_dialog_box()
