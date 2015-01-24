#!/usr/bin/env python
# encoding: utf-8
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from efl import elementary
from efl.elementary.window import StandardWindow
from efl.elementary.layout import Layout
from efl.elementary.theme import theme_list_item_path_get

from efl.evas import EVAS_HINT_EXPAND
EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND


BODHI_ABOUT_VERSION = "3.0.0"
BODHI_ABOUT_TITLE = "Bodhi Linux"
BODHI_ABOUT_TEXT = """
Bodhi Linux - Enlightened Linux Desktop
"""
BODHI_ABOUT_AUTHORS = """
Jeff Hoogland (Jef91)<br>
Joris van Dijk (aeonius)<br>
Stephen Houston (okra)<br>
Kristi Hoogland (TheWife)<br>
Jason Thomas (Tristam)<br>
Kai Huuhko (kuuko)<br>
Robert Wiley (y_lee)<br>
Doug Yanez (Deepspeed)<br>
Eric Brown (feneric)<br>
Bob Eley<br>
Kaleb Elwert (belak)<br>
Karen Hoogland<br>
Micah Denn (M1C4HTRON13)<br>
Gareth Williams (hippytaff)<br>
Víctor Parra García (esmirlin)<br>
Anthony Cervantes (AntCer)<br>
Timmy Larsson (Timmy)<br>
Renato Rener (r1to)<br>
Agustin Verdegal (Agust)<br>
David La Monaca (cercamon)<br>
Alexandre Eldredge (Spoonite)<br>
Jose Manimala (Ittan)<br>
Erik Zervas (Tolcarael)<br>
Jason Peel (Jarope)<br>
Andreas Pachler<br>
Georg Eckert<br>
Michael Rokosz (mrokosz)<br>
Adrian Koryl (husarz)<br>
F. Junger<br>
Joao Teixeira<br>
Matt Carter (Matt)<br>
Hendra Kusuma<br>
"""


class BodhiDialog(StandardWindow):
    def __init__(self):
        StandardWindow.__init__(self, 'bodhi_about', 'About Bodhi')
        self.callback_delete_request_add(lambda o: elementary.exit())

        f = theme_list_item_path_get('default', None)
        ly = Layout(self, file=(f, 'e/widgets/about/main'),
                    size_hint_weight=EXPAND_BOTH)
        ly.part_text_set('e.text.label', 'Close')
        ly.part_text_set('e.text.title', BODHI_ABOUT_TITLE)
        ly.part_text_set('e.text.version', BODHI_ABOUT_VERSION)
        ly.part_text_set('e.textblock.about', BODHI_ABOUT_TEXT)
        ly.part_text_set('e.textblock.authors', BODHI_ABOUT_AUTHORS)
        ly.signal_callback_add('e,action,close', '*',
                            lambda l,e,s: elementary.exit())

        self.resize_object_add(ly)
        ly.show()
        self.show()


if __name__ == "__main__":
    elementary.init()
    BodhiDialog()
    elementary.run()
    elementary.shutdown()
