import subprocess
import sys

import numpy as np

import cartopy

def make_random_svg(n=1):
    state_borders = cartopy.feature.NaturalEarthFeature(
        category='cultural', name='admin_1_states_provinces_lines',
        scale='50m', facecolor='none'
    )

    geoms = state_borders.geometries()

    for _ in range(n):
        gn = geoms.next()

    lx, ly = (np.floor(gn.bounds[0]), np.floor(gn.bounds[1]))

    svg_start = '''
<!DOCTYPE html><html><body>
<svg version="1.1"
     viewBox="''' + str(lx) + ' ' + str(ly) + ' ' + '15 15" ' + '''
     baseProfile="full" width="400" height="400"
     xmlns="http://www.w3.org/2000/svg">\n
'''

    svg_close = '\n</svg></body></html>'

    svg = svg_start + \
          gn.svg(scale_factor=0.1, stroke_color='black') + svg_close

    open('random_svg.html', 'w').write(svg)

    sys.exit(0)


if __name__ == "__main__":

    help_msg = '''
Make a .html page with an svg of the nth svg available in "state_borders"

Example (make html of 10th svg available):

    python make_random_svg.py 10
    '''

    if len(sys.argv) == 1:
        make_random_svg()

    elif len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            print help_msg
            sys.exit(0)
        make_random_svg(n=int(sys.argv[1]))

    else:
        print help_msg
        sys.exit(1)
