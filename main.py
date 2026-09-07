from src.triangle import initial_triangle
from src.vol_weighted_factor import volume_weighted_factors
from src.cumulative_dev_factors import cumulative_dev_factor


def main():
    triangle = initial_triangle()
    ldfs = volume_weighted_factors(triangle)
    cdfs = cumulative_dev_factor(ldfs)

    print(cdfs)


if __name__ == "__main__":
    main()
