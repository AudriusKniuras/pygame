def affine_transformation(x, a, b, c, d):
    # Affine transformation
    # x in the range [a,b] transformed to y in the range [c, d]
    y = (x-a) * (d-c) / (b-a) + c
    return int(y)

def line_function(x):
    return -0.3*x + 0.2