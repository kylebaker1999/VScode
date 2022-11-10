import math
def compute_volume(radius, height):
        volume = math.pi * radius ** 2 * height
        return volume

def compute_surface_area(radius, height):
        surface_area = 2 * math.pi *radius * (radius 
        + height)
        return surface_area


def main():

    name = "#1 Picnic"
    radius = 6.83 
    height = 10.16
    cost_per = .28
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#1 Tall"
    radius = 7.78 
    height = 11.91
    cost_per = .43
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#2"
    radius = 8.73 
    height = 11.59
    cost_per = .45
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#2.5"
    radius = 10.32 
    height = 11.91
    cost_per = .28
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#3 Cylinder"
    radius = 10.79 
    height = 17.78
    cost_per = .86
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#5"
    radius = 13.02 
    height = 14.29
    cost_per = .83
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#6Z"
    radius = 5.40 
    height = 8.89
    cost_per = .22
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#8Z short"
    radius = 6.83 
    height = 7.62
    cost_per = .26
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#10"
    radius = 15.72 
    height = 17.78
    cost_per = 1.53
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#211"
    radius = 6.83
    height = 12.38
    cost_per = .34
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#300"
    radius = 7.62 
    height = 11.27
    cost_per = .38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")

    name = "#303"
    radius = 8.10
    height = 11.11
    cost_per = .42
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_eff = volume / surface_area
    print(f"{name} {storage_eff:.2f}")
main()


