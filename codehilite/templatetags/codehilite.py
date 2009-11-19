# Copyright (C) 2009  David Roberts <d@vidr.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer, TextLexer
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter
@stringfilter
def codehilite(value, arg):
    try:
        lexer = get_lexer_by_name(arg)
    except ValueError:
        try:
            lexer = guess_lexer(value)
        except ValueError:
            lexer = TextLexer()
    formatter = HtmlFormatter(cssclass="codehilite")
    return mark_safe(highlight(value, lexer, formatter))
