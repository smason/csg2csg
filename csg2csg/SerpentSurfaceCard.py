#!/usr/env/python3

from csg2csg.SurfaceCard import SurfaceCard, SurfaceType


# write the general form of a plane
def serpent_plane_string(SurfaceCard):
    string = " plane " + str(SurfaceCard.surface_coefficients[0]) + " "
    string += str(SurfaceCard.surface_coefficients[1]) + " "
    string += str(SurfaceCard.surface_coefficients[2]) + " "
    string += str(SurfaceCard.surface_coefficients[3]) + "\n"
    return string


# write the specific x form of the plane
def serpent_plane_x_string(SurfaceCard):
    string = " px " + str(SurfaceCard.surface_coefficients[3]) + "\n"
    return string


# write the specific y form of the plane
def serpent_plane_y_string(SurfaceCard):
    string = " py " + str(SurfaceCard.surface_coefficients[3]) + "\n"
    return string


# write the specific z form of the plane
def serpent_plane_z_string(SurfaceCard):
    string = " pz " + str(SurfaceCard.surface_coefficients[3]) + "\n"
    return string


# write a cylinder_x
def serpent_cylinder_x(SurfaceCard):
    string = " cylx " + str(SurfaceCard.surface_coefficients[0]) + " "
    string += str(SurfaceCard.surface_coefficients[1]) + " "
    string += str(SurfaceCard.surface_coefficients[2]) + " "
    string += "\n"
    return string


# write a cylinder_y
def serpent_cylinder_y(SurfaceCard):
    string = " cyly " + str(SurfaceCard.surface_coefficients[0]) + " "
    string += str(SurfaceCard.surface_coefficients[1]) + " "
    string += str(SurfaceCard.surface_coefficients[2]) + " "
    string += "\n"
    return string


# write a cylinder_z
def serpent_cylinder_z(SurfaceCard):
    string = " cylz " + str(SurfaceCard.surface_coefficients[0]) + " "
    string += str(SurfaceCard.surface_coefficients[1]) + " "
    string += str(SurfaceCard.surface_coefficients[2]) + " "
    string += "\n"
    return string


# write a sphere
def serpent_sphere(SurfaceCard):
    a, b, c, d = SurfaceCard.surface_coefficients
    return f" sph {a} {b} {c} {d}\n"


# write a general quadratic
def serpent_gq(SurfaceCard):
    string = " quadratic "
    for coefficient in SurfaceCard.surface_coefficients:
        string += " " + str(coefficient) + " "
    string += "\n"
    return string


# its not clear how we deal with +-1 cones for serpent}
# write a cone along x - jaakko has implemented a special
# version for mcnp comparisons - ckx/y/z
def serpent_cone_x(SurfaceCard):
    x = SurfaceCard.surface_coefficients[0]
    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    r = SurfaceCard.surface_coefficients[3]

    if len(SurfaceCard.surface_coefficients) > 4:
        side = SurfaceCard.surface_coefficients[4]
        string = " {} {:f} {:f} {:f} {:f} {:f}\n".format("ckx", x, y, z, r, side)
    else:
        string = " {} {:f} {:f} {:f} {:f}\n".format("ckx", x, y, z, r)

    return string


# serpent a cone along y
def serpent_cone_y(SurfaceCard):
    x = SurfaceCard.surface_coefficients[0]
    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    r = SurfaceCard.surface_coefficients[3]

    if len(SurfaceCard.surface_coefficients) > 4:
        side = SurfaceCard.surface_coefficients[4]
        string = " {} {:f} {:f} {:f} {:f} {:f}\n".format("cky", x, y, z, r, side)
    else:
        string = " {} {:f} {:f} {:f} {:f}\n".format("cky", x, y, z, r)

    return string


# serpent a cone along z
def serpent_cone_z(SurfaceCard):
    x = SurfaceCard.surface_coefficients[0]
    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    r = SurfaceCard.surface_coefficients[3]

    if len(SurfaceCard.surface_coefficients) > 4:
        side = SurfaceCard.surface_coefficients[4]
        string = " {} {:f} {:f} {:f} {:f} {:f}\n".format("ckz", x, y, z, r, side)
    else:
        string = " {} {:f} {:f} {:f} {:f}\n".format("ckz", x, y, z, r)

    return string


# serpent a torus x
def serpent_torus_x(SurfaceCard):
    x = SurfaceCard.surface_coefficients[0]
    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    a = SurfaceCard.surface_coefficients[3]
    b = SurfaceCard.surface_coefficients[4]
    c = SurfaceCard.surface_coefficients[5]
    string = " {} {:f} {:f} {:f} {:f} {:f} {:f}\n".format("torx", x, y, z, a, b, c)
    return string


# serpent a torus y
def serpent_torus_y(SurfaceCard):
    x = SurfaceCard.surface_coefficients[0]
    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    a = SurfaceCard.surface_coefficients[3]
    b = SurfaceCard.surface_coefficients[4]
    c = SurfaceCard.surface_coefficients[5]
    string = " {} {:f} {:f} {:f} {:f} {:f} {:f}\n".format("tory", x, y, z, a, b, c)
    return string


# serpent a torus z
def serpent_torus_z(SurfaceCard):
    x = SurfaceCard.surface_coefficients[0]
    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    a = SurfaceCard.surface_coefficients[3]
    b = SurfaceCard.surface_coefficients[4]
    c = SurfaceCard.surface_coefficients[5]
    string = " {} {:f} {:f} {:f} {:f} {:f} {:f}\n".format("torz", x, y, z, a, b, c)
    return string


"""
# write a conex
def serpent_cone_x(SurfaceCard):
    
        mcnp xyz r2 -1 +1
        *
        ||
        | \
        |  \
        |   \
        |    \
        |     \
        *------*
        
    From the bounding coodinate appropriate in 
    this case - if pointing down need the lowest value
        
    
    # cone points down from xyz
    if SurfaceCard.surface_coefficients[4] == -1:
        h = abs(SurfaceCard.b_box[0])
        x = SurfaceCard.b_box[0]
    # cone point up from xyz
    if SurfaceCard.surface_coefficients[4] == 1:
        h = abs(SurfaceCard.b_box[1])
        x = SurfaceCard.b_box[1]

    y = SurfaceCard.surface_coefficients[1]
    z = SurfaceCard.surface_coefficients[2]
    r = h*sqrt(SurfaceCard.surface_coefficients[3])

    string = ' {} {:f} {:f} {:f} {:f} {:f}'.format("conx",x,y,z,r,h)
  
    return string

# write a cone y
def serpent_cone_y(SurfaceCard):
    
        mcnp xyz r2 -1 +1
        *
        ||
        | \
        |  \
        |   \
        |    \
        |     \
        *------*
        
    From the bounding coodinate appropriate in 
    this case - if pointing down need the lowest value
        
    
    # cone points down from xyz
    if SurfaceCard.surface_coefficients[4] == -1:
        h = abs(SurfaceCard.b_box[2])
        y = SurfaceCard.b_box[2]
    # cone point up from xyz
    if SurfaceCard.surface_coefficients[4] == 1:
        h = abs(SurfaceCard.b_box[3])
        y = SurfaceCard.b_box[3]

    x = SurfaceCard.surface_coefficients[0]
    z = SurfaceCard.surface_coefficients[2]
    r = h*sqrt(SurfaceCard.surface_coefficients[3])

    string = ' {} {:f} {:f} {:f} {:f} {:f}'.format("cony",x,y,z,r,h)
  
    return string

# write a cone z
def serpent_cone_z(SurfaceCard):
    
        mcnp xyz r2 -1 +1
        *
        ||
        | \
        |  \
        |   \
        |    \
        |     \
        *------*
        
    From the bounding coodinate appropriate in 
    this case - if pointing down need the lowest value
        
    
    # cone points down from xyz
    if SurfaceCard.surface_coefficients[4] == -1:
        h = abs(SurfaceCard.b_box[5])
        z = SurfaceCard.b_box[5]
    # cone point up from xyz
    if SurfaceCard.surface_coefficients[4] == 1:
        h = abs(SurfaceCard.b_box[6])
        z = SurfaceCard.b_box[6]

    x = SurfaceCard.surface_coefficients[0]
   y = SurfaceCard.surface_coefficients[1]
    r = h*sqrt(SurfaceCard.surface_coefficients[3])

  
    return string

"""

_SURFACE_WRITERS = {
    SurfaceType.PLANE_GENERAL: serpent_plane_string,
    SurfaceType.PLANE_X: serpent_plane_x_string,
    SurfaceType.PLANE_Y: serpent_plane_y_string,
    SurfaceType.PLANE_Z: serpent_plane_z_string,
    SurfaceType.CYLINDER_X: serpent_cylinder_x,
    SurfaceType.CYLINDER_Y: serpent_cylinder_y,
    SurfaceType.CYLINDER_Z: serpent_cylinder_z,
    SurfaceType.SPHERE_GENERAL: serpent_sphere,
    SurfaceType.CONE_X: serpent_cone_x,
    SurfaceType.CONE_Y: serpent_cone_y,
    SurfaceType.CONE_Z: serpent_cone_z,
    SurfaceType.TORUS_X: serpent_torus_x,
    SurfaceType.TORUS_Y: serpent_torus_y,
    SurfaceType.TORUS_Z: serpent_torus_z,
    SurfaceType.GENERAL_QUADRATIC: serpent_gq,
}


# write the surface description to file
def write_serpent_surface(filestream, SurfaceCard):
    st = SurfaceCard.surface_type
    if st not in _SURFACE_WRITERS:
        raise ValueError(f"Unsupported surface type {st!r}")

    tail = _SURFACE_WRITERS[st](SurfaceCard)
    filestream.write(f"surf {SurfaceCard.surface_id}{tail}")


class SerpentSurfaceCard(SurfaceCard):
    def __init__(self, card_string):
        SurfaceCard.__init__(self, card_string)

    def write(self):
        print("hello")
