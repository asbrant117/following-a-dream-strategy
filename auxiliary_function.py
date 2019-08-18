def animation(animation_input, sprite_cgaracter):
    anim = []
    for frame in animation_input:
        anim.append(sprite_cgaracter(frame))
    return anim
