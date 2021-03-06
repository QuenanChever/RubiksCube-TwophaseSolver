# ################### Movetables describe the transformation of the coordinates by cube moves. #########################

from os import path
import array as ar
import cubie as cb
import enums
from defs import N_TWIST, N_FLIP, N_SLICE_SORTED, N_CORNERS, N_UD_EDGES, N_MOVE
from misc import get_pruning_table_path

a = cb.CubieCube()
# ########### Move table for the twists of the corners. twist < 2187 in phase 1, twist = 0 in phase 2. #################

# The twist coordinate describes the 3^7 = 2187 possible orientations of the 8 corners
table_name = "move_twist"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    twist_move = ar.array('H', [0 for i in range(N_TWIST * N_MOVE)])
    for i in range(N_TWIST):
        a.set_twist(i)
        for j in enums.Color:  # six faces U, R, F, D, L, B
            for k in range(3):  # three moves for each face, for example U, U2, U3 = U'
                a.corner_multiply(cb.basicMoveCube[j])
                twist_move[N_MOVE * i + 3 * j + k] = a.get_twist()
            a.corner_multiply(cb.basicMoveCube[j])  # 4. move restores face
    fh = open(table_path, "wb")
    twist_move.tofile(fh)
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    twist_move = ar.array('H')
    twist_move.fromfile(fh, N_TWIST * N_MOVE)
fh.close()
########################################################################################################################

# ################  Move table for the flip of the edges. flip < 2048 in phase 1, flip = 0 in phase 2.##################

# The flip coordinate describes the 2^11 = 2048 possible orientations of the 12 edges
table_name = "move_flip"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    flip_move = ar.array('H', [0 for i in range(N_FLIP * N_MOVE)])
    for i in range(N_FLIP):
        a.set_flip(i)
        for j in enums.Color:
            for k in range(3):
                a.edge_multiply(cb.basicMoveCube[j])
                flip_move[N_MOVE * i + 3 * j + k] = a.get_flip()
            a.edge_multiply(cb.basicMoveCube[j])
    fh = open(table_path, "wb")
    flip_move.tofile(fh)
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    flip_move = ar.array('H')
    flip_move.fromfile(fh, N_FLIP * N_MOVE)
fh.close()
########################################################################################################################

# ###################### Move table for the four UD-slice edges FR, FL, Bl and BR. #####################################

# The slice_sorted coordinate describes the 12!/8! = 11880 possible positions of the FR, FL, BL and BR edges.
# Though for phase 1 only the "unsorted" slice coordinate with Binomial(12,4) = 495 positions is relevant, using the
# slice_sorted coordinate gives us the permutation of the FR, FL, BL and BR edges at the beginning of phase 2 for free.
# slice_sorted  < 11880 in phase 1, slice  < 24 in phase 2, slice = 0 for solved cube
table_name = "move_slice_sorted"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    slice_sorted_move = ar.array('H', [0 for i in range(N_SLICE_SORTED * N_MOVE)])
    for i in range(N_SLICE_SORTED):
        if i % 200 == 0:
            print('.', end='', flush=True)
        a.set_slice_sorted(i)
        for j in enums.Color:
            for k in range(3):
                a.edge_multiply(cb.basicMoveCube[j])
                slice_sorted_move[N_MOVE * i + 3 * j + k] = a.get_slice_sorted()
            a.edge_multiply(cb.basicMoveCube[j])
    fh = open(table_path, "wb")
    slice_sorted_move.tofile(fh)
    print()
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    slice_sorted_move = ar.array('H')
    slice_sorted_move.fromfile(fh, N_SLICE_SORTED * N_MOVE)
fh.close()
########################################################################################################################

# ################# Move table for the u_edges coordinate for transition phase 1 -> phase 2 ############################

# The u_edges coordinate describes the 12!/8! = 11880 possible positions of the UR, UF, UL and UB edges. It is needed at
# the end of phase 1 to set up the coordinates of phase 2
# slice_sorted  < 11880 in phase 1, slice  < 24 in phase 2, slice = 0 for solved cube
table_name = "move_u_edges"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    u_edges_move = ar.array('H', [0 for i in range(N_SLICE_SORTED * N_MOVE)])
    for i in range(N_SLICE_SORTED):
        if i % 200 == 0:
            print('.', end='', flush=True)
        a.set_u_edges(i)
        for j in enums.Color:
            for k in range(3):
                a.edge_multiply(cb.basicMoveCube[j])
                u_edges_move[N_MOVE * i + 3 * j + k] = a.get_u_edges()
            a.edge_multiply(cb.basicMoveCube[j])
    fh = open(table_path, "wb")
    u_edges_move.tofile(fh)
    print()
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    u_edges_move = ar.array('H')
    u_edges_move.fromfile(fh, N_SLICE_SORTED * N_MOVE)
fh.close()
########################################################################################################################

# ################# Move table for the d_edges coordinate for transition phase 1 -> phase 2 ############################

# The d_edges coordinate describes the 12!/8! = 11880 possible positions of the DR, DF, DL and DB edges. It is needed at
# the end of phase 1 to set up the coordinates of phase 2
# slice_sorted  < 11880 in phase 1, slice  < 24 in phase 2, slice = 0 for solved cube
table_name = "move_d_edges"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    d_edges_move = ar.array('H', [0 for i in range(N_SLICE_SORTED * N_MOVE)])
    for i in range(N_SLICE_SORTED):
        if i % 200 == 0:
            print('.', end='', flush=True)
        a.set_d_edges(i)
        for j in enums.Color:
            for k in range(3):
                a.edge_multiply(cb.basicMoveCube[j])
                d_edges_move[N_MOVE * i + 3 * j + k] = a.get_d_edges()
            a.edge_multiply(cb.basicMoveCube[j])
    fh = open(table_path, "wb")
    d_edges_move.tofile(fh)
    print()
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    d_edges_move = ar.array('H')
    d_edges_move.fromfile(fh, N_SLICE_SORTED * N_MOVE)
fh.close()
########################################################################################################################

# ######################### # Move table for the edges in the U-face and D-face. URtoDB  < 40320 #######################

# The ud_edges coordinate describes the 40320 permutations of the edges UR, UF, UL, UB, DR, DF, DL and DB in phase 2
table_name = "move_ud_edges"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    ud_edges_move = ar.array('H', [0 for i in range(N_UD_EDGES * N_MOVE)])
    for i in range(N_UD_EDGES):
        if (i+1) % 600 == 0:
            print('.', end='', flush=True)
        if (i+1) % 48000 == 0:
            print('')
        a.set_ud_edges(i)
        for j in enums.Color:
            for k in range(3):
                a.edge_multiply(cb.basicMoveCube[j])
                # only R2, F2, L2 and B2 in phase 2
                if j in [enums.Color.R, enums.Color.F, enums.Color.L, enums.Color.B] and k != 1:
                    continue
                ud_edges_move[N_MOVE * i + 3 * j + k] = a.get_ud_edges()
            a.edge_multiply(cb.basicMoveCube[j])
    fh = open(table_path, "wb")
    ud_edges_move.tofile(fh)
    print()
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    ud_edges_move = ar.array('H')
    ud_edges_move.fromfile(fh, N_UD_EDGES * N_MOVE)
fh.close()
########################################################################################################################

# ############################ Move table for the  corners coordinate in phase 2 #######################################

# The corners coordinate describes the 8! = 40320 permutations of the corners.
table_name = "move_corners"
table_path = get_pruning_table_path(table_name)
if not path.isfile(table_path):
    print("creating " + table_name + " table...")
    corners_move = ar.array('H', [0 for i in range(N_CORNERS * N_MOVE)])
    # Move table for the corners. corner  < 40320
    for i in range(N_CORNERS):
        if (i+1) % 200 == 0:
            print('.', end='', flush=True)
        if(i+1) % 16000 == 0:
            print('')
        a.set_corners(i)
        for j in enums.Color:
            for k in range(3):
                a.corner_multiply(cb.basicMoveCube[j])
                corners_move[N_MOVE * i + 3 * j + k] = a.get_corners()
            a.corner_multiply(cb.basicMoveCube[j])
    fh = open(table_path, "wb")
    corners_move.tofile(fh)
    fh.close()
    print()
else:
    # print("loading " + table_name + " table...")
    fh = open(table_path, "rb")
    corners_move = ar.array('H')
    corners_move.fromfile(fh, N_CORNERS * N_MOVE)
fh.close()
########################################################################################################################
