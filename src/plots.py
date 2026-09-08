from matplotlib import pyplot as plt


def plot_development_factors(ldfs, path):
    plt.figure(figsize=(8, 5))

    plt.plot(ldfs.index, ldfs.values, marker='o')

    plt.xlabel('Development Lag')
    plt.ylabel('Age-to-Age Factor')
    plt.title('Development Factors by Lag')

    plt.axhline(y=1.0, linestyle='--')
    plt.grid(alpha=0.3)

    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
