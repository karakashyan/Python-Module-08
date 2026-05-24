import sys
import importlib.util
import importlib.metadata


def check_dependency(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def get_version(name: str) -> str:
    return importlib.metadata.version(name)


def check_all_dependencies() -> bool:
    dependencies = {
                    "pandas": "Data manipulation ready",
                    "numpy": "Numerical computation ready",
                    "matplotlib": "Visualization ready"
                   }
    status = True
    for name, description in dependencies.items():
        if check_dependency(name):
            print(f"[OK] {name} ({get_version(name)}) - {description}")
        else:
            print(f"[MISSING] {name} - {description}")
            status = False
    return status


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    if not check_all_dependencies():
        print()
        print("Some dependencies are missing.")
        print()
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print()
        print("Or install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        sys.exit(1)

    print("\npip vs Poetry:")
    print("  pip    — manual requirements.txt, no lock file by default")
    print("  Poetry — pyproject.toml + auto-generated poetry.lock")

    print("\nAnalyzing Matrix data...")

    import pandas as pd  # type: ignore[import-untyped]
    import numpy as np  # type: ignore[import-not-found]
    import matplotlib.pyplot as plt  # type: ignore[import-not-found]

    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["matrix_signal"])
    print("Generating visualization...")
    plt.figure(figsize=(12, 6), facecolor="black")
    plt.plot(df["matrix_signal"], color="lime", linewidth=0.5, alpha=0.8)
    plt.title("Matrix Signal Analysis", color="lime", fontsize=16)
    plt.xlabel("Data Point", color="lime")
    plt.ylabel("Signal Value", color="lime")
    plt.tick_params(colors="lime")
    plt.gca().set_facecolor("black")
    plt.gca().spines["bottom"].set_color("lime")
    plt.gca().spines["top"].set_color("lime")
    plt.gca().spines["left"].set_color("lime")
    plt.gca().spines["right"].set_color("lime")
    plt.savefig("matrix_analysis.png", facecolor="black")
    plt.close()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
