# -*- coding: utf-8 -*-
"""
@Time       : 2022/5/18 14:16
@Author     : Sun
@Email      : 18814563079@163.com
@Project    :
@File       : __init__.py
@Description:
@Software   : PyCharm
"""
from matplotlib import transforms
from matplotlib.patches import CirclePolygon
from numpy import ma
import numpy as np
import matplotlib.quiver


def _make_barbs_draw_below_2m(self, u, v, nflags, nbarbs, half_barb, empty_flag, length, pivot, sizes, fill_empty, flip):
    spacing = length * sizes.get('spacing', 0.125)
    full_height = length * sizes.get('height', 0.4)
    full_width = length * sizes.get('width', 0.25)
    empty_rad = length * sizes.get('emptybarb', 0.15)
    pivot_points = dict(tip=0.0, middle=-length / 2.)
    endx = 0.0
    try:
        endy = float(pivot)
    except ValueError:
        endy = pivot_points[pivot.lower()]
    angles = -(ma.arctan2(v, u) + np.pi / 2)
    circ = CirclePolygon((0, 0), radius=empty_rad).get_verts()
    if fill_empty:
        empty_barb = circ
    else:
        empty_barb = np.concatenate((circ, circ[::-1]))
    barb_list = []
    for index, angle in np.ndenumerate(angles):
        if empty_flag[index] and pivot != "tip":
            barb_list.append(empty_barb)
            continue
        poly_verts = [(endx, endy)]
        offset = length
        barb_height = -full_height if flip[index] else full_height
        for i in range(nflags[index]):
            if offset != length:
                offset += spacing / 2.
            poly_verts.extend(
                [[endx, endy + offset],
                 [endx + barb_height, endy - full_width / 2 + offset],
                 [endx, endy - full_width + offset]])
            offset -= full_width + spacing
        for i in range(nbarbs[index]):
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height, endy + offset + full_width / 2),
                 (endx, endy + offset)])
            offset -= spacing
        if half_barb[index]:
            if offset == length:
                poly_verts.append((endx, endy + offset))
                offset -= 1.5 * spacing
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height / 2, endy + offset + full_width / 4),
                 (endx, endy + offset)])
        if empty_flag[index] and pivot == "tip":
            if offset == length:
                poly_verts.append((endx, endy + offset))
        poly_verts = transforms.Affine2D().rotate(-angle).transform(poly_verts)
        barb_list.append(poly_verts)
    return barb_list


def _make_barbs_draw_empty_flag(self, u, v, nflags, nbarbs, half_barb, empty_flag, length, pivot, sizes, fill_empty, flip):
    spacing = length * sizes.get('spacing', 0.125)
    full_height = length * sizes.get('height', 0.4)
    full_width = length * sizes.get('width', 0.25)
    empty_rad = length * sizes.get('emptybarb', 0.15)
    pivot_points = dict(tip=0.0, middle=-length / 2.)
    endx = 0.0
    try:
        endy = float(pivot)
    except ValueError:
        endy = pivot_points[pivot.lower()]
    angles = -(ma.arctan2(v, u) + np.pi / 2)
    circ = CirclePolygon((0, 0), radius=empty_rad).get_verts()
    if fill_empty:
        empty_barb = circ
    else:
        empty_barb = np.concatenate((circ, circ[::-1]))
    barb_list = []
    for index, angle in np.ndenumerate(angles):
        if empty_flag[index]:
            barb_list.append(empty_barb)
            continue
        poly_verts = [(endx, endy)]
        offset = length
        barb_height = -full_height if flip[index] else full_height
        for i in range(nflags[index]):
            if offset != length:
                offset += spacing / 2.
            temp = [[endx, endy + offset],
                    [endx + barb_height, endy - full_width / 2 + offset],
                    [endx, endy - full_width + offset]]
            poly_verts.extend(np.concatenate((temp, temp[::-1])))
            offset -= full_width + spacing
        for i in range(nbarbs[index]):
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height, endy + offset + full_width / 2),
                 (endx, endy + offset)])
            offset -= spacing
        if half_barb[index]:
            if offset == length:
                poly_verts.append((endx, endy + offset))
                offset -= 1.5 * spacing
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height / 2, endy + offset + full_width / 4),
                 (endx, endy + offset)])
        poly_verts = transforms.Affine2D().rotate(-angle).transform(
            poly_verts)
        barb_list.append(poly_verts)
    return barb_list


def _make_barbs_draw_two_flag(self, u, v, full_nflags, empty_nflags, nbarbs, half_barb, empty_flag, length, pivot, sizes, fill_empty, flip):
    spacing = length * sizes.get('spacing', 0.125)
    full_height = length * sizes.get('height', 0.4)
    full_width = length * sizes.get('width', 0.25)
    empty_rad = length * sizes.get('emptybarb', 0.15)
    pivot_points = dict(tip=0.0, middle=-length / 2.)
    endx = 0.0
    try:
        endy = float(pivot)
    except ValueError:
        endy = pivot_points[pivot.lower()]
    angles = -(ma.arctan2(v, u) + np.pi / 2)
    circ = CirclePolygon((0, 0), radius=empty_rad).get_verts()
    if fill_empty:
        empty_barb = circ
    else:
        empty_barb = np.concatenate((circ, circ[::-1]))
    barb_list = []
    for index, angle in np.ndenumerate(angles):
        if empty_flag[index]:
            barb_list.append(empty_barb)
            continue
        poly_verts = [(endx, endy)]
        offset = length
        barb_height = -full_height if flip[index] else full_height
        for i in range(full_nflags[index]):
            if offset != length:
                offset += spacing / 2.
            temp = [[endx, endy + offset],
                    [endx + barb_height, endy - full_width / 2 + offset],
                    [endx, endy - full_width + offset]]
            poly_verts.extend(temp)
            offset -= full_width + spacing
        for i in range(empty_nflags[index]):
            if offset != length:
                offset += spacing / 2.
            temp = [[endx, endy + offset],
                    [endx + barb_height, endy - full_width / 2 + offset],
                    [endx, endy - full_width + offset]]
            poly_verts.extend(np.concatenate((temp, temp[::-1])))
            offset -= full_width + spacing
        for i in range(nbarbs[index]):
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height, endy + offset + full_width / 2),
                 (endx, endy + offset)])
            offset -= spacing
        if half_barb[index]:
            if offset == length:
                poly_verts.append((endx, endy + offset))
                offset -= 1.5 * spacing
            poly_verts.extend(
                [(endx, endy + offset),
                 (endx + barb_height / 2, endy + offset + full_width / 4),
                 (endx, endy + offset)])
        poly_verts = transforms.Affine2D().rotate(-angle).transform(
            poly_verts)
        barb_list.append(poly_verts)
    return barb_list


def set_UVC_draw_two_flag(self, U, V, C=None):
    from matplotlib import cbook
    def _check_consistent_shapes(*arrays):
        all_shapes = {a.shape for a in arrays}
        if len(all_shapes) != 1:
            raise ValueError('The shapes of the passed in arrays do not match')

    self.u = ma.masked_invalid(U, copy=True).ravel()
    self.v = ma.masked_invalid(V, copy=True).ravel()
    if len(self.flip) == 1:
        flip = np.broadcast_to(self.flip, self.u.shape)
    else:
        flip = self.flip

    if C is not None:
        c = ma.masked_invalid(C, copy=True).ravel()
        x, y, u, v, c, flip = cbook.delete_masked_points(
            self.x.ravel(), self.y.ravel(), self.u, self.v, c,
            flip.ravel())
        _check_consistent_shapes(x, y, u, v, c, flip)
    else:
        x, y, u, v, flip = cbook.delete_masked_points(
            self.x.ravel(), self.y.ravel(), self.u, self.v, flip.ravel())
        _check_consistent_shapes(x, y, u, v, flip)

    magnitude = np.hypot(u, v)
    full_nflags, empty_nflags, barbs, halves, empty = self._find_tails(magnitude,
                                                                       self.rounding,
                                                                       **self.barb_increments)
    plot_barbs = self._make_barbs(u, v, full_nflags, empty_nflags, barbs, halves, empty,
                                  self._length, self._pivot, self.sizes,
                                  self.fill_empty, flip)
    self.set_verts(plot_barbs)
    if C is not None:
        self.set_array(c)
    xy = np.column_stack((x, y))
    self._offsets = xy
    self.stale = True


def _find_tails_draw_two_flag(self, mag, rounding=True, half=5, full=10, empty_flag=50, full_flag=125):
    if rounding:
        mag = half * (mag / half + 0.5).astype(int)

    num_full_nflags = np.floor(mag / full_flag).astype(int)
    mag = mag % full_flag

    num_empty_nflags = np.floor(mag / empty_flag).astype(int)
    mag = mag % empty_flag

    num_barb = np.floor(mag / full).astype(int)
    mag = mag % full

    half_flag = mag >= half
    is_empty_flag = ~(half_flag | (num_full_nflags > 0) | (num_empty_nflags > 0) | (num_barb > 0))

    return num_full_nflags, num_empty_nflags, num_barb, half_flag, is_empty_flag


def change_barb_of_draw_below_2m():
    matplotlib.quiver.Barbs._make_barbs = _make_barbs_draw_below_2m


def change_barb_of_draw_empty_flag():
    matplotlib.quiver.Barbs._make_barbs = _make_barbs_draw_empty_flag


def change_barb_of_draw_two_flag():
    matplotlib.quiver.Barbs._make_barbs = _make_barbs_draw_two_flag
    matplotlib.quiver.Barbs.set_UVC = set_UVC_draw_two_flag
    matplotlib.quiver.Barbs._find_tails = _find_tails_draw_two_flag
