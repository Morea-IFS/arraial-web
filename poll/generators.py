

def cripto(id, number):
    for i in range(10):
        number = number.replace(str(i), lists[id][i])
    return number

def descripto(id, text):
    for i in range(10):
        text = text.replace(lists[id][i], str(i))
    return text

lists = [
    ['Au', 'lm', 'Pq', 'rs', 'bC', 'gD', 'fj', 'Hv', 'wI', 'nK'],
    ['Cp', 'vR', 'Xe', 'qZ', 'Yg', 'Bd', 'MT', 'nJ', 'ak', 'Uh'],
    ['Zx', 'Nt', 'eK', 'Ra', 'oF', 'sy', 'HG', 'Vm', 'Lw', 'cj'],
    ['Up', 'Ki', 'mS', 'DJ', 'zo', 'Xb', 'tv', 'WA', 'rn', 'gL'],
    ['ae', 'QN', 'lx', 'Py', 'sC', 'fz', 'MJ', 'Ku', 'br', 'WV'],
    ['Th', 'Ec', 'aN', 'UB', 'yw', 'pq', 'GL', 'Xr', 'mo', 'Vd'],
    ['dv', 'LU', 'rb', 'Az', 'TY', 'mc', 'jh', 'Eg', 'QP', 'nW'],
    ['ih', 'Wo', 'Mz', 'cl', 'gT', 'NJ', 'Fu', 'ae', 'Yx', 'bk'],
    ['zd', 'KW', 'HF', 'pn', 'vo', 'qJ', 'Xm', 'Ca', 'eg', 'Ru'],
    ['BL', 'tx', 'Nq', 'AK', 'ew', 'rM', 'Oy', 'uh', 'jd', 'VP'],
    ['TM', 'PQ', 'Gb', 'nY', 'CB', 'oz', 'me', 'bo', 'rW', 'EL'],
    ['pv', 'Tb', 'eI', 'lM', 'KN', 'NU', 'KH', 'AW', 'QO', 'Rx'],
    ['ke', 'Zz', 'GZ', 'IP', 'qn', 'cn', 'Vw', 'oN', 'cX', 'QI'],
    ['kX', 'iX', 'Da', 'Ic', 'Px', 'iE', 'Qm', 'mD', 'bF', 'RU'],
    ['qm', 'cs', 'lo', 'sY', 'Ft', 'kd', 'mL', 'mX', 'od', 'Ht'],
    ['wh', 'Ha', 'Bl', 'LQ', 'cu', 'KC', 'wQ', 'PN', 'Fx', 'hr'],
    ['Ae', 'dU', 'dX', 'nz', 'ua', 'vD', 'Pw', 'iU', 'UO', 'OV'],
    ['lR', 'PK', 'Hq', 'Jb', 'OX', 'qY', 'sv', 'uZ', 'nu', 'eB'],
    ['Mc', 'Ad', 'vl', 'at', 'Me', 'kD', 'eC', 'gQ', 'sp', 'zX'],
    ['dx', 'XL', 'Uv', 'NQ', 'Du', 'TC', 'cF', 'NV', 'CH', 'CZ'],
    ['NX', 'QX', 'ji', 'sF', 'BW', 'VB', 'hv', 'uf', 'kC', 'ED'],
    ['Zi', 'py', 'gu', 'fc', 'Gm', 'Xy', 'gB', 'PF', 'vc', 'uy'],
    ['SV', 'hQ', 'hV', 'ax', 'rR', 'Ui', 'Eq', 'Nj', 'uo', 'mH'],
    ['YQ', 'MN', 'Gi', 'Ge', 'qA', 'Ul', 'zt', 'PB', 'LZ', 'zu'],
    ['lk', 'kg', 'HT', 'Re', 'to', 'Xv', 'GO', 'UN', 'HM', 'hn'],
    ['er', 'hf', 'Ap', 'oZ', 'kR', 'Qg', 'YJ', 'oB', 'Zr', 'Et'],
    ['yp', 'ce', 'Gj', 'AU', 'JX', 'jn', 'pc', 'XW', 'rl', 'lF'],
    ['TF', 'hZ', 'cJ', 'cG', 'CK', 'kT', 'iw', 'Ee', 'LJ', 'ot'],
    ['Bu', 'oS', 'yR', 'Vo', 'EC', 'xK', 'ei', 'qi', 'Mq', 'fF'],
    ['zC', 'qC', 'mb', 'QG', 'Hh', 'pi', 'XP', 'kw', 'Oo', 'nq'],
    ['Tx', 'mR', 'Fq', 'DZ', 'nA', 'OW', 'Ti', 'Uk', 'Aj', 'es'],
    ['go', 'pW', 'ME', 'Tw', 'Zn', 'QM', 'jq', 'bs', 'dR', 'fO'],
    ['yS', 'dJ', 'ep', 'Hy', 'Ot', 'Tv', 'Qk', 'hO', 'yG', 'DG'],
    ['SB', 'SC', 'rP', 'vT', 'gA', 'bq', 'LH', 'Uo', 'fJ', 'gq'],
    ['Qt', 'gd', 'Xp', 'HI', 'Pf', 'Gd', 'QZ', 'zj', 'ol', 'CM'],
    ['QE', 'Zp', 'TR', 'bV', 'oj', 'EZ', 'bK', 'Bb', 'Yn', 'Ab'],
    ['VG', 'Yl', 'WC', 'pk', 'jz', 'Vz', 'gZ', 'OT', 'Fs', 'FW'],
    ['SM', 'tY', 'Mk', 'Iy', 'Gh', 'Wr', 'XK', 'Ne', 'HY', 'tE'],
    ['YL', 'yH', 'Us', 'lv', 'TJ', 'Nr', 'xA', 'Oi', 'eO', 'XZ'],
    ['Ux', 'RL', 'uN', 'Lr', 'uM', 'tn', 'LB', 'Qs', 'PI', 'Uy']
]
